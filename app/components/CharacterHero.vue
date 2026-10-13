<script setup lang="ts">
withDefaults(defineProps<{ variant?: 'auth' | 'menu' | 'upload' | 'store' | 'confirm' | 'success' }>(), { variant: 'auth' })
</script>

<template>
  <picture class="character-hero relative mx-auto block h-auto w-full object-contain">
    <source media="(min-width: 1024px)" :srcset="`/images/official/desktop/characters/${variant === 'upload' ? 'upload' : variant === 'auth' || variant === 'menu' ? 'auth' : 'store'}.webp`" />
    <img :src="`/images/official/characters/${variant}.webp`" :alt="variant === 'upload' ? 'Los exploradores de Pixlor' : 'Los exploradores de Pixlor: una conejita, un tigre y un panda'" class="block h-auto w-full object-contain" />
  </picture>
</template>
