import tailwindcss from '@tailwindcss/vite'

export default defineNuxtConfig({
  debug: false,
  app: {
    head: {
      htmlAttrs: { lang: 'es' },
      title: 'Pixlor · Tu aventura empieza aquí',
      meta: [{ name: 'description', content: 'Explora el mundo de Pixlor, comparte tus creaciones y descubre recompensas.' }],
    },
  },
  css: ['~/assets/css/main.css'],
  compatibilityDate: '2026-10-06',
  vite: {
    plugins: [
      tailwindcss(),
    ],
  },
})
