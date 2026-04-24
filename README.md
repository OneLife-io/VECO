# VECO

This repository contains two applications:

1. **VECO CRM** — a Salesforce-style sales application (Flask + SQLite)
2. **VECO Marketing Site** — an AI Data Cloud Platform marketing site (React + TypeScript)

---

## VECO CRM

A Salesforce-style sales CRM built with Flask + SQLite. Single binary, no
external services required.

> ⚠️ This is **not** a clone of Salesforce. Salesforce is a 25-year platform
> spanning Sales Cloud, Service Cloud, Marketing Cloud, Commerce, Analytics,
> Slack, Heroku, MuleSoft, and a low-code app platform. This is a focused
> reimplementation of the **Sales Cloud core** — accounts, contacts, leads,
> opportunities, pipeline, activities, dashboards, and reports — at a level
> that's runnable on a laptop in under two minutes.

### What's included

- **Accounts** — companies you sell to, with industry/revenue/employees
- **Contacts** — people at those accounts, linked back to the account
- **Leads** — unqualified prospects, with statuses and ratings
- **Lead conversion** — turn a qualified lead into Account + Contact + Opportunity
- **Opportunities** — deals with stage, amount, probability, close date,
  next step, and a stage path tracker
- **Pipeline view** — drag-and-drop kanban across stages, with rolling totals
- **Activities** — calls, emails, meetings, tasks; due dates and overdue flagging;
  per-record activity timeline
- **Notes** — free-text notes attached to any record
- **Dashboard** — pipeline value, weighted pipeline, won-this-month, new leads,
  pipeline-by-stage chart, top-sellers leaderboard, my open tasks, recent activity
- **Reports** — won by month/quarter/year, win rate, lead-source breakdown,
  pipeline by industry, top accounts, aging open opportunities
- **Global search** — across accounts, contacts, leads, opportunities
- **Multi-user** — register/login, each record has an owner
- **Filtering** — list views with search + status/industry/stage filters

### What's *not* included

Email integration, marketing automation, custom objects/fields at runtime,
forecasting workflows, territory management, CPQ, communities, mobile apps,
process automation, Einstein AI, AppExchange, and the rest of the Salesforce
universe.

### Run it

```bash
pip install -r requirements.txt
python seed.py        # optional: load sample data
python app.py
```

Open http://localhost:5000 and sign in with `demo@veco.io` / `demo`
(other seeded users: `alex@veco.io`, `priya@veco.io`, `jordan@veco.io`, all
with password `demo`).

### Stack

- **Flask** — routing & rendering
- **SQLAlchemy** — ORM
- **Flask-Login** — sessions
- **SQLite** — file-based DB (auto-created at `veco.db`)
- **Jinja2** — server-rendered HTML
- **Vanilla CSS + JS** — Salesforce Lightning-inspired styling, drag/drop kanban

No build step. No node_modules. No frontend framework.

---

## VECO Marketing Site

A single-page marketing site inspired by the structure and tone of the
Snowflake platform page, built as a VECO clone.

### Stack

- **Vite** (fast dev server + production build)
- **React 18** + **TypeScript**
- **Tailwind CSS 3** (design system via `tailwind.config.js`)
- Inter (Google Fonts) for typography

### Getting started

```bash
npm install
npm run dev      # start local dev server (http://localhost:5173)
npm run build    # type-check + production build into dist/
npm run preview  # preview the production build locally
```

### Sections

1. Announcement bar
2. Sticky navigation (with mobile menu)
3. Hero — "One unified platform. Every data and AI workload."
4. Customer-logo marquee
5. Platform pillars — Easy / Connected / Trusted
6. VECO Intelligence (conversational AI over governed data)
7. Workloads tabs — Ingest · Analyze · Model · Share · Build apps
8. VECO Postgres callout
9. Platform stats
10. Ecosystem — Partners · Marketplace · Open Source · Developer Hub
11. CTA banner
12. Footer

## Project layout

```
# CRM (Flask)
app.py            # Flask app & all routes
models.py         # SQLAlchemy models + enums
seed.py           # Sample data
requirements.txt
templates/        # Jinja2 templates
  base.html
  dashboard.html, login.html, register.html
  pipeline.html, activities.html, reports.html, search.html
  accounts/  contacts/  leads/  opportunities/
  _activity_form.html  _note_form.html  _timeline.html
static/
  style.css       # Salesforce-style theming
  app.js          # Kanban drag/drop

# Marketing Site (React)
src/
  App.tsx
  main.tsx
  index.css
  components/
    Announcement.tsx
    Navbar.tsx
    Hero.tsx
    LogoMarquee.tsx
    Pillars.tsx
    AIFeatures.tsx
    Workloads.tsx
    Postgres.tsx
    Stats.tsx
    Ecosystem.tsx
    CTA.tsx
    Footer.tsx
    Logo.tsx
```
