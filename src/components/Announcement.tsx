export default function Announcement() {
  return (
    <div className="bg-gradient-to-r from-brand-700 via-brand-500 to-brand-700 text-white">
      <div className="container-page flex flex-col items-center justify-between gap-2 py-2.5 text-center text-xs font-medium sm:flex-row sm:text-sm">
        <p className="opacity-95">
          <span className="mr-2 inline-flex items-center rounded-full bg-white/20 px-2 py-0.5 text-[10px] font-bold uppercase tracking-widest">
            New
          </span>
          VECO World Tour — hands-on with agentic AI on your governed data
        </p>
        <a
          href="#"
          className="inline-flex items-center gap-1 font-semibold underline-offset-4 hover:underline"
        >
          Register now
          <svg
            className="h-3.5 w-3.5"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
          >
            <path
              fillRule="evenodd"
              d="M7.21 14.77a.75.75 0 01.02-1.06L11.168 10 7.23 6.29a.75.75 0 111.04-1.08l4.5 4.25a.75.75 0 010 1.08l-4.5 4.25a.75.75 0 01-1.06-.02z"
              clipRule="evenodd"
            />
          </svg>
        </a>
      </div>
    </div>
  )
}
