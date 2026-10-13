<script setup lang="ts">
defineProps<{ provider: 'google' | 'facebook' }>()
const names = { google: 'Google', facebook: 'Facebook' }
</script>

<template>
  <ArtworkButton :asset="`auth/${provider}`" :label="`Continuar con ${names[provider]}`" />
</template>
