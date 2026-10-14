import tailwindcss from '@tailwindcss/vite'

export default defineNuxtConfig({
  compatibilityDate: '2026-10-06',

  css: ['~/assets/css/main.css'],

  runtimeConfig: {
    public: {
      supabaseUrl: '',
      supabasePublishableKey: '',
    },
  },

  vite: {
    plugins: [
      tailwindcss(),
    ],
  },
})