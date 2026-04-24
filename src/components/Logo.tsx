export default function Logo({ className = 'h-7 w-auto' }: { className?: string }) {
  return (
    <div className={`flex items-center gap-2 ${className}`}>
      <svg viewBox="0 0 64 64" className="h-7 w-7" aria-hidden="true">
        <defs>
          <linearGradient id="logo-g" x1="0" x2="1" y1="0" y2="1">
            <stop offset="0" stopColor="#29B5E8" />
            <stop offset="1" stopColor="#0086B8" />
          </linearGradient>
        </defs>
        <rect width="64" height="64" rx="14" fill="url(#logo-g)" />
        <g stroke="#fff" strokeWidth="3" strokeLinecap="round">
          <path d="M32 10v44M13 21l38 22M13 43l38-22" />
        </g>
        <g fill="#fff">
          <circle cx="32" cy="10" r="3" />
          <circle cx="32" cy="54" r="3" />
          <circle cx="13" cy="21" r="3" />
          <circle cx="51" cy="43" r="3" />
          <circle cx="13" cy="43" r="3" />
          <circle cx="51" cy="21" r="3" />
        </g>
      </svg>
      <span className="text-lg font-bold tracking-tight text-white">VECO</span>
    </div>
  )
}
