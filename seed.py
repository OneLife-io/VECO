"""Populate the CRM with sample data so the app feels alive on first run."""
import random
from datetime import date, datetime, timedelta

from app import app
from models import (
    db, User, Account, Contact, Lead, Opportunity, Activity, Note,
    OPP_STAGES, LEAD_STATUSES, INDUSTRIES,
)

SAMPLE_USERS = [
    ("demo@veco.io", "Demo User", "demo"),
    ("alex@veco.io", "Alex Chen", "demo"),
    ("priya@veco.io", "Priya Patel", "demo"),
    ("jordan@veco.io", "Jordan Reyes", "demo"),
]

SAMPLE_ACCOUNTS = [
    ("Acme Corporation", "Manufacturing", "https://acme.example.com", "+1 415 555 0100", 12000, 4_500_000_000, "San Francisco", "USA"),
    ("Globex", "Technology", "https://globex.example.com", "+1 212 555 0188", 3400, 980_000_000, "New York", "USA"),
    ("Initech", "Finance", "https://initech.example.com", "+1 512 555 0119", 850, 220_000_000, "Austin", "USA"),
    ("Umbrella Health", "Healthcare", "https://umbrella.example.com", "+44 20 7946 0058", 6200, 1_400_000_000, "London", "UK"),
    ("Soylent Foods", "Retail", "https://soylent.example.com", "+1 503 555 0145", 480, 95_000_000, "Portland", "USA"),
    ("Stark Industries", "Manufacturing", "https://stark.example.com", "+1 213 555 0123", 25000, 12_000_000_000, "Los Angeles", "USA"),
    ("Wayne Enterprises", "Finance", "https://wayne.example.com", "+1 312 555 0132", 18000, 8_700_000_000, "Chicago", "USA"),
    ("Hooli", "Technology", "https://hooli.example.com", "+1 650 555 0119", 9100, 3_200_000_000, "Palo Alto", "USA"),
    ("Pied Piper", "Technology", "https://piedpiper.example.com", "+1 408 555 0190", 42, 8_000_000, "San Jose", "USA"),
    ("Massive Dynamic", "Technology", "https://massive.example.com", "+1 617 555 0143", 5800, 2_900_000_000, "Boston", "USA"),
]

SAMPLE_CONTACTS = [
    ("Wile", "Coyote", "VP Procurement", "wile@acme.example.com", "+1 415 555 0101", "Acme Corporation"),
    ("Road", "Runner", "Director of Operations", "road@acme.example.com", "+1 415 555 0102", "Acme Corporation"),
    ("Hank", "Scorpio", "CEO", "hank@globex.example.com", "+1 212 555 0189", "Globex"),
    ("Bill", "Lumbergh", "VP Engineering", "bill@initech.example.com", "+1 512 555 0120", "Initech"),
    ("Peter", "Gibbons", "Senior Engineer", "peter@initech.example.com", "+1 512 555 0121", "Initech"),
    ("Ada", "Wong", "CISO", "ada@umbrella.example.com", "+44 20 7946 0059", "Umbrella Health"),
    ("Tony", "Stark", "Founder", "tony@stark.example.com", "+1 213 555 0124", "Stark Industries"),
    ("Pepper", "Potts", "COO", "pepper@stark.example.com", "+1 213 555 0125", "Stark Industries"),
    ("Bruce", "Wayne", "CEO", "bruce@wayne.example.com", "+1 312 555 0133", "Wayne Enterprises"),
    ("Lucius", "Fox", "CTO", "lucius@wayne.example.com", "+1 312 555 0134", "Wayne Enterprises"),
    ("Gavin", "Belson", "CEO", "gavin@hooli.example.com", "+1 650 555 0120", "Hooli"),
    ("Richard", "Hendricks", "Founder", "richard@piedpiper.example.com", "+1 408 555 0191", "Pied Piper"),
    ("Nina", "Sharp", "President", "nina@massive.example.com", "+1 617 555 0144", "Massive Dynamic"),
]

SAMPLE_LEADS = [
    ("Sarah", "Connor", "Cyberdyne Systems", "VP Security", "sarah@cyberdyne.example.com", "Hot", "Web", 75000),
    ("John", "Hammond", "InGen", "CEO", "john@ingen.example.com", "Warm", "Referral", 250000),
    ("Ellen", "Ripley", "Weyland-Yutani", "Director Logistics", "ripley@weyland.example.com", "Hot", "Event", 180000),
    ("Walter", "White", "Gray Matter", "Head of R&D", "walter@graymatter.example.com", "Cold", "Cold Outreach", 50000),
    ("Don", "Draper", "Sterling Cooper", "Creative Director", "don@scdp.example.com", "Warm", "Partner", 120000),
    ("Daenerys", "Targaryen", "Dragonstone Holdings", "Chair", "daenerys@dragonstone.example.com", "Hot", "Referral", 500000),
    ("Saul", "Goodman", "Wexler-McGill", "Partner", "saul@wexlermcgill.example.com", "Warm", "Web", 35000),
    ("Tyrion", "Lannister", "Casterly Rock Capital", "Hand", "tyrion@casterly.example.com", "Hot", "Event", 800000),
]

OPP_NAMES = [
    "Platform Subscription",
    "Annual Renewal",
    "Enterprise License",
    "Implementation Services",
    "Premium Support",
    "Pilot Expansion",
    "Multi-Year Deal",
    "Add-on Modules",
]

