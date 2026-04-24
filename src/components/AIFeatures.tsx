export default function AIFeatures() {
  return (
    <section id="solutions" className="section relative border-t border-white/5 bg-ink-900/40">
      <div className="container-page">
        <div className="grid items-start gap-12 lg:grid-cols-2">
          <div>
            <p className="eyebrow">VECO Intelligence</p>
            <h2 className="mt-3 text-balance text-3xl font-bold tracking-tight sm:text-5xl">
              Talk to your enterprise data.
              <br />
              <span className="text-brand-300">Agents answer in your context.</span>
            </h2>
            <p className="mt-5 text-white/70">
              Ask complex questions in natural language and get trustworthy
              answers grounded in your governed data. Build task-specific
              agents with role-based access, explainable reasoning, and
              enterprise-ready guardrails.
            </p>

            <ul className="mt-8 space-y-4">
              {[
                {
                  t: 'Ground answers in governed data',
                  d: 'Every response cites the tables, metrics, or documents that produced it.',
                },
                {
                  t: 'Cortex LLM functions in SQL',
                  d: 'Classify, summarize, translate or extract directly in your queries — no data movement.',
                },
                {
                  t: 'Bring or choose your model',
                  d: 'Use native industry-leading models or plug in your own — hosted where your data lives.',
                },
              ].map((it) => (
                <li key={it.t} className="flex gap-4">
                  <span className="mt-0.5 flex h-8 w-8 flex-none items-center justify-center rounded-full bg-brand-400/15 text-brand-300">
                    <svg viewBox="0 0 20 20" fill="currentColor" className="h-4 w-4">
                      <path
                        fillRule="evenodd"
                        d="M16.7 5.3a1 1 0 010 1.4l-8 8a1 1 0 01-1.4 0l-4-4a1 1 0 111.4-1.4L8 12.6l7.3-7.3a1 1 0 011.4 0z"
                        clipRule="evenodd"
                      />
                    </svg>
                  </span>
                  <div>
                    <p className="font-semibold text-white">{it.t}</p>
                    <p className="text-sm text-white/65">{it.d}</p>
                  </div>
                </li>
              ))}
            </ul>

            <div className="mt-8 flex flex-col gap-3 sm:flex-row">
              <a href="#" className="btn-primary">Explore VECO Intelligence</a>
              <a href="#" className="btn-secondary">Cortex AI overview</a>
            </div>
          </div>

          <ChatMock />
        </div>
      </div>
    </section>
  )
}

function ChatMock() {
  return (
    <div className="relative">
      <div className="absolute -inset-6 -z-10 rounded-[28px] bg-gradient-to-br from-brand-500/30 to-fuchsia-500/20 blur-2xl" />
      <div className="rounded-2xl border border-white/10 bg-ink-900 p-5 shadow-glow">
        <div className="flex items-center justify-between border-b border-white/10 pb-3">
          <div className="flex items-center gap-2">
            <span className="inline-flex h-7 w-7 items-center justify-center rounded-full bg-brand-400/20 text-xs font-bold text-brand-300">
              VI
            </span>
            <div>
              <p className="text-sm font-semibold text-white">VECO Intelligence</p>
              <p className="text-[11px] text-white/50">finance-agent · governed</p>
            </div>
          </div>
          <span className="rounded-full border border-white/10 px-2 py-0.5 text-[10px] font-semibold uppercase tracking-widest text-white/60">
            Secure
          </span>
        </div>

        <div className="mt-4 space-y-3 text-sm">
          <div className="ml-auto max-w-[85%] rounded-2xl rounded-tr-sm bg-brand-500/20 px-4 py-3 text-white/90">
            Which regions drove the biggest MRR swing last quarter, and why?
          </div>

          <div className="max-w-[90%] rounded-2xl rounded-tl-sm border border-white/10 bg-white/[0.03] px-4 py-3 text-white/85">
            <p>
              EMEA contributed <b className="text-white">+$4.2M</b> MRR (↑18%),
              driven by 3 enterprise expansions. APAC contracted{' '}
              <b className="text-white">−$1.1M</b> from two mid-market churns.
            </p>
            <div className="mt-3 grid grid-cols-3 gap-2">
              {[
                { l: 'NA', v: '+2.1M', up: true },
                { l: 'EMEA', v: '+4.2M', up: true },
                { l: 'APAC', v: '−1.1M', up: false },
              ].map((r) => (
                <div
                  key={r.l}
                  className="rounded-lg border border-white/10 bg-black/20 p-3"
                >
                  <div className="text-[10px] uppercase tracking-widest text-white/50">
                    {r.l}
                  </div>
                  <div
                    className={`mt-1 text-sm font-semibold ${
                      r.up ? 'text-emerald-300' : 'text-rose-300'
                    }`}
                  >
                    {r.v}
                  </div>
                </div>
              ))}
            </div>
            <p className="mt-3 text-xs text-white/50">
              Sources: <span className="underline">fct_subscriptions</span>,{' '}
              <span className="underline">dim_customer</span>,{' '}
              <span className="underline">churn_events</span>
            </p>
          </div>
        </div>

        <div className="mt-4 flex items-center gap-2 rounded-xl border border-white/10 bg-black/30 px-3 py-2">
          <svg
            className="h-4 w-4 text-white/50"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path d="M12.9 14.32a8 8 0 111.41-1.41l4.38 4.38-1.4 1.42-4.39-4.39zM8 14A6 6 0 108 2a6 6 0 000 12z" />
          </svg>
          <input
            disabled
            className="w-full bg-transparent text-sm text-white/70 outline-none placeholder:text-white/40"
            placeholder="Ask a question about your data..."
          />
          <button className="rounded-lg bg-brand-400 px-3 py-1.5 text-xs font-semibold text-ink-950">
            Ask
          </button>
        </div>
      </div>
    </div>
  )
}
