<script setup lang="ts">
const props = defineProps<{ open: boolean; titleId: string }>()
const emit = defineEmits<{ close: [] }>()
const dialog = ref<HTMLDialogElement>()
let restoreScroll: (() => void) | undefined
let previousFocus: HTMLElement | null = null

const release = () => {
  if (dialog.value?.open) dialog.value.close()
  restoreScroll?.()
  restoreScroll = undefined
  if (previousFocus?.isConnected) previousFocus.focus({ preventScroll: true })
  previousFocus = null
}

const syncOpen = () => {
  if (!dialog.value) return
  if (!props.open) {
    release()
    return
  }
  if (dialog.value.open) return
  previousFocus = document.activeElement instanceof HTMLElement ? document.activeElement : null
  const rootOverflow = document.documentElement.style.overflow
  const bodyOverflow = document.body.style.overflow
  restoreScroll = () => {
    document.documentElement.style.overflow = rootOverflow
    document.body.style.overflow = bodyOverflow
  }
  dialog.value.showModal()
  document.documentElement.style.overflow = 'hidden'
  document.body.style.overflow = 'hidden'
}

watch(() => props.open, syncOpen, { flush: 'post' })
watch(() => props.titleId, () => {
  if (props.open && dialog.value?.open) dialog.value.querySelector<HTMLElement>('[autofocus], button:not([disabled]), input:not([disabled]), a[href]')?.focus({ preventScroll: true })
}, { flush: 'post' })
onMounted(syncOpen)
onBeforeUnmount(release)
</script>

<template>
  <dialog ref="dialog" class="browser-dialog" aria-modal="true" :aria-labelledby="titleId" @cancel.prevent="emit('close')">
    <slot />
  </dialog>
</template>