NOTE_BODIES = [
    "Spoke with the team — they're evaluating two competitors. We need to send the technical comparison doc by Friday.",
    "Decision-maker is the new CFO; she joins next month. Hold off on commercials until then.",
    "Procurement asked for SOC 2 + DPA. Sent both, awaiting redlines.",
    "Champion is solid; pulled in his manager for the next call. Looking good for end of quarter.",
    "Budget signed off. Just waiting on legal.",
]


def reset():
    db.drop_all()
    db.create_all()


def populate():
    print("Seeding users...")
    users = []
    for email, name, password in SAMPLE_USERS:
        u = User(email=email, name=name)
        u.set_password(password)
        db.session.add(u)
        users.append(u)
    db.session.flush()

    print("Seeding accounts...")
    accounts = {}
    for name, industry, website, phone, employees, revenue, city, country in SAMPLE_ACCOUNTS:
        a = Account(
            name=name, industry=industry, website=website, phone=phone,
            employees=employees, annual_revenue=revenue,
            billing_city=city, billing_country=country,
            owner_id=random.choice(users).id,
            description=f"{name} is a leading {industry.lower()} company.",
        )
        db.session.add(a)
        accounts[name] = a
    db.session.flush()

    print("Seeding contacts...")
    contacts = []
    for first, last, title, email, phone, account_name in SAMPLE_CONTACTS:
        c = Contact(
            first_name=first, last_name=last, title=title,
            email=email, phone=phone,
            account_id=accounts[account_name].id,
            owner_id=random.choice(users).id,
        )
        db.session.add(c)
        contacts.append(c)
    db.session.flush()

    print("Seeding leads...")
    for first, last, company, title, email, rating, source, value in SAMPLE_LEADS:
        l = Lead(
            first_name=first, last_name=last, company=company, title=title,
            email=email, rating=rating, source=source, estimated_value=value,
            status=random.choice(["New", "Working", "Nurturing"]),
            industry=random.choice(INDUSTRIES),
            owner_id=random.choice(users).id,
            created_at=datetime.utcnow() - timedelta(days=random.randint(0, 12)),
        )
        db.session.add(l)
    db.session.flush()

    print("Seeding opportunities...")
    today = date.today()
    opps = []
    for account in accounts.values():
        n = random.randint(1, 3)
        account_contacts = [c for c in contacts if c.account_id == account.id]
        for _ in range(n):
            stage = random.choices(
                OPP_STAGES,
                weights=[3, 4, 3, 2, 2, 1],  # bias toward open stages
                k=1,
            )[0]
            amount = random.choice([15000, 25000, 50000, 80000, 120000, 220000, 450000])
            probability = {
                "Prospecting": 10, "Qualification": 25, "Proposal": 50,
                "Negotiation": 75, "Closed Won": 100, "Closed Lost": 0,
            }[stage]
            close_offset = random.randint(-25, 60)
            opp = Opportunity(
                name=f"{account.name} - {random.choice(OPP_NAMES)}",
                account_id=account.id,
                contact_id=(account_contacts[0].id if account_contacts else None),
                stage=stage,
                amount=amount,
                probability=probability,
                close_date=today + timedelta(days=close_offset),
                type=random.choice(["New Business", "Renewal", "Upsell"]),
                source=random.choice(["Web", "Referral", "Event", "Cold Outreach", "Partner"]),
                next_step=random.choice([
                    "Send proposal", "Schedule demo", "Procurement review",
                    "Legal redlines", "Final pricing call",
                ]),
                owner_id=random.choice(users).id,
                created_at=datetime.utcnow() - timedelta(days=random.randint(5, 90)),
            )
            db.session.add(opp)
            opps.append(opp)
    db.session.flush()

    print("Seeding activities & notes...")
    subjects = {
        "Call": ["Discovery call", "Follow-up call", "Pricing discussion", "Check-in call"],
        "Email": ["Sent proposal", "Sent SOC 2 docs", "Sent contract", "Recap email"],
        "Meeting": ["Demo with team", "Onsite kickoff", "Stakeholder review"],
        "Task": ["Update CRM", "Prepare deck", "Send NDA", "Internal sync"],
    }
    for opp in random.sample(opps, k=min(len(opps), 18)):
        for _ in range(random.randint(1, 3)):
            t = random.choice(["Call", "Email", "Meeting", "Task"])
            a = Activity(
                type=t,
                subject=random.choice(subjects[t]),
                description=None,
                status=random.choice(["Open", "Open", "Completed"]),
                due_date=today + timedelta(days=random.randint(-7, 14)),
                owner_id=opp.owner_id,
                related_account_id=opp.account_id,
                related_opportunity_id=opp.id,
            )
            db.session.add(a)
    for opp in random.sample(opps, k=min(len(opps), 8)):
        n = Note(
            body=random.choice(NOTE_BODIES),
            related_account_id=opp.account_id,
            related_opportunity_id=opp.id,
            author_id=opp.owner_id,
        )
        db.session.add(n)

    db.session.commit()
    print(f"Done. {len(users)} users, {len(accounts)} accounts, {len(contacts)} contacts, "
          f"{len(SAMPLE_LEADS)} leads, {len(opps)} opportunities.")


if __name__ == "__main__":
    with app.app_context():
        reset()
        populate()
