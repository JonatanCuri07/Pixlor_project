<script setup lang="ts">
defineProps<{ provider: 'google' | 'facebook' | 'apple' }>()
const names = { google: 'Google', facebook: 'Facebook', apple: 'Apple' }
</script>

<template>
  <button type="button" class="social-button flex w-full items-center justify-center gap-3">
    <AppIcon :name="provider" class="shrink-0" />
    <span>Continuar con {{ names[provider] }}</span>
  </button>
</template>
