# VECO — The AI Data Cloud Platform

A single-page marketing site inspired by the structure and tone of the
Snowflake platform page, built as a VECO clone.

## Stack

- **Vite** (fast dev server + production build)
- **React 18** + **TypeScript**
- **Tailwind CSS 3** (design system via `tailwind.config.js`)
- Inter (Google Fonts) for typography

## Getting started

```bash
npm install
npm run dev      # start local dev server (http://localhost:5173)
npm run build    # type-check + production build into dist/
npm run preview  # preview the production build locally
```

## Sections

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
