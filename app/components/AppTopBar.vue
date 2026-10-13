<script setup lang="ts">
withDefaults(defineProps<{ variant?: 'upload' | 'store' | 'confirm' | 'success' }>(), { variant: 'store' })
</script>

<template>
  <header class="top-bar grid grid-cols-[auto_minmax(0,1fr)_auto] items-start gap-2">
    <NavigationMenuButton />
    <PixlorLogo :variant="variant" />
    <CoinCounter :variant="variant === 'upload' ? 'upload' : 'store'" />
  </header>
</template>
