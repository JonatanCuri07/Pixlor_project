<script setup lang="ts">
withDefaults(defineProps<{ to?: string; label?: string }>(), { to: '/', label: 'Volver al inicio de sesión' })
</script>

<template>
  <NuxtLink :to="to" class="back-button artwork-control block" :aria-label="label">
    <img src="/images/official/navigation/back.webp" alt="" aria-hidden="true" width="103" height="102" class="block h-auto w-full object-contain" />
  </NuxtLink>
</template>
