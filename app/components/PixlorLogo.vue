<script setup lang="ts">
withDefaults(defineProps<{ variant?: 'main' | 'upload' | 'store' | 'confirm' | 'success' }>(), { variant: 'main' })
</script>

<template>
  <picture class="pixlor-logo mx-auto block h-auto object-contain">
    <source media="(min-width: 1024px)" :srcset="`/images/official/desktop/branding/${variant === 'main' ? 'main' : variant === 'upload' ? 'upload' : 'store'}.webp`" />
    <img :src="`/images/official/branding/${variant}.webp`" alt="Pixlor" class="block h-auto w-full object-contain" />
  </picture>
</template>
