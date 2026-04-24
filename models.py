from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

OPP_STAGES = [
    "Prospecting",
    "Qualification",
    "Proposal",
    "Negotiation",
    "Closed Won",
    "Closed Lost",
]

LEAD_STATUSES = ["New", "Working", "Nurturing", "Qualified", "Unqualified"]
ACTIVITY_TYPES = ["Call", "Email", "Meeting", "Task"]
ACTIVITY_STATUSES = ["Open", "Completed"]
INDUSTRIES = [
    "Technology", "Finance", "Healthcare", "Manufacturing",
    "Retail", "Education", "Energy", "Media", "Other",
]


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(160), unique=True, nullable=False, index=True)
    name = db.Column(db.String(160), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    accounts = db.relationship("Account", backref="owner", lazy="dynamic")
    contacts = db.relationship("Contact", backref="owner", lazy="dynamic")
    leads = db.relationship("Lead", backref="owner", lazy="dynamic")
    opportunities = db.relationship("Opportunity", backref="owner", lazy="dynamic")
    activities = db.relationship("Activity", backref="owner", lazy="dynamic")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Account(db.Model):
    __tablename__ = "accounts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, index=True)
    industry = db.Column(db.String(80))
    website = db.Column(db.String(200))
    phone = db.Column(db.String(60))
    employees = db.Column(db.Integer)
    annual_revenue = db.Column(db.Float)
    billing_city = db.Column(db.String(120))
    billing_country = db.Column(db.String(120))
    description = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    contacts = db.relationship("Contact", backref="account", lazy="dynamic", cascade="all, delete-orphan")
    opportunities = db.relationship("Opportunity", backref="account", lazy="dynamic", cascade="all, delete-orphan")


class Contact(db.Model):
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    title = db.Column(db.String(160))
    email = db.Column(db.String(200), index=True)
    phone = db.Column(db.String(60))
    mobile = db.Column(db.String(60))
    department = db.Column(db.String(120))
    description = db.Column(db.Text)
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"))
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()


class Lead(db.Model):
    __tablename__ = "leads"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    company = db.Column(db.String(200), nullable=False, index=True)
    title = db.Column(db.String(160))
    email = db.Column(db.String(200), index=True)
    phone = db.Column(db.String(60))
    industry = db.Column(db.String(80))
    status = db.Column(db.String(40), default="New", index=True)
    source = db.Column(db.String(80))
    rating = db.Column(db.String(20))  # Hot/Warm/Cold
    estimated_value = db.Column(db.Float)
    description = db.Column(db.Text)
    converted = db.Column(db.Boolean, default=False, index=True)
    converted_at = db.Column(db.DateTime)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()


class Opportunity(db.Model):
    __tablename__ = "opportunities"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, index=True)
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"))
    contact_id = db.Column(db.Integer, db.ForeignKey("contacts.id"))
    stage = db.Column(db.String(40), default="Prospecting", index=True)
    amount = db.Column(db.Float, default=0)
    probability = db.Column(db.Integer, default=10)
    close_date = db.Column(db.Date)
    type = db.Column(db.String(60))  # New Business, Renewal, Upsell
    source = db.Column(db.String(80))
    next_step = db.Column(db.String(255))
    description = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    contact = db.relationship("Contact")

    @property
    def is_closed(self):
        return self.stage in ("Closed Won", "Closed Lost")

    @property
    def is_won(self):
        return self.stage == "Closed Won"

    @property
    def weighted_amount(self):
        return (self.amount or 0) * (self.probability or 0) / 100.0


class Activity(db.Model):
    __tablename__ = "activities"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(40), default="Task", index=True)
    subject = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default="Open", index=True)
    due_date = db.Column(db.Date)
    completed_at = db.Column(db.DateTime)

    related_account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"))
    related_contact_id = db.Column(db.Integer, db.ForeignKey("contacts.id"))
    related_lead_id = db.Column(db.Integer, db.ForeignKey("leads.id"))
    related_opportunity_id = db.Column(db.Integer, db.ForeignKey("opportunities.id"))

    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    related_account = db.relationship("Account", backref="activities")
    related_contact = db.relationship("Contact", backref="activities")
    related_lead = db.relationship("Lead", backref="activities")
    related_opportunity = db.relationship("Opportunity", backref="activities")

    @property
    def is_overdue(self):
        return (
            self.status == "Open"
            and self.due_date is not None
            and self.due_date < date.today()
        )


class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    related_account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"))
    related_contact_id = db.Column(db.Integer, db.ForeignKey("contacts.id"))
    related_lead_id = db.Column(db.Integer, db.ForeignKey("leads.id"))
    related_opportunity_id = db.Column(db.Integer, db.ForeignKey("opportunities.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    author = db.relationship("User")
    related_account = db.relationship("Account", backref="notes")
    related_contact = db.relationship("Contact", backref="notes")
    related_lead = db.relationship("Lead", backref="notes")
    related_opportunity = db.relationship("Opportunity", backref="notes")
