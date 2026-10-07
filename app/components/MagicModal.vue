<script setup lang="ts">
defineProps<{ titleId: string }>()
const dialog = ref<HTMLDialogElement>()
onMounted(() => dialog.value?.showModal())
const close = () => navigateTo('/store')
</script>

<template>
  <dialog ref="dialog" class="magic-dialog" :aria-labelledby="titleId" @cancel.prevent="close">
    <MagicPanel class="modal-panel">
      <span class="modal-star grid place-items-center" aria-hidden="true"><AppIcon name="star" /></span>
      <slot />
    </MagicPanel>
  </dialog>
</template>
