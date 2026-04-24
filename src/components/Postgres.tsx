export default function Postgres() {
  return (
    <section id="pricing" className="section relative overflow-hidden border-t border-white/5">
      <div className="pointer-events-none absolute inset-0 -z-10 bg-gradient-to-b from-ink-900/30 via-transparent to-transparent" />
      <div className="container-page">
        <div className="relative overflow-hidden rounded-3xl border border-white/10 bg-gradient-to-br from-[#0f1b2d] via-[#0b1020] to-[#0a0a0f] p-10 lg:p-16">
          <div
            aria-hidden="true"
            className="pointer-events-none absolute -right-24 -top-24 h-80 w-80 rounded-full bg-brand-500/30 blur-3xl"
          />
          <div
            aria-hidden="true"
            className="pointer-events-none absolute -left-16 bottom-0 h-72 w-72 rounded-full bg-fuchsia-500/20 blur-3xl"
          />

          <div className="grid items-center gap-10 lg:grid-cols-5">
            <div className="lg:col-span-3">
              <p className="eyebrow">VECO Postgres</p>
              <h2 className="mt-3 text-balance text-3xl font-bold tracking-tight sm:text-5xl">
                The world's most popular database, on the AI Data Cloud.
              </h2>
              <p className="mt-5 max-w-xl text-white/75">
                Run transactional workloads alongside analytics and AI — fully
                managed Postgres with elastic compute, zero-downtime upgrades,
                and governed access to your operational data.
              </p>
              <div className="mt-7 flex flex-col gap-3 sm:flex-row">
                <a href="#" className="btn-primary">Read the announcement</a>
                <a href="#" className="btn-secondary">Try VECO Postgres</a>
              </div>

              <div className="mt-8 grid grid-cols-3 gap-4 text-sm">
                {[
                  { k: 'ACID', v: 'Full Postgres compatibility' },
                  { k: 'HA', v: 'Multi-AZ with failover' },
                  { k: 'Scale', v: 'Elastic read & write' },
                ].map((x) => (
                  <div key={x.k} className="rounded-xl border border-white/10 bg-white/5 p-4">
                    <div className="text-xs font-semibold uppercase tracking-widest text-brand-300">
                      {x.k}
                    </div>
                    <div className="mt-1 text-white/90">{x.v}</div>
                  </div>
                ))}
              </div>
            </div>

            <div className="relative lg:col-span-2">
              <div className="rounded-2xl border border-white/10 bg-ink-900 p-5 shadow-xl">
                <div className="flex items-center justify-between border-b border-white/10 pb-2 text-xs text-white/50">
                  <span>psql — veco.postgres</span>
                  <span className="text-emerald-300">● connected</span>
                </div>
                <pre className="mt-3 overflow-x-auto text-sm leading-6 text-white/85">
                  <code>
{`veco=> SELECT plan_tier, COUNT(*)
veco->   FROM subscriptions
veco->  WHERE status = 'active'
veco->  GROUP BY 1;

 plan_tier | count
-----------+-------
 starter   |  12380
 growth    |   4920
 scale     |    812
 enterprise|    144
(4 rows)

Time: 42 ms`}
                  </code>
                </pre>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
