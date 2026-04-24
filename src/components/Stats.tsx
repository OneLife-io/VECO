const stats = [
  { v: '11,000+', l: 'Customers worldwide' },
  { v: '4,500+', l: 'Live data products shared' },
  { v: '40+', l: 'Cloud regions available' },
  { v: '99.99%', l: 'Uptime SLA' },
]

export default function Stats() {
  return (
    <section className="border-y border-white/5 bg-ink-900/60 py-14">
      <div className="container-page">
        <div className="grid gap-8 text-center sm:grid-cols-2 lg:grid-cols-4">
          {stats.map((s) => (
            <div key={s.l}>
              <div className="bg-gradient-to-b from-white to-brand-300 bg-clip-text text-4xl font-extrabold tracking-tight text-transparent sm:text-5xl">
                {s.v}
              </div>
              <div className="mt-2 text-sm text-white/60">{s.l}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
