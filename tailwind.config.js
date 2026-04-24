/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        ink: {
          950: '#0A0A0F',
          900: '#11121A',
          800: '#1B1D29',
        },
        brand: {
          50: '#EAF7FF',
          100: '#CFEEFF',
          200: '#9DDCFF',
          300: '#63C7FF',
          400: '#29B5E8',
          500: '#11A3DC',
          600: '#0086B8',
          700: '#00678F',
          800: '#0A4A66',
          900: '#0C3A50',
        },
      },
      fontFamily: {
        sans: [
          'Inter',
          'ui-sans-serif',
          'system-ui',
          '-apple-system',
          'Segoe UI',
          'Roboto',
          'Helvetica Neue',
          'Arial',
          'sans-serif',
        ],
      },
      boxShadow: {
        glow: '0 0 80px -10px rgba(41, 181, 232, 0.45)',
      },
    },
  },
  plugins: [],
}
