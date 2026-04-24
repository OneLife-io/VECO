const pillars = [
  {
    tag: 'Easy',
    title: 'Fully managed, effortlessly scalable',
    body:
      'One platform across data types and clouds. Zero infrastructure to manage, near-zero maintenance, and pricing that scales the way you do.',
    points: [
      'Instant elasticity per workload',
      'Multi-cloud: AWS, Azure & Google Cloud',
      'Automatic performance tuning',
    ],
    icon: (
      <svg viewBox="0 0 24 24" fill="none" className="h-6 w-6" stroke="currentColor" strokeWidth="1.8">
        <path d="M4 7l8-4 8 4-8 4-8-4z" />
        <path d="M4 12l8 4 8-4" />
        <path d="M4 17l8 4 8-4" />
      </svg>
    ),
  },
  {
    tag: 'Connected',
    title: 'Data, apps, and AI — deeply integrated',
    body:
      'Go from ingestion and modeling to analytics, agents, and apps without stitching together a dozen tools. One copy of your data, one governance model, one experience.',
    points: [
      'Unified storage for structured, semi-structured & unstructured data',
      'Native Python, SQL, Java, Scala & notebooks',
      'Live data sharing across clouds',
    ],
    icon: (
      <svg viewBox="0 0 24 24" fill="none" className="h-6 w-6" stroke="currentColor" strokeWidth="1.8">
        <circle cx="6" cy="6" r="2.2" />
        <circle cx="18" cy="6" r="2.2" />
        <circle cx="6" cy="18" r="2.2" />
        <circle cx="18" cy="18" r="2.2" />
        <path d="M8 6h8M6 8v8M18 8v8M8 18h8" />
      </svg>
    ),
  },
  {
    tag: 'Trusted',
    title: 'Enterprise security by default',
    body:
      'Always-on, unified security, governance, observability, and disaster recovery — regardless of cloud or region. Built so you can say yes to more use cases.',
    points: [
      'End-to-end encryption & private connectivity',
      'Row/column policies, lineage & access history',
      'SOC 2, ISO 27001, HIPAA, PCI, FedRAMP',
    ],
    icon: (
      <svg viewBox="0 0 24 24" fill="none" className="h-6 w-6" stroke="currentColor" strokeWidth="1.8">
        <path d="M12 3l8 3v6c0 5-3.4 8.5-8 9-4.6-.5-8-4-8-9V6l8-3z" />
        <path d="M9 12l2 2 4-4" />
      </svg>
    ),
  },
]

export default function Pillars() {
  return (
    <section id="platform" className="section relative">
      <div className="container-page">
        <div className="mx-auto max-w-3xl text-center">
          <p className="eyebrow">The Platform</p>
          <h2 className="mt-3 text-balance text-3xl font-bold tracking-tight sm:text-5xl">
            A single foundation for every data and AI team
          </h2>
          <p className="mt-5 text-white/70">
            VECO eliminates silos and accelerates innovation with a trusted,
            scalable AI Data Cloud — so every team can move faster on the
            data and AI that run the business.
          </p>
        </div>

        <div className="mt-14 grid gap-6 lg:grid-cols-3">
          {pillars.map((p) => (
            <div key={p.tag} className="card group relative overflow-hidden">
              <div className="pointer-events-none absolute -right-16 -top-16 h-48 w-48 rounded-full bg-brand-400/10 blur-3xl transition group-hover:bg-brand-400/20" />
              <div className="flex items-center gap-3">
                <span className="inline-flex h-10 w-10 items-center justify-center rounded-xl bg-brand-400/15 text-brand-300">
                  {p.icon}
                </span>
                <span className="text-[11px] font-bold uppercase tracking-[0.22em] text-brand-400">
                  {p.tag}
                </span>
              </div>
              <h3 className="mt-5 text-xl font-semibold text-white">
                {p.title}
              </h3>
              <p className="mt-3 text-sm leading-relaxed text-white/70">
                {p.body}
              </p>
              <ul className="mt-5 space-y-2.5">
                {p.points.map((pt) => (
                  <li
                    key={pt}
                    className="flex items-start gap-2 text-sm text-white/80"
                  >
                    <svg
                      className="mt-0.5 h-4 w-4 flex-none text-brand-400"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                    >
                      <path
                        fillRule="evenodd"
                        d="M16.7 5.3a1 1 0 010 1.4l-8 8a1 1 0 01-1.4 0l-4-4a1 1 0 111.4-1.4L8 12.6l7.3-7.3a1 1 0 011.4 0z"
                        clipRule="evenodd"
                      />
                    </svg>
                    {pt}
                  </li>
                ))}
              </ul>
              <a
                href="#"
                className="btn-ghost mt-6"
              >
                Learn more →
              </a>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
