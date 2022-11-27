/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./ECOmmerce/templates/**/*.html'],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
  ],
}
