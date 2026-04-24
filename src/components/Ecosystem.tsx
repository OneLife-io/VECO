const cards = [
  {
    title: 'Partners',
    desc: 'Plug into integrated technologies and certified migration experts that help you get to value faster.',
    cta: 'Browse partners',
    icon: (
      <svg viewBox="0 0 24 24" fill="none" className="h-6 w-6" stroke="currentColor" strokeWidth="1.8">
        <path d="M8 12l-3 3 4 4 3-3M16 12l3-3-4-4-3 3" />
        <path d="M9 15l6-6" />
      </svg>
    ),
  },
  {
    title: 'Marketplace',
    desc: 'Discover live data sets, ready-to-run apps, and LLMs — installed in clicks, with built-in governance.',
    cta: 'Explore marketplace',
    icon: (
      <svg viewBox="0 0 24 24" fill="none" className="h-6 w-6" stroke="currentColor" strokeWidth="1.8">
        <path d="M3 9l2-5h14l2 5" />
        <path d="M5 9v10a2 2 0 002 2h10a2 2 0 002-2V9" />
        <path d="M3 9a3 3 0 006 0 3 3 0 006 0 3 3 0 006 0" />
      </svg>
    ),
  },
  {
    title: 'Open Source',
    desc: 'Contribute to and build on the open tools VECO supports — from Iceberg and Arrow to Streamlit.',
    cta: 'View projects',
    icon: (
      <svg viewBox="0 0 24 24" fill="none" className="h-6 w-6" stroke="currentColor" strokeWidth="1.8">
        <path d="M8 3l-5 7 5 7" />
        <path d="M16 3l5 7-5 7" />
        <path d="M14 3l-4 18" />
      </svg>
    ),
  },
  {
    title: 'Developer Hub',
    desc: 'Reference architectures, quickstarts and SDKs. Level up your skill set with hands-on tutorials.',
    cta: 'Start building',
    icon: (
      <svg viewBox="0 0 24 24" fill="none" className="h-6 w-6" stroke="currentColor" strokeWidth="1.8">
        <path d="M8 9l-4 3 4 3M16 9l4 3-4 3M14 6l-4 12" />
      </svg>
    ),
  },
]

export default function Ecosystem() {
  return (
    <section id="resources" className="section">
      <div className="container-page">
        <div className="mx-auto max-w-3xl text-center">
          <p className="eyebrow">Ecosystem</p>
          <h2 className="mt-3 text-balance text-3xl font-bold tracking-tight sm:text-5xl">
            An ecosystem that scales with you
          </h2>
          <p className="mt-5 text-white/70">
            Everything you need to build faster — partners, marketplace apps
            and data, open source, and developer tools — all connected to the
            same governed platform.
          </p>
        </div>

        <div className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          {cards.map((c) => (
            <div key={c.title} className="card">
              <span className="inline-flex h-10 w-10 items-center justify-center rounded-xl bg-brand-400/15 text-brand-300">
                {c.icon}
              </span>
              <h3 className="mt-5 text-lg font-semibold text-white">
                {c.title}
              </h3>
              <p className="mt-2 text-sm text-white/70">{c.desc}</p>
              <a href="#" className="btn-ghost mt-5">{c.cta} →</a>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
