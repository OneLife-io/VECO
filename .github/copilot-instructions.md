# Copilot Instructions for VECO

## Project Overview
VECO is a React + TypeScript marketing/landing page application built with Vite and styled with Tailwind CSS.

## Tech Stack
- **Framework**: React 18 with TypeScript (strict mode)
- **Build tool**: Vite
- **Styling**: Tailwind CSS with custom `ink` and `brand` color palettes
- **Module system**: ESM (`"type": "module"`)
- **JSX transform**: `react-jsx` (no need to import React in every file)

## Code Conventions
- All component files use `.tsx` extension and live under `src/components/`
- Components are written as named `export default function` declarations
- TypeScript is configured with `strict: true`, `noUnusedLocals: true`, and `noUnusedParameters: true` — avoid introducing unused variables or parameters
- Config files (e.g., `vite.config.ts`, `tailwind.config.js`, `postcss.config.js`) use `export default` (ESM)
- Use Tailwind utility classes for all styling; do not add inline styles or external CSS unless necessary

## Review Guidance
- Flag any TypeScript type-safety issues, `any` types, or unsafe casts
- Ensure all React components are properly typed (props interfaces/types)
- Check for unused imports, variables, or parameters (TypeScript compiler will catch these)
- Verify Tailwind classes reference the custom theme tokens where appropriate (`ink-*`, `brand-*`)
- Confirm new components are registered in `src/App.tsx` if they are page-level sections
- Look for accessibility issues (semantic HTML, `alt` attributes, ARIA labels)
