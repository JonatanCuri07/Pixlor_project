<script setup lang="ts">
withDefaults(defineProps<{ variant?: 'upload' | 'store' }>(), { variant: 'store' })
</script>

<template>
  <span class="coin-counter block shrink-0" aria-label="250 Pixlor Coins">
    <img :src="`/images/official/${variant}/counter.webp`" alt="" aria-hidden="true" class="block h-auto w-full object-contain" />
  </span>
</template>
