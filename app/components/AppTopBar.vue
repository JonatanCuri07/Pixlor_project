<script setup lang="ts">
withDefaults(defineProps<{ menu?: boolean }>(), { menu: false })
</script>

<template>
  <header class="top-bar grid grid-cols-[auto_1fr_auto] items-start gap-2">
    <NuxtLink to="/menu" class="nav-circle grid place-items-center" :aria-label="menu ? 'Abrir menú principal' : 'Volver al menú'">
      <AppIcon :name="menu ? 'menu' : 'back'" />
    </NuxtLink>
    <PixlorLogo />
    <CoinCounter />
  </header>
</template>
