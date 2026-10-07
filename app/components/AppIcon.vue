<script setup lang="ts">
withDefaults(defineProps<{ name: string }>(), { name: 'star' })
const paths: Record<string, string> = {
  arrow: 'M5 12h14m-6-6 6 6-6 6',
  back: 'M19 12H5m6-6-6 6 6 6',
  chevron: 'm9 5 7 7-7 7',
  menu: 'M4 6h16M4 12h16M4 18h16',
  user: 'M16 7a4 4 0 1 1-8 0 4 4 0 0 1 8 0ZM4 21v-2a8 8 0 0 1 16 0v2Z',
  mail: 'M3 5h18v14H3Zm0 0 9 8 9-8',
  lock: 'M5 10h14v11H5Zm3 0V6a4 4 0 0 1 8 0v4m-4 5v2',
  eye: 'M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12Zm13 0a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z',
  eyeOff: 'm3 3 18 18M10 5h2c6 0 10 7 10 7a20 20 0 0 1-4 5M6 6a20 20 0 0 0-4 6s4 7 10 7a12 12 0 0 0 5-1m-8-9a4 4 0 0 0 5 5',
  cart: 'M2 3h3l3 13h11l3-10H6M10 21a1 1 0 1 1-2 0 1 1 0 0 1 2 0Zm10 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z',
  logout: 'M10 3H4v18h6m3-9h9m-4-4 4 4-4 4M10 7v10',
  camera: 'M3 7h4l2-3h6l2 3h4v14H3Zm14 7a5 5 0 1 1-10 0 5 5 0 0 1 10 0Z',
  gallery: 'M3 3h18v18H3Zm0 14 6-6 5 5 3-3 4 4M9 7h.01',
  link: 'm10 13 4-4m-6 6-2 2a4 4 0 0 1-6-6l5-5a4 4 0 0 1 6 0m2 3 2-2a4 4 0 0 1 6 6l-5 5a4 4 0 0 1-6 0',
  upload: 'M7 18H5a4 4 0 0 1-1-8 8 8 0 0 1 16-1 5 5 0 0 1-1 9h-2M12 22V11m-4 4 4-4 4 4',
  star: 'm12 2 3 6 7 1-5 5 1 7-6-3-6 3 1-7-5-5 7-1Z',
}
</script>

<template>
  <svg v-if="name === 'google'" viewBox="0 0 24 24" aria-hidden="true" class="app-icon">
    <path fill="#4285F4" d="M21.6 12.2c0-.7-.1-1.4-.2-2.2H12v4.2h5.4a4.6 4.6 0 0 1-2 3v2.5h3.3c2-1.8 2.9-4.4 2.9-7.5Z" />
    <path fill="#34A853" d="M12 22c2.7 0 5-.9 6.7-2.3l-3.3-2.5c-.9.6-2 .9-3.4.9-2.6 0-4.8-1.7-5.6-4H3v2.6A10 10 0 0 0 12 22Z" />
    <path fill="#FBBC05" d="M6.4 14.1a6 6 0 0 1 0-4.2V7.3H3a10 10 0 0 0 0 9.4Z" />
    <path fill="#EA4335" d="M12 5.9c1.5 0 2.8.5 3.9 1.5l2.9-2.9A9.7 9.7 0 0 0 12 2a10 10 0 0 0-9 5.3l3.4 2.6c.8-2.3 3-4 5.6-4Z" />
  </svg>
  <svg v-else-if="name === 'facebook'" viewBox="0 0 24 24" aria-hidden="true" class="app-icon">
    <circle cx="12" cy="12" r="12" fill="#087cff" />
    <path fill="white" d="M13.8 24v-9.3h3.1l.5-3.6h-3.6V8.8c0-1 .3-1.8 1.8-1.8h1.9V3.8c-.4 0-1.5-.2-2.8-.2-2.7 0-4.6 1.7-4.6 4.7v2.8H7v3.6h3.1V24Z" />
  </svg>
  <svg v-else-if="name === 'apple'" viewBox="0 0 24 24" aria-hidden="true" class="app-icon" fill="currentColor">
    <path d="M17.1 12.7c0-2.2 1.8-3.3 1.9-3.4-1.1-1.6-2.9-1.9-3.5-1.9-1.5-.2-2.9.9-3.7.9-.7 0-1.9-.9-3.1-.9-1.6 0-3.1.9-3.9 2.3-1.7 2.9-.4 7.2 1.2 9.6.8 1.1 1.7 2.4 2.9 2.3 1.2 0 1.7-.7 3.1-.7s1.9.7 3.1.7c1.3 0 2.1-1.1 2.9-2.3.9-1.3 1.3-2.6 1.3-2.7-.1 0-2.2-.9-2.2-3.9ZM14.7 5.9c.7-.9 1.2-2.1 1.1-3.3-1 .1-2.3.7-3 1.6-.7.7-1.3 2-1.2 3.1 1.2.1 2.4-.6 3.1-1.4Z" />
  </svg>
  <svg v-else-if="name === 'whatsapp'" viewBox="0 0 24 24" aria-hidden="true" class="app-icon" fill="none" stroke="currentColor" stroke-width="1.7">
    <path d="M21 11.5a9 9 0 0 1-13.5 8L2 21l1.5-5.3A9 9 0 1 1 21 11.5Z" />
    <path fill="currentColor" stroke="none" d="M7.3 6.9c.3-.3.6-.3.9-.3h.6c.2 0 .3.1.4.4l.8 1.9c.1.2 0 .4-.1.6l-.7.8c-.2.2-.1.4 0 .6.5.9 1.4 1.9 2.8 2.5.3.1.4.1.6-.1l.9-1.1c.2-.2.4-.2.6-.1l2 .9c.3.1.4.2.4.4 0 .3-.2 1.4-.8 1.8-.6.5-1.4.6-2.2.4-1-.2-2.5-.7-4.1-2.1-1.7-1.5-2.9-3.4-3-4.5-.2-1 .2-1.7.9-2.1Z" />
  </svg>
  <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="app-icon">
    <path :d="paths[name] || paths.star" />
  </svg>
</template>
