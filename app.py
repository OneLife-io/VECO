"""VECO CRM — a Salesforce-style CRM application.

Run:
    pip install -r requirements.txt
    python seed.py        # optional, loads sample data
    python app.py         # http://localhost:5000   demo@veco.io / demo
"""
import os
from datetime import datetime, date, timedelta
from collections import defaultdict

from flask import (
    Flask, render_template, request, redirect, url_for, flash, jsonify, abort
)
from flask_login import (
    LoginManager, login_user, logout_user, login_required, current_user
)
from sqlalchemy import or_, func

from models import (
    db, User, Account, Contact, Lead, Opportunity, Activity, Note,
    OPP_STAGES, LEAD_STATUSES, ACTIVITY_TYPES, ACTIVITY_STATUSES, INDUSTRIES,
)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "veco-dev-secret-change-me")
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        os.environ.get("DATABASE_URL")
        or f"sqlite:///{os.path.join(BASE_DIR, 'veco.db')}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    login_manager = LoginManager(app)
    login_manager.login_view = "login"

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    # ------------------------------------------------------------------ helpers
    def _parse_date(value):
        if not value:
            return None
        try:
            return datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            return None

    def _parse_float(value):
        try:
            return float(value) if value not in (None, "") else None
        except ValueError:
            return None

    def _parse_int(value):
        try:
            return int(value) if value not in (None, "") else None
        except ValueError:
            return None

    @app.context_processor
    def inject_globals():
        return {
            "OPP_STAGES": OPP_STAGES,
            "LEAD_STATUSES": LEAD_STATUSES,
            "ACTIVITY_TYPES": ACTIVITY_TYPES,
            "ACTIVITY_STATUSES": ACTIVITY_STATUSES,
            "INDUSTRIES": INDUSTRIES,
            "today": date.today(),
        }

    # ----------------------------------------------------------------------- auth
    @app.route("/register", methods=["GET", "POST"])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for("dashboard"))
        if request.method == "POST":
            email = request.form["email"].strip().lower()
            name = request.form["name"].strip()
            password = request.form["password"]
            if User.query.filter_by(email=email).first():
                flash("An account with that email already exists.", "error")
                return redirect(url_for("register"))
            u = User(email=email, name=name)
            u.set_password(password)
            db.session.add(u)
            db.session.commit()
            login_user(u)
            return redirect(url_for("dashboard"))
        return render_template("register.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for("dashboard"))
        if request.method == "POST":
            email = request.form["email"].strip().lower()
            password = request.form["password"]
            user = User.query.filter_by(email=email).first()
            if user and user.check_password(password):
                login_user(user)
                return redirect(request.args.get("next") or url_for("dashboard"))
            flash("Invalid email or password.", "error")
        return render_template("login.html")

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for("login"))

    # ----------------------------------------------------------------- dashboard
    @app.route("/")
    @login_required
    def dashboard():
        today = date.today()
        month_start = today.replace(day=1)

        opps = Opportunity.query.all()
        open_opps = [o for o in opps if not o.is_closed]
        won_opps = [o for o in opps if o.is_won]
        won_this_month = [o for o in won_opps if o.close_date and o.close_date >= month_start]

        pipeline_value = sum(o.amount or 0 for o in open_opps)
        weighted_pipeline = sum(o.weighted_amount for o in open_opps)
        won_amount_month = sum(o.amount or 0 for o in won_this_month)

        stage_breakdown = defaultdict(lambda: {"count": 0, "value": 0.0})
        for o in open_opps:
            stage_breakdown[o.stage]["count"] += 1
            stage_breakdown[o.stage]["value"] += o.amount or 0
        # Order stages
        stage_breakdown_ordered = [
            (s, stage_breakdown[s]) for s in OPP_STAGES if s in stage_breakdown
        ]
        max_stage_value = max((d["value"] for _, d in stage_breakdown_ordered), default=1) or 1

        # Leaderboard
        leaderboard = (
            db.session.query(User.name, func.coalesce(func.sum(Opportunity.amount), 0))
            .join(Opportunity, Opportunity.owner_id == User.id)
            .filter(Opportunity.stage == "Closed Won")
            .filter(Opportunity.close_date >= month_start)
            .group_by(User.name)
            .order_by(func.coalesce(func.sum(Opportunity.amount), 0).desc())
            .all()
        )

        # Recent activity
        recent_activities = (
            Activity.query.order_by(Activity.created_at.desc()).limit(8).all()
        )
        my_open_tasks = (
            Activity.query.filter_by(owner_id=current_user.id, status="Open")
            .order_by(Activity.due_date.asc().nullslast())
            .limit(8)
            .all()
        )

        # New leads this week
        week_ago = today - timedelta(days=7)
        new_leads_count = Lead.query.filter(Lead.created_at >= week_ago).count()

        return render_template(
            "dashboard.html",
            pipeline_value=pipeline_value,
            weighted_pipeline=weighted_pipeline,
            won_amount_month=won_amount_month,
            won_count_month=len(won_this_month),
            open_opp_count=len(open_opps),
            new_leads_count=new_leads_count,
            stage_breakdown=stage_breakdown_ordered,
            max_stage_value=max_stage_value,
            leaderboard=leaderboard,
            recent_activities=recent_activities,
            my_open_tasks=my_open_tasks,
        )

    # ------------------------------------------------------------------ accounts
    @app.route("/accounts")
    @login_required
    def accounts_list():
        q = request.args.get("q", "").strip()
        industry = request.args.get("industry", "")
        query = Account.query
        if q:
            like = f"%{q}%"
            query = query.filter(or_(Account.name.ilike(like), Account.billing_city.ilike(like)))
        if industry:
            query = query.filter_by(industry=industry)
        accounts = query.order_by(Account.name.asc()).all()
        return render_template("accounts/list.html", accounts=accounts, q=q, industry=industry)

    @app.route("/accounts/new", methods=["GET", "POST"])
    @login_required
    def accounts_new():
        if request.method == "POST":
            a = Account(owner_id=current_user.id)
            _populate_account(a, request.form)
            db.session.add(a)
            db.session.commit()
            flash("Account created.", "success")
            return redirect(url_for("accounts_detail", account_id=a.id))
        return render_template("accounts/form.html", account=None)

    @app.route("/accounts/<int:account_id>")
    @login_required
    def accounts_detail(account_id):
        account = db.session.get(Account, account_id) or abort(404)
        notes = Note.query.filter_by(related_account_id=account.id).order_by(Note.created_at.desc()).all()
        activities = (
            Activity.query.filter_by(related_account_id=account.id)
            .order_by(Activity.created_at.desc()).all()
        )
        return render_template(
            "accounts/detail.html",
            account=account, notes=notes, activities=activities,
        )

    @app.route("/accounts/<int:account_id>/edit", methods=["GET", "POST"])
    @login_required
    def accounts_edit(account_id):
        account = db.session.get(Account, account_id) or abort(404)
        if request.method == "POST":
            _populate_account(account, request.form)
            db.session.commit()
            flash("Account updated.", "success")
            return redirect(url_for("accounts_detail", account_id=account.id))
        return render_template("accounts/form.html", account=account)

    @app.route("/accounts/<int:account_id>/delete", methods=["POST"])
    @login_required
    def accounts_delete(account_id):
        account = db.session.get(Account, account_id) or abort(404)
        db.session.delete(account)
        db.session.commit()
        flash("Account deleted.", "success")
        return redirect(url_for("accounts_list"))

    def _populate_account(a, form):
        a.name = form["name"].strip()
        a.industry = form.get("industry") or None
        a.website = form.get("website") or None
        a.phone = form.get("phone") or None
        a.employees = _parse_int(form.get("employees"))
        a.annual_revenue = _parse_float(form.get("annual_revenue"))
        a.billing_city = form.get("billing_city") or None
        a.billing_country = form.get("billing_country") or None
        a.description = form.get("description") or None

    # ------------------------------------------------------------------ contacts
    @app.route("/contacts")
    @login_required
    def contacts_list():
        q = request.args.get("q", "").strip()
        query = Contact.query
        if q:
            like = f"%{q}%"
            query = query.filter(or_(
                Contact.first_name.ilike(like),
                Contact.last_name.ilike(like),
                Contact.email.ilike(like),
                Contact.title.ilike(like),
            ))
        contacts = query.order_by(Contact.last_name.asc()).all()
        return render_template("contacts/list.html", contacts=contacts, q=q)

    @app.route("/contacts/new", methods=["GET", "POST"])
    @login_required
    def contacts_new():
        if request.method == "POST":
            c = Contact(owner_id=current_user.id)
            _populate_contact(c, request.form)
            db.session.add(c)
            db.session.commit()
            flash("Contact created.", "success")
            return redirect(url_for("contacts_detail", contact_id=c.id))
        accounts = Account.query.order_by(Account.name).all()
        prefilled_account = _parse_int(request.args.get("account_id"))
        return render_template("contacts/form.html", contact=None, accounts=accounts,
                               prefilled_account=prefilled_account)

    @app.route("/contacts/<int:contact_id>")
    @login_required
    def contacts_detail(contact_id):
        contact = db.session.get(Contact, contact_id) or abort(404)
        notes = Note.query.filter_by(related_contact_id=contact.id).order_by(Note.created_at.desc()).all()
        activities = (
            Activity.query.filter_by(related_contact_id=contact.id)
            .order_by(Activity.created_at.desc()).all()
        )
        return render_template(
            "contacts/detail.html",
            contact=contact, notes=notes, activities=activities,
        )

    @app.route("/contacts/<int:contact_id>/edit", methods=["GET", "POST"])
    @login_required
    def contacts_edit(contact_id):
        contact = db.session.get(Contact, contact_id) or abort(404)
        if request.method == "POST":
            _populate_contact(contact, request.form)
            db.session.commit()
            flash("Contact updated.", "success")
            return redirect(url_for("contacts_detail", contact_id=contact.id))
        accounts = Account.query.order_by(Account.name).all()
        return render_template("contacts/form.html", contact=contact, accounts=accounts,
                               prefilled_account=None)

    @app.route("/contacts/<int:contact_id>/delete", methods=["POST"])
    @login_required
    def contacts_delete(contact_id):
        contact = db.session.get(Contact, contact_id) or abort(404)
        db.session.delete(contact)
        db.session.commit()
        flash("Contact deleted.", "success")
        return redirect(url_for("contacts_list"))

    def _populate_contact(c, form):
        c.first_name = form["first_name"].strip()
        c.last_name = form["last_name"].strip()
        c.title = form.get("title") or None
        c.email = (form.get("email") or "").strip().lower() or None
        c.phone = form.get("phone") or None
        c.mobile = form.get("mobile") or None
        c.department = form.get("department") or None
        c.description = form.get("description") or None
        c.account_id = _parse_int(form.get("account_id"))

    # --------------------------------------------------------------------- leads
    @app.route("/leads")
    @login_required
    def leads_list():
        q = request.args.get("q", "").strip()
        status = request.args.get("status", "")
        show_converted = request.args.get("converted", "")
        query = Lead.query
        if not show_converted:
            query = query.filter_by(converted=False)
        if q:
            like = f"%{q}%"
            query = query.filter(or_(
                Lead.first_name.ilike(like),
                Lead.last_name.ilike(like),
                Lead.company.ilike(like),
                Lead.email.ilike(like),
            ))
        if status:
            query = query.filter_by(status=status)
        leads = query.order_by(Lead.created_at.desc()).all()
        return render_template("leads/list.html", leads=leads, q=q, status=status,
                               show_converted=show_converted)

    @app.route("/leads/new", methods=["GET", "POST"])
    @login_required
    def leads_new():
        if request.method == "POST":
            lead = Lead(owner_id=current_user.id)
            _populate_lead(lead, request.form)
            db.session.add(lead)
            db.session.commit()
            flash("Lead created.", "success")
            return redirect(url_for("leads_detail", lead_id=lead.id))
        return render_template("leads/form.html", lead=None)

    @app.route("/leads/<int:lead_id>")
    @login_required
    def leads_detail(lead_id):
        lead = db.session.get(Lead, lead_id) or abort(404)
        notes = Note.query.filter_by(related_lead_id=lead.id).order_by(Note.created_at.desc()).all()
        activities = (
            Activity.query.filter_by(related_lead_id=lead.id)
            .order_by(Activity.created_at.desc()).all()
        )
        return render_template(
            "leads/detail.html", lead=lead, notes=notes, activities=activities,
        )

    @app.route("/leads/<int:lead_id>/edit", methods=["GET", "POST"])
    @login_required
    def leads_edit(lead_id):
        lead = db.session.get(Lead, lead_id) or abort(404)
        if request.method == "POST":
            _populate_lead(lead, request.form)
            db.session.commit()
            flash("Lead updated.", "success")
            return redirect(url_for("leads_detail", lead_id=lead.id))
        return render_template("leads/form.html", lead=lead)

    @app.route("/leads/<int:lead_id>/delete", methods=["POST"])
    @login_required
    def leads_delete(lead_id):
        lead = db.session.get(Lead, lead_id) or abort(404)
        db.session.delete(lead)
        db.session.commit()
        flash("Lead deleted.", "success")
        return redirect(url_for("leads_list"))

    @app.route("/leads/<int:lead_id>/convert", methods=["GET", "POST"])
    @login_required
    def leads_convert(lead_id):
        lead = db.session.get(Lead, lead_id) or abort(404)
        if lead.converted:
            flash("Lead has already been converted.", "info")
            return redirect(url_for("leads_detail", lead_id=lead.id))
        existing_account = Account.query.filter(func.lower(Account.name) == lead.company.lower()).first()
        if request.method == "POST":
            # Account
            account_id = _parse_int(request.form.get("account_id"))
            if account_id:
                account = db.session.get(Account, account_id)
            else:
                account = Account(
                    name=request.form.get("account_name", lead.company).strip(),
                    industry=lead.industry,
                    phone=lead.phone,
                    owner_id=current_user.id,
                )
                db.session.add(account)
                db.session.flush()
            # Contact
            contact = Contact(
                first_name=lead.first_name,
                last_name=lead.last_name,
                title=lead.title,
                email=lead.email,
                phone=lead.phone,
                account_id=account.id,
                owner_id=current_user.id,
            )
            db.session.add(contact)
            db.session.flush()
            # Opportunity (optional)
            if request.form.get("create_opportunity") == "on":
                opp = Opportunity(
                    name=request.form.get("opportunity_name") or f"{lead.company} - New Business",
                    account_id=account.id,
                    contact_id=contact.id,
                    stage="Qualification",
                    amount=_parse_float(request.form.get("amount")) or lead.estimated_value or 0,
                    probability=20,
                    close_date=_parse_date(request.form.get("close_date")) or (date.today() + timedelta(days=30)),
                    type="New Business",
                    source=lead.source,
                    owner_id=current_user.id,
                )
                db.session.add(opp)
            lead.converted = True
            lead.converted_at = datetime.utcnow()
            lead.status = "Qualified"
            db.session.commit()
            flash("Lead converted.", "success")
            return redirect(url_for("accounts_detail", account_id=account.id))
        return render_template("leads/convert.html", lead=lead, existing_account=existing_account)

    def _populate_lead(lead, form):
        lead.first_name = form["first_name"].strip()
        lead.last_name = form["last_name"].strip()
        lead.company = form["company"].strip()
        lead.title = form.get("title") or None
        lead.email = (form.get("email") or "").strip().lower() or None
        lead.phone = form.get("phone") or None
        lead.industry = form.get("industry") or None
        lead.status = form.get("status") or "New"
        lead.source = form.get("source") or None
        lead.rating = form.get("rating") or None
        lead.estimated_value = _parse_float(form.get("estimated_value"))
        lead.description = form.get("description") or None

    # ------------------------------------------------------------- opportunities
    @app.route("/opportunities")
    @login_required
    def opps_list():
        q = request.args.get("q", "").strip()
        stage = request.args.get("stage", "")
        query = Opportunity.query
        if q:
            like = f"%{q}%"
            query = query.filter(Opportunity.name.ilike(like))
        if stage:
            query = query.filter_by(stage=stage)
        opps = query.order_by(Opportunity.close_date.asc().nullslast()).all()
        return render_template("opportunities/list.html", opps=opps, q=q, stage=stage)

    @app.route("/opportunities/new", methods=["GET", "POST"])
    @login_required
    def opps_new():
        if request.method == "POST":
            opp = Opportunity(owner_id=current_user.id)
            _populate_opp(opp, request.form)
            db.session.add(opp)
            db.session.commit()
            flash("Opportunity created.", "success")
            return redirect(url_for("opps_detail", opp_id=opp.id))
        accounts = Account.query.order_by(Account.name).all()
        contacts = Contact.query.order_by(Contact.last_name).all()
        prefilled_account = _parse_int(request.args.get("account_id"))
        return render_template("opportunities/form.html", opp=None, accounts=accounts,
                               contacts=contacts, prefilled_account=prefilled_account)

    @app.route("/opportunities/<int:opp_id>")
    @login_required
    def opps_detail(opp_id):
        opp = db.session.get(Opportunity, opp_id) or abort(404)
        notes = Note.query.filter_by(related_opportunity_id=opp.id).order_by(Note.created_at.desc()).all()
        activities = (
            Activity.query.filter_by(related_opportunity_id=opp.id)
            .order_by(Activity.created_at.desc()).all()
        )
        return render_template(
            "opportunities/detail.html", opp=opp, notes=notes, activities=activities,
        )

    @app.route("/opportunities/<int:opp_id>/edit", methods=["GET", "POST"])
    @login_required
    def opps_edit(opp_id):
        opp = db.session.get(Opportunity, opp_id) or abort(404)
        if request.method == "POST":
            _populate_opp(opp, request.form)
            db.session.commit()
            flash("Opportunity updated.", "success")
            return redirect(url_for("opps_detail", opp_id=opp.id))
        accounts = Account.query.order_by(Account.name).all()
        contacts = Contact.query.order_by(Contact.last_name).all()
        return render_template("opportunities/form.html", opp=opp, accounts=accounts,
                               contacts=contacts, prefilled_account=None)

    @app.route("/opportunities/<int:opp_id>/delete", methods=["POST"])
    @login_required
    def opps_delete(opp_id):
        opp = db.session.get(Opportunity, opp_id) or abort(404)
        db.session.delete(opp)
        db.session.commit()
        flash("Opportunity deleted.", "success")
        return redirect(url_for("opps_list"))

    def _populate_opp(opp, form):
        opp.name = form["name"].strip()
        opp.account_id = _parse_int(form.get("account_id"))
        opp.contact_id = _parse_int(form.get("contact_id"))
        opp.stage = form.get("stage") or "Prospecting"
        opp.amount = _parse_float(form.get("amount")) or 0
        opp.probability = _parse_int(form.get("probability")) or 10
        opp.close_date = _parse_date(form.get("close_date"))
        opp.type = form.get("type") or None
        opp.source = form.get("source") or None
        opp.next_step = form.get("next_step") or None
        opp.description = form.get("description") or None

    # -------------------------------------------------------------- pipeline
    @app.route("/pipeline")
    @login_required
    def pipeline():
        opps = Opportunity.query.order_by(Opportunity.close_date.asc().nullslast()).all()
        by_stage = {s: [] for s in OPP_STAGES}
        totals = {s: 0.0 for s in OPP_STAGES}
        for o in opps:
            by_stage.setdefault(o.stage, []).append(o)
            totals[o.stage] = totals.get(o.stage, 0.0) + (o.amount or 0)
        return render_template("pipeline.html", by_stage=by_stage, totals=totals)

    @app.route("/api/opportunities/<int:opp_id>/stage", methods=["POST"])
    @login_required
    def api_update_stage(opp_id):
        opp = db.session.get(Opportunity, opp_id) or abort(404)
        data = request.get_json(silent=True) or {}
        stage = data.get("stage")
        if stage not in OPP_STAGES:
            return jsonify({"error": "invalid stage"}), 400
        opp.stage = stage
        if stage == "Closed Won":
            opp.probability = 100
            if not opp.close_date or opp.close_date > date.today():
                opp.close_date = date.today()
        elif stage == "Closed Lost":
            opp.probability = 0
        db.session.commit()
        return jsonify({"ok": True, "stage": opp.stage})

    # ------------------------------------------------------------------ reports
    @app.route("/reports")
    @login_required
    def reports():
        today = date.today()
        month_start = today.replace(day=1)
        quarter_start = today.replace(month=((today.month - 1) // 3) * 3 + 1, day=1)
        year_start = today.replace(month=1, day=1)

        won_month = (
            db.session.query(func.coalesce(func.sum(Opportunity.amount), 0))
            .filter(Opportunity.stage == "Closed Won")
            .filter(Opportunity.close_date >= month_start)
            .scalar() or 0
        )
        won_quarter = (
            db.session.query(func.coalesce(func.sum(Opportunity.amount), 0))
            .filter(Opportunity.stage == "Closed Won")
            .filter(Opportunity.close_date >= quarter_start)
            .scalar() or 0
        )
        won_year = (
            db.session.query(func.coalesce(func.sum(Opportunity.amount), 0))
            .filter(Opportunity.stage == "Closed Won")
            .filter(Opportunity.close_date >= year_start)
            .scalar() or 0
        )

        # Win rate
        closed = Opportunity.query.filter(Opportunity.stage.in_(["Closed Won", "Closed Lost"])).count()
        won = Opportunity.query.filter_by(stage="Closed Won").count()
        win_rate = (won / closed * 100) if closed else 0

        # Lead source breakdown
        source_rows = (
            db.session.query(Lead.source, func.count(Lead.id))
            .group_by(Lead.source).all()
        )
        # Pipeline by industry (open opps)
        industry_rows = (
            db.session.query(Account.industry, func.coalesce(func.sum(Opportunity.amount), 0))
            .join(Opportunity, Opportunity.account_id == Account.id)
            .filter(~Opportunity.stage.in_(["Closed Won", "Closed Lost"]))
            .group_by(Account.industry)
            .order_by(func.coalesce(func.sum(Opportunity.amount), 0).desc())
            .all()
        )
        # Top accounts by open pipeline
        top_accounts = (
            db.session.query(Account.id, Account.name,
                             func.coalesce(func.sum(Opportunity.amount), 0))
            .join(Opportunity, Opportunity.account_id == Account.id)
            .filter(~Opportunity.stage.in_(["Closed Won", "Closed Lost"]))
            .group_by(Account.id, Account.name)
            .order_by(func.coalesce(func.sum(Opportunity.amount), 0).desc())
            .limit(10).all()
        )
        # Aging open opps
        aging = []
        for opp in Opportunity.query.filter(~Opportunity.stage.in_(["Closed Won", "Closed Lost"])).all():
            age_days = (today - opp.created_at.date()).days
            aging.append((opp, age_days))
        aging.sort(key=lambda t: t[1], reverse=True)
        aging = aging[:10]

        return render_template(
            "reports.html",
            won_month=won_month, won_quarter=won_quarter, won_year=won_year,
            win_rate=win_rate, closed_count=closed, won_count=won,
            source_rows=source_rows, industry_rows=industry_rows,
            top_accounts=top_accounts, aging=aging,
        )

    # --------------------------------------------------------------- activities
    @app.route("/activities")
    @login_required
    def activities_list():
        scope = request.args.get("scope", "mine")
        status = request.args.get("status", "Open")
        query = Activity.query
        if scope == "mine":
            query = query.filter_by(owner_id=current_user.id)
        if status:
            query = query.filter_by(status=status)
        activities = query.order_by(Activity.due_date.asc().nullslast(),
                                    Activity.created_at.desc()).all()
        return render_template("activities.html", activities=activities,
                               scope=scope, status=status)

    @app.route("/activities/new", methods=["POST"])
    @login_required
    def activities_new():
        a = Activity(
            owner_id=current_user.id,
            type=request.form.get("type") or "Task",
            subject=request.form["subject"].strip(),
            description=request.form.get("description") or None,
            due_date=_parse_date(request.form.get("due_date")),
            status=request.form.get("status") or "Open",
            related_account_id=_parse_int(request.form.get("related_account_id")),
            related_contact_id=_parse_int(request.form.get("related_contact_id")),
            related_lead_id=_parse_int(request.form.get("related_lead_id")),
            related_opportunity_id=_parse_int(request.form.get("related_opportunity_id")),
        )
        db.session.add(a)
        db.session.commit()
        flash("Activity logged.", "success")
        return redirect(request.form.get("next") or url_for("activities_list"))

    @app.route("/activities/<int:activity_id>/complete", methods=["POST"])
    @login_required
    def activities_complete(activity_id):
        a = db.session.get(Activity, activity_id) or abort(404)
        a.status = "Completed"
        a.completed_at = datetime.utcnow()
        db.session.commit()
        return redirect(request.form.get("next") or url_for("activities_list"))

    @app.route("/activities/<int:activity_id>/delete", methods=["POST"])
    @login_required
    def activities_delete(activity_id):
        a = db.session.get(Activity, activity_id) or abort(404)
        nxt = request.form.get("next") or url_for("activities_list")
        db.session.delete(a)
        db.session.commit()
        return redirect(nxt)

    # -------------------------------------------------------------------- notes
    @app.route("/notes/new", methods=["POST"])
    @login_required
    def notes_new():
        n = Note(
            body=request.form["body"].strip(),
            author_id=current_user.id,
            related_account_id=_parse_int(request.form.get("related_account_id")),
            related_contact_id=_parse_int(request.form.get("related_contact_id")),
            related_lead_id=_parse_int(request.form.get("related_lead_id")),
            related_opportunity_id=_parse_int(request.form.get("related_opportunity_id")),
        )
        if not n.body:
            flash("Note cannot be empty.", "error")
        else:
            db.session.add(n)
            db.session.commit()
        return redirect(request.form.get("next") or url_for("dashboard"))

    @app.route("/notes/<int:note_id>/delete", methods=["POST"])
    @login_required
    def notes_delete(note_id):
        n = db.session.get(Note, note_id) or abort(404)
        nxt = request.form.get("next") or url_for("dashboard")
        db.session.delete(n)
        db.session.commit()
        return redirect(nxt)

    # ------------------------------------------------------------------ search
    @app.route("/search")
    @login_required
    def search():
        q = request.args.get("q", "").strip()
        results = {"accounts": [], "contacts": [], "leads": [], "opportunities": []}
        if q:
            like = f"%{q}%"
            results["accounts"] = Account.query.filter(Account.name.ilike(like)).limit(20).all()
            results["contacts"] = Contact.query.filter(or_(
                Contact.first_name.ilike(like),
                Contact.last_name.ilike(like),
                Contact.email.ilike(like),
            )).limit(20).all()
            results["leads"] = Lead.query.filter(or_(
                Lead.first_name.ilike(like),
                Lead.last_name.ilike(like),
                Lead.company.ilike(like),
                Lead.email.ilike(like),
            )).limit(20).all()
            results["opportunities"] = Opportunity.query.filter(
                Opportunity.name.ilike(like)
            ).limit(20).all()
        return render_template("search.html", q=q, results=results)

    # --------------------------------------------------------------------- init
    @app.cli.command("init-db")
    def init_db():
        with app.app_context():
            db.create_all()
            print("Database initialized.")

    with app.app_context():
        db.create_all()

    return app


app = create_app()


if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG", "").strip().lower() in ("1", "true", "yes", "on")
    app.run(debug=debug_mode, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    app.run(debug=debug_mode, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
