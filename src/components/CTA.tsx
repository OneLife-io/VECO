export default function CTA() {
  return (
    <section id="start" className="section">
      <div className="container-page">
        <div className="relative overflow-hidden rounded-3xl border border-white/10 bg-gradient-to-br from-brand-700 via-brand-500 to-brand-700 p-10 text-center lg:p-16">
          <div
            aria-hidden="true"
            className="pointer-events-none absolute -inset-16 bg-[radial-gradient(ellipse_at_top,_rgba(255,255,255,0.3),_transparent_60%)]"
          />
          <h2 className="relative text-balance text-3xl font-bold tracking-tight text-white sm:text-5xl">
            Mobilize your data, apps, and AI.
          </h2>
          <p className="relative mx-auto mt-4 max-w-2xl text-white/85">
            Start free and bring your first workload to the AI Data Cloud in
            minutes. Talk to our team for architecture deep dives, proofs of
            value, and migration planning.
          </p>
          <div className="relative mt-8 flex flex-col items-center justify-center gap-3 sm:flex-row">
            <a
              href="#"
              className="inline-flex items-center justify-center rounded-full bg-ink-950 px-7 py-3 text-sm font-semibold text-white transition hover:bg-ink-800"
            >
              Start for free
            </a>
            <a
              href="#"
              className="inline-flex items-center justify-center rounded-full border border-white/40 bg-white/10 px-7 py-3 text-sm font-semibold text-white transition hover:bg-white/20"
            >
              Talk to an expert
            </a>
          </div>
        </div>
      </div>
    </section>
  )
}
