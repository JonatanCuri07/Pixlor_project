<script setup lang="ts">
withDefaults(defineProps<{ to?: string; color?: 'purple' | 'orange' | 'red' | 'green'; icon?: string; arrow?: boolean }>(), { color: 'purple', arrow: false })
</script>

<template>
  <NuxtLink v-if="to" :to="to" :class="['magic-button', `button-${color}`]">
    <AppIcon v-if="icon" :name="icon" class="button-icon shrink-0" />
    <span class="min-w-0 flex-1"><slot /></span>
    <AppIcon v-if="arrow" name="arrow" class="shrink-0" />
  </NuxtLink>
  <button v-else type="button" :class="['magic-button', `button-${color}`]">
    <AppIcon v-if="icon" :name="icon" class="button-icon shrink-0" />
    <span class="min-w-0 flex-1"><slot /></span>
    <AppIcon v-if="arrow" name="arrow" class="shrink-0" />
  </button>
</template>
