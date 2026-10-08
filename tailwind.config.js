/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        'toeic-primary': '#0d2d4e',
        'toeic-accent': '#f2a900',
        // Gradient palette
        'indigo-start': '#4f46e5',
        'indigo-end': '#7c3aed',
        'purple-start': '#6d28d9',
        'purple-end': '#a855f7',
        'amber-start': '#f59e0b',
        'amber-end': '#fbbf24',
        'emerald-start': '#10b981',
        'emerald-end': '#34d399',
        'rose-start': '#ef4444',
        'rose-end': '#f87171',
      },
      animation: {
        'fadeIn': 'fadeIn 0.3s ease-out',
        fadeIn: 'fadeIn 0.3s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: 0, transform: 'translateY(10px)' },
          '100%': { opacity: 1, transform: 'translateY(0)' },
        },
      },
      backdropBlur: {
        xs: '2px',
      },
    },
  },
  plugins: [],
};