<script setup lang="ts">
defineProps<{ open: boolean; title: string; titleId: string }>()
const emit = defineEmits<{ close: [] }>()
</script>

<template>
  <BrowserModal :open="open" :title-id="titleId" class="local-dialog" @close="emit('close')">
    <MagicPanel class="local-modal-panel">
      <header class="mb-4 flex items-start justify-between gap-3">
        <h2 :id="titleId" class="text-xl font-black sm:text-2xl">{{ title }}</h2>
        <button type="button" class="close-control shrink-0" aria-label="Cerrar modal" @click="emit('close')">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true" class="h-5 w-5"><path d="m6 6 12 12M6 18 18 6" /></svg>
        </button>
      </header>
      <slot />
    </MagicPanel>
  </BrowserModal>
</template>
