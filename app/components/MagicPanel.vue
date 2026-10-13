<script setup lang="ts">
withDefaults(defineProps<{ variant?: 'auth' | 'menu' }>(), { variant: 'auth' })
</script>

<template>
  <section :class="['magic-panel relative', `panel-${variant}`]">
    <slot />
  </section>
</template>
