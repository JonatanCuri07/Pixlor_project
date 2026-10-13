<script setup lang="ts">
defineProps<{ open: boolean; titleId: string; variant: 'confirm' | 'success' }>()
const emit = defineEmits<{ close: [] }>()
</script>

<template>
  <BrowserModal :open="open" :title-id="titleId" class="magic-dialog" @close="emit('close')">
    <NavigationMenuButton class="modal-navigation" />
    <div :class="['modal-panel', `modal-${variant}`]">
      <div class="modal-artwork relative">
        <picture class="modal-panel-image block"><source media="(min-width: 1024px)" :srcset="`/images/official/desktop/${variant}/panel.webp`" /><img :src="`/images/official/${variant}/panel.webp`" alt="" aria-hidden="true" class="block h-auto w-full object-contain" /></picture>
        <slot name="artwork" />
      </div>
      <slot />
    </div>
  </BrowserModal>
</template>
