import Logo from './Logo'

const cols = [
  {
    title: 'Platform',
    links: [
      'AI Data Cloud',
      'VECO Intelligence',
      'Cortex AI',
      'VECO Postgres',
      'Data Sharing',
      'Native Apps',
    ],
  },
  {
    title: 'Solutions',
    links: [
      'Marketing',
      'Finance',
      'Retail',
      'Healthcare',
      'Financial Services',
      'Public Sector',
    ],
  },
  {
    title: 'Developers',
    links: [
      'Documentation',
      'Quickstarts',
      'SDKs',
      'Snowpark',
      'Streamlit',
      'Reference architectures',
    ],
  },
  {
    title: 'Resources',
    links: [
      'Blog',
      'Events',
      'Customer stories',
      'Community',
      'Trust center',
      'Support',
    ],
  },
  {
    title: 'Company',
    links: ['About', 'Careers', 'Leadership', 'News', 'Investor relations', 'Contact'],
  },
]

export default function Footer() {
  return (
    <footer className="border-t border-white/5 bg-ink-950 py-16">
      <div className="container-page">
        <div className="grid gap-10 lg:grid-cols-6">
          <div className="lg:col-span-1">
            <Logo />
            <p className="mt-4 max-w-xs text-sm text-white/60">
              The AI Data Cloud — mobilize data, apps, and AI on one unified
              platform.
            </p>
            <div className="mt-5 flex items-center gap-3">
              {['x', 'li', 'yt', 'gh'].map((s) => (
                <a
                  key={s}
                  href="#"
                  className="flex h-9 w-9 items-center justify-center rounded-full border border-white/10 bg-white/5 text-white/70 transition hover:border-brand-400/50 hover:text-white"
                  aria-label={s}
                >
                  <span className="text-xs font-bold uppercase">{s}</span>
                </a>
              ))}
            </div>
          </div>

          {cols.map((c) => (
            <div key={c.title}>
              <h4 className="text-xs font-semibold uppercase tracking-[0.18em] text-white/90">
                {c.title}
              </h4>
              <ul className="mt-4 space-y-2.5">
                {c.links.map((l) => (
                  <li key={l}>
                    <a
                      href="#"
                      className="text-sm text-white/60 transition hover:text-white"
                    >
                      {l}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <div className="mt-14 flex flex-col items-start justify-between gap-4 border-t border-white/5 pt-8 text-xs text-white/50 sm:flex-row sm:items-center">
          <p>© {new Date().getFullYear()} VECO, Inc. All rights reserved.</p>
          <div className="flex flex-wrap gap-5">
            <a href="#" className="hover:text-white">Privacy</a>
            <a href="#" className="hover:text-white">Terms</a>
            <a href="#" className="hover:text-white">Security</a>
            <a href="#" className="hover:text-white">Cookie settings</a>
            <a href="#" className="hover:text-white">Do not sell my info</a>
          </div>
        </div>
      </div>
    </footer>
  )
}
