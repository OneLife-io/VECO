import { useEffect, useState } from 'react'
import Logo from './Logo'

const navItems = [
  { label: 'Platform', href: '#platform' },
  { label: 'Solutions', href: '#solutions' },
  { label: 'Pricing', href: '#pricing' },
  { label: 'Developers', href: '#developers' },
  { label: 'Resources', href: '#resources' },
  { label: 'Company', href: '#company' },
]

export default function Navbar() {
  const [scrolled, setScrolled] = useState(false)
  const [open, setOpen] = useState(false)

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 8)
    onScroll()
    window.addEventListener('scroll', onScroll, { passive: true })
    return () => window.removeEventListener('scroll', onScroll)
  }, [])

  return (
    <header
      className={`sticky top-0 z-40 transition ${
        scrolled
          ? 'border-b border-white/10 bg-ink-950/80 backdrop-blur-md'
          : 'bg-transparent'
      }`}
    >
      <div className="container-page flex h-16 items-center justify-between">
        <a href="#" aria-label="VECO home" className="flex items-center">
          <Logo />
        </a>

        <nav className="hidden items-center gap-7 lg:flex">
          {navItems.map((item) => (
            <a
              key={item.label}
              href={item.href}
              className="group relative text-sm font-medium text-white/80 transition hover:text-white"
            >
              {item.label}
              <span className="absolute -bottom-1 left-0 h-0.5 w-0 bg-brand-400 transition-all group-hover:w-full" />
            </a>
          ))}
        </nav>

        <div className="hidden items-center gap-3 lg:flex">
          <a
            href="#"
            className="text-sm font-medium text-white/80 transition hover:text-white"
          >
            Sign in
          </a>
          <a href="#start" className="btn-primary">
            Start for free
          </a>
        </div>

        <button
          type="button"
          className="inline-flex h-10 w-10 items-center justify-center rounded-md text-white/90 lg:hidden"
          aria-label="Toggle menu"
          onClick={() => setOpen((v) => !v)}
        >
          <svg
            className="h-6 w-6"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            {open ? (
              <path d="M6 6l12 12M6 18L18 6" />
            ) : (
              <path d="M4 6h16M4 12h16M4 18h16" />
            )}
          </svg>
        </button>
      </div>

      {open && (
        <div className="lg:hidden">
          <div className="container-page flex flex-col gap-2 border-t border-white/10 bg-ink-950/95 py-4 backdrop-blur">
            {navItems.map((item) => (
              <a
                key={item.label}
                href={item.href}
                className="rounded-md px-2 py-2 text-sm font-medium text-white/80 hover:bg-white/5 hover:text-white"
                onClick={() => setOpen(false)}
              >
                {item.label}
              </a>
            ))}
            <div className="mt-2 flex items-center gap-3 px-2">
              <a href="#" className="btn-secondary flex-1">
                Sign in
              </a>
              <a href="#start" className="btn-primary flex-1">
                Start for free
              </a>
            </div>
          </div>
        </div>
      )}
    </header>
  )
}
