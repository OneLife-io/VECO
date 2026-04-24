import { useState } from 'react'

type Tab = {
  id: string
  label: string
  title: string
  body: string
  bullets: string[]
  metric: { l: string; v: string }[]
}

const tabs: Tab[] = [
  {
    id: 'ingest',
    label: 'Ingest',
    title: 'Bring every byte in — streaming or batch',
    body:
      'Open connectors, zero-copy shares, and native support for structured, semi-structured and unstructured data keep your pipelines simple and reliable.',
    bullets: [
      'Streaming ingest with Snowpipe & Kafka',
      'Dynamic tables & declarative pipelines',
      'Iceberg-native, open table formats',
    ],
    metric: [
      { l: 'connectors', v: '250+' },
      { l: 'p95 latency', v: '< 1s' },
      { l: 'uptime', v: '99.99%' },
    ],
  },
  {
    id: 'analyze',
    label: 'Analyze',
    title: 'Analytics with optimal price-performance',
    body:
      'Run sub-second BI on petabyte data, mix SQL and Python, and keep costs predictable — all on a platform built to separate storage and compute.',
    bullets: [
      'Per-workload elastic compute',
      'Native BI with semantic layer',
      'Time travel & zero-copy cloning',
    ],
    metric: [
      { l: 'query speedup', v: '3–10×' },
      { l: 'clusters', v: 'auto' },
      { l: 'concurrency', v: '∞' },
    ],
  },
  {
    id: 'model',
    label: 'Model',
    title: 'ML & AI where your data already lives',
    body:
      'Train, register, and serve models without moving data. Feature stores, notebooks and MLOps are part of the platform.',
    bullets: [
      'Snowpark ML & Container Services',
      'Feature Store + Model Registry',
      'GPU-powered training & serving',
    ],
    metric: [
      { l: 'GPUs', v: 'A100/H100' },
      { l: 'models', v: 'train & host' },
      { l: 'governance', v: 'end-to-end' },
    ],
  },
  {
    id: 'share',
    label: 'Share',
    title: 'Live data sharing — across clouds & orgs',
    body:
      'No ETL, no file copies. Share live data, apps, and AI with partners or across business units with fine-grained governance.',
    bullets: [
      'Cross-region & cross-cloud shares',
      'Private data exchanges',
      'Usage metering & monetization',
    ],
    metric: [
      { l: 'data products', v: '4,500+' },
      { l: 'providers', v: '1,200+' },
      { l: 'copies', v: 'zero' },
    ],
  },
  {
    id: 'build',
    label: 'Build apps',
    title: 'Ship data & AI apps to any cloud',
    body:
      'Develop, distribute and monetize full-stack apps on a platform that handles auth, billing, compute and data — so your team ships faster.',
    bullets: [
      'Streamlit in VECO',
      'Native Apps with billing & listings',
      'Open SDKs: Python, JS, Java, Scala',
    ],
    metric: [
      { l: 'time to launch', v: 'days' },
      { l: 'regions', v: '40+' },
      { l: 'install', v: '1-click' },
    ],
  },
]

export default function Workloads() {
  const [active, setActive] = useState(tabs[0].id)
  const current = tabs.find((t) => t.id === active) ?? tabs[0]

  return (
    <section id="developers" className="section">
      <div className="container-page">
        <div className="mx-auto max-w-3xl text-center">
          <p className="eyebrow">Workloads</p>
          <h2 className="mt-3 text-balance text-3xl font-bold tracking-tight sm:text-5xl">
            From ingestion to insight to intelligent apps
          </h2>
          <p className="mt-5 text-white/70">
            Every workload, one platform. Ingest, analyze, model, share, and
            build — with shared governance and a single copy of your data.
          </p>
        </div>

        <div className="mt-12 flex flex-wrap items-center justify-center gap-2">
          {tabs.map((t) => (
            <button
              key={t.id}
              onClick={() => setActive(t.id)}
              className={`rounded-full border px-5 py-2 text-sm font-semibold transition ${
                active === t.id
                  ? 'border-brand-400 bg-brand-400 text-ink-950'
                  : 'border-white/10 bg-white/5 text-white/80 hover:border-white/30 hover:text-white'
              }`}
            >
              {t.label}
            </button>
          ))}
        </div>

        <div className="mt-10 grid items-center gap-10 rounded-3xl border border-white/10 bg-gradient-to-b from-white/[0.04] to-white/[0.01] p-8 lg:grid-cols-2 lg:p-12">
          <div>
            <h3 className="text-2xl font-semibold text-white sm:text-3xl">
              {current.title}
            </h3>
            <p className="mt-4 text-white/70">{current.body}</p>
            <ul className="mt-6 space-y-2.5">
              {current.bullets.map((b) => (
                <li key={b} className="flex items-start gap-2 text-sm text-white/85">
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
                  {b}
                </li>
              ))}
            </ul>
            <a href="#" className="btn-ghost mt-6">Read the docs →</a>
          </div>

          <div className="relative">
            <div className="absolute -inset-6 -z-10 rounded-[28px] bg-gradient-to-br from-brand-500/20 to-fuchsia-500/10 blur-2xl" />
            <div className="rounded-2xl border border-white/10 bg-ink-900 p-6">
              <div className="flex items-center justify-between">
                <div className="text-xs font-semibold uppercase tracking-widest text-white/50">
                  {current.label} · live snapshot
                </div>
                <span className="text-[10px] text-emerald-300">● healthy</span>
              </div>
              <div className="mt-5 grid grid-cols-3 gap-3">
                {current.metric.map((m) => (
                  <div
                    key={m.l}
                    className="rounded-xl border border-white/10 bg-black/20 p-4"
                  >
                    <div className="text-[11px] uppercase tracking-widest text-white/50">
                      {m.l}
                    </div>
                    <div className="mt-1 text-xl font-bold text-white">{m.v}</div>
                  </div>
                ))}
              </div>
              <MiniChart />
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}

function MiniChart() {
  const bars = [28, 42, 35, 55, 48, 70, 64, 82, 76, 90, 84, 96]
  return (
    <div className="mt-6">
      <div className="flex items-end gap-1.5">
        {bars.map((h, i) => (
          <div
            key={i}
            className="flex-1 rounded-t bg-gradient-to-t from-brand-700 to-brand-300"
            style={{ height: `${h}px` }}
          />
        ))}
      </div>
      <div className="mt-2 flex items-center justify-between text-[10px] uppercase tracking-widest text-white/40">
        <span>last 12 hrs</span>
        <span>throughput / minute</span>
      </div>
    </div>
  )
}
