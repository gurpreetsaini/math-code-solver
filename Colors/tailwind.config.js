
module.exports = {
  content: ["./*.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        'math-primary': '#4D6CFA',
        'math-secondary': '#FF7A45',
        'math-accent': '#6DD400',
        'math-light': '#F5F9FF',
        'math-dark': '#2D3748',
        'math-pink': '#FF6B8B',
        'math-purple': '#9D6CFF',
        'math-yellow': '#FFD166'
      },
      fontFamily: {
        sans: ['Quicksand', 'sans-serif'],
        comic: ['"Comic Neue"', 'cursive']
      }
    }
  },
  plugins: [],
}
