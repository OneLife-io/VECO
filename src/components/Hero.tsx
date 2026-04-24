export default function Hero() {
  return (
    <section className="relative overflow-hidden hero-aurora">
      <div className="pointer-events-none absolute inset-0 grid-bg opacity-70" />
      <div className="container-page relative pt-16 pb-24 sm:pt-24 sm:pb-32 lg:pt-28 lg:pb-40">
        <div className="mx-auto max-w-4xl text-center">
          <span className="inline-flex items-center gap-2 rounded-full border border-white/15 bg-white/5 px-3 py-1 text-xs font-semibold text-white/80 backdrop-blur">
            <span className="h-1.5 w-1.5 rounded-full bg-brand-400 shadow-[0_0_12px_2px_rgba(41,181,232,0.7)]" />
            The AI Data Cloud Platform
          </span>

          <h1 className="mt-6 text-balance text-4xl font-extrabold leading-[1.05] tracking-tight sm:text-6xl lg:text-7xl">
            One unified platform.
            <br />
            <span className="bg-gradient-to-r from-brand-300 via-white to-brand-300 bg-clip-text text-transparent">
              Every data and AI workload.
            </span>
          </h1>

          <p className="mx-auto mt-6 max-w-2xl text-balance text-lg text-white/75 sm:text-xl">
            Mobilize data, apps, and AI with a fully managed, deeply integrated
            cloud — from ingestion and analytics to building and sharing the
            next generation of intelligent applications.
          </p>

          <div className="mt-9 flex flex-col items-center justify-center gap-3 sm:flex-row">
            <a href="#start" className="btn-primary">
              Start for free
            </a>
            <a href="#demo" className="btn-secondary">
              Watch the demo
              <svg
                className="ml-2 h-4 w-4"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
              >
                <path d="M6.3 4.2a1 1 0 011.55-.83l8 5.8a1 1 0 010 1.66l-8 5.8A1 1 0 016.3 15.8V4.2z" />
              </svg>
            </a>
          </div>

          <p className="mt-5 text-xs text-white/50">
            No credit card required · 30-day free trial · Deploy on AWS, Azure
            or Google Cloud
          </p>
        </div>

        <HeroVisual />
      </div>
    </section>
  )
}

function HeroVisual() {
  return (
    <div className="relative mx-auto mt-16 max-w-5xl">
      <div className="absolute -inset-8 -z-10 rounded-[36px] bg-gradient-to-br from-brand-500/30 via-fuchsia-500/10 to-brand-400/30 blur-2xl" />
      <div className="overflow-hidden rounded-2xl border border-white/10 bg-gradient-to-b from-white/[0.08] to-white/[0.02] p-2 shadow-glow backdrop-blur">
        <div className="rounded-xl border border-white/10 bg-ink-900">
          <div className="flex items-center justify-between border-b border-white/10 px-4 py-2.5">
            <div className="flex items-center gap-2">
              <span className="h-2.5 w-2.5 rounded-full bg-red-400/80" />
              <span className="h-2.5 w-2.5 rounded-full bg-yellow-300/80" />
              <span className="h-2.5 w-2.5 rounded-full bg-green-400/80" />
            </div>
            <span className="text-xs text-white/50">veco · workspace</span>
            <span className="text-xs text-brand-300">● connected</span>
          </div>

          <div className="grid gap-4 p-5 md:grid-cols-3">
            <Panel
              title="Agents"
              rows={[
                { l: 'revenue-forecast', v: 'running' },
                { l: 'churn-signals', v: 'ready' },
                { l: 'invoice-ocr', v: 'idle' },
              ]}
              accent="bg-brand-400"
            />
            <Panel
              title="Pipelines"
              rows={[
                { l: 'orders ingest', v: '1.2M / hr' },
                { l: 'clickstream', v: '840k / hr' },
                { l: 'web logs', v: '310k / hr' },
              ]}
              accent="bg-emerald-400"
            />
            <Panel
              title="Warehouses"
              rows={[
                { l: 'ANALYTICS_XS', v: '98% cache' },
                { l: 'ML_TRAIN_L', v: 'auto-scaled' },
                { l: 'APP_SERVING', v: 'healthy' },
              ]}
              accent="bg-fuchsia-400"
            />
          </div>

          <div className="border-t border-white/10 p-5">
            <div className="text-[11px] uppercase tracking-widest text-white/40">
              Query
            </div>
            <pre className="mt-2 overflow-x-auto text-sm leading-6 text-white/85">
              <code>
                <span className="text-brand-300">SELECT</span> product_id,
                {'\n'}  <span className="text-fuchsia-300">AI_COMPLETE</span>(
                <span className="text-emerald-300">'summarize reviews in 1 line'</span>, reviews) AS summary,
                {'\n'}  <span className="text-fuchsia-300">AI_CLASSIFY</span>(reviews,
                [<span className="text-emerald-300">'positive'</span>, <span className="text-emerald-300">'neutral'</span>, <span className="text-emerald-300">'negative'</span>]) AS sentiment
                {'\n'}<span className="text-brand-300">FROM</span> marketplace.products;
              </code>
            </pre>
          </div>
        </div>
      </div>
    </div>
  )
}

function Panel({
  title,
  rows,
  accent,
}: {
  title: string
  rows: { l: string; v: string }[]
  accent: string
}) {
  return (
    <div className="rounded-lg border border-white/10 bg-white/[0.03] p-4">
      <div className="flex items-center gap-2">
        <span className={`h-2 w-2 rounded-full ${accent}`} />
        <div className="text-sm font-semibold text-white">{title}</div>
      </div>
      <ul className="mt-3 space-y-2 text-xs">
        {rows.map((r) => (
          <li
            key={r.l}
            className="flex items-center justify-between rounded border border-white/5 bg-black/20 px-3 py-2"
          >
            <span className="text-white/70">{r.l}</span>
            <span className="text-white/90">{r.v}</span>
          </li>
        ))}
      </ul>
    </div>
  )
}
