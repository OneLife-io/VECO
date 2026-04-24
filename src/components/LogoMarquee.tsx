const logos = [
  'NORTHWIND',
  'ACME CORP',
  'PIXELMILL',
  'FINHUB',
  'BIOGENIX',
  'ASTRA RETAIL',
  'LUMENWORKS',
  'HELIOS',
  'ORBIT MEDIA',
  'NOVAWARE',
]

export default function LogoMarquee() {
  return (
    <section className="border-y border-white/5 bg-ink-900/60 py-10">
      <div className="container-page">
        <p className="text-center text-xs font-semibold uppercase tracking-[0.22em] text-white/50">
          Trusted by 11,000+ teams — from startups to the Fortune 500
        </p>
        <div className="marquee mt-6 overflow-hidden">
          <div className="marquee-track flex w-[200%] items-center gap-14 whitespace-nowrap">
            {[...logos, ...logos].map((l, i) => (
              <span
                key={i}
                className="text-lg font-bold tracking-[0.25em] text-white/40 transition hover:text-white/80"
              >
                {l}
              </span>
            ))}
          </div>
        </div>
      </div>
    </section>
  )
}
