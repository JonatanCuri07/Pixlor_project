<script setup lang="ts">
const route = useRoute()
const background = computed(() => {
  if (route.path.startsWith('/store')) return 'store'
  if (route.path === '/upload') return 'upload'
  if (route.path === '/menu' || route.path === '/profile') return 'menu'
  return 'auth'
})
</script>

<template>
  <div :class="['app-background min-h-dvh', `background-${background}`]">
    <a href="#main-content" class="skip-link">Saltar al contenido</a>
    <main id="main-content" class="app-shell mx-auto w-full">
      <slot />
    </main>
  </div>
</template>
