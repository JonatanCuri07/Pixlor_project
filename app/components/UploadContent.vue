<script setup lang="ts">
type SelectedContent = { source: 'file' | 'camera'; file: File; previewUrl: string } | { source: 'link'; url: string }
const selectedContent = shallowRef<SelectedContent | null>(null)
const filePicker = ref<HTMLInputElement>()
const isCameraOpen = ref(false)
const isLinkModalOpen = ref(false)
const isMediaOpen = ref(false)
const lightboxVideo = ref<HTMLVideoElement>()
const linkDraft = ref('')
const linkError = ref('')
const feedback = ref('')
const errorMessage = ref('')
const dragDepth = ref(0)
const isDragging = computed(() => dragDepth.value > 0)
const canSubmit = computed(() => selectedContent.value !== null)

const closeMedia = () => {
  lightboxVideo.value?.pause()
  isMediaOpen.value = false
}

const openMedia = () => {
  if (selectedContent.value && selectedContent.value.source !== 'link') isMediaOpen.value = true
}

const releaseContent = () => {
  closeMedia()
  if (selectedContent.value && selectedContent.value.source !== 'link') URL.revokeObjectURL(selectedContent.value.previewUrl)
  selectedContent.value = null
}

const removeContent = () => {
  releaseContent()
  feedback.value = ''
  errorMessage.value = ''
}

const selectFile = (file: File, source: 'file' | 'camera' = 'file') => {
  removeContent()
  if (!file.type.startsWith('image/') && !file.type.startsWith('video/')) {
    errorMessage.value = 'Selecciona una imagen o un video. Este tipo de archivo no es compatible.'
    return
  }
  try {
    selectedContent.value = { source, file, previewUrl: URL.createObjectURL(file) }
  } catch {
    errorMessage.value = 'No se pudo preparar este archivo. Intenta seleccionarlo de nuevo.'
  }
}

const openPicker = () => filePicker.value?.click()
const onFileChange = (event: Event) => {
  const input = event.target as HTMLInputElement
  const file = input.files?.[0]
  if (file) selectFile(file)
  input.value = ''
}

const onDragEnter = (event: DragEvent) => {
  if (event.dataTransfer?.types.includes('Files')) dragDepth.value++
}
const onDragOver = (event: DragEvent) => {
  if (event.dataTransfer) event.dataTransfer.dropEffect = 'copy'
}
const onDrop = (event: DragEvent) => {
  dragDepth.value = 0
  const file = event.dataTransfer?.files[0]
  if (file) selectFile(file)
  else {
    removeContent()
    errorMessage.value = 'Arrastra una imagen o un video desde tus archivos.'
  }
}

const openLink = () => {
  linkDraft.value = selectedContent.value?.source === 'link' ? selectedContent.value.url : ''
  linkError.value = ''
  isLinkModalOpen.value = true
}
const addLink = () => {
  try {
    const url = new URL(linkDraft.value.trim())
    if (!['http:', 'https:'].includes(url.protocol)) throw new Error('Invalid protocol')
    removeContent()
    selectedContent.value = { source: 'link', url: url.href }
    isLinkModalOpen.value = false
    linkDraft.value = ''
    linkError.value = ''
  } catch {
    linkError.value = 'Ingresa un enlace válido que empiece con https:// o http://.'
  }
}
const openCamera = () => {
  errorMessage.value = ''
  feedback.value = ''
  isCameraOpen.value = true
}
const prepareContent = () => {
  if (canSubmit.value) feedback.value = 'Tu contenido está listo para enviar.'
}

onBeforeUnmount(releaseContent)
</script>

<template>
  <section class="upload-content" aria-label="Selecciona tu contenido">
    <input ref="filePicker" type="file" accept="image/*,video/*" hidden @change="onFileChange" />
    <div :class="['upload-dropzone relative rounded-3xl', { 'is-dragging': isDragging }]" @dragenter.prevent="onDragEnter" @dragover.prevent="onDragOver" @dragleave.prevent="dragDepth = Math.max(0, dragDepth - 1)" @drop.prevent="onDrop">
      <ArtworkButton v-if="!selectedContent" asset="upload/panel" desktop-asset="upload/panel" label="Arrastra tu foto o video aquí o selecciona un archivo" @click="openPicker" />
      <template v-else>
        <picture class="block"><source media="(min-width: 1024px)" srcset="/images/official/desktop/upload/panel.webp" /><img src="/images/official/upload/panel.webp" alt="" aria-hidden="true" class="block h-auto w-full object-contain" /></picture>
        <div class="upload-preview absolute flex min-h-0 flex-col items-center justify-center gap-1 text-white" aria-label="Contenido seleccionado">
          <button type="button" class="preview-remove close-control absolute" aria-label="Eliminar contenido seleccionado" @click="removeContent">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true" class="h-5 w-5"><path d="m6 6 12 12M6 18 18 6" /></svg>
          </button>
          <template v-if="selectedContent.source !== 'link'">
            <button type="button" class="preview-open relative flex min-h-0 w-full flex-1 items-center justify-center rounded-xl" :aria-label="selectedContent.file.type.startsWith('image/') ? 'Ampliar imagen' : 'Reproducir video'" aria-haspopup="dialog" @click="openMedia">
              <img v-if="selectedContent.file.type.startsWith('image/')" :src="selectedContent.previewUrl" alt="Vista previa del contenido seleccionado" class="preview-thumbnail block h-full w-full rounded-xl object-contain" />
              <template v-else>
                <video :src="selectedContent.previewUrl" muted playsinline preload="metadata" class="preview-thumbnail block h-full w-full rounded-xl object-contain" />
                <span class="preview-play absolute grid place-items-center" aria-hidden="true"><svg viewBox="0 0 24 24" fill="currentColor" class="h-7 w-7"><path d="m8 4 12 8-12 8Z" /></svg></span>
              </template>
            </button>
            <p class="preview-filename w-full truncate text-center font-bold" :title="selectedContent.file.name">{{ selectedContent.file.name }}<span class="sr-only"> · {{ selectedContent.file.type }}</span></p>
          </template>
          <button v-else type="button" class="preview-link-content flex min-h-0 w-full flex-1 flex-col items-center justify-center gap-2 rounded-xl px-4" aria-label="Editar enlace seleccionado" @click="openLink">
            <AppIcon name="link" class="shrink-0" />
            <span class="font-black">Enlace seleccionado</span>
            <span class="line-clamp-2 break-all text-xs">{{ selectedContent.url }}</span>
          </button>
        </div>
      </template>
    </div>
    <p v-if="errorMessage" class="local-notice notice-error mt-3" role="alert">{{ errorMessage }}</p>
    <div class="upload-options relative mx-auto mt-3">
      <picture class="block"><source media="(min-width: 1024px)" srcset="/images/official/desktop/upload/options.webp" /><img src="/images/official/upload/options.webp" alt="" aria-hidden="true" class="block h-auto w-full object-contain" /></picture>
      <div class="upload-option-controls absolute grid grid-cols-3 gap-2">
        <button type="button" class="rounded-xl" aria-label="Cámara" @click="openCamera"><span class="sr-only">Cámara</span></button>
        <button type="button" class="rounded-xl" aria-label="Galería" @click="openPicker"><span class="sr-only">Galería</span></button>
        <button type="button" class="rounded-xl" aria-label="Link" @click="openLink"><span class="sr-only">Link</span></button>
      </div>
    </div>
    <ArtworkButton asset="upload/submit" desktop-asset="upload/submit" label="Subir contenido" :disabled="!canSubmit" class="mt-3" @click="prepareContent" />
    <p v-if="feedback" class="local-notice mt-3" role="status">{{ feedback }}</p>
    <p class="mt-3"><img src="/images/official/upload/note.webp" alt="Tu contenido es revisado por nuestro equipo." class="mx-auto block h-auto w-full object-contain" /></p>
    <CameraCaptureModal :open="isCameraOpen" @close="isCameraOpen = false" @captured="selectFile($event, 'camera')" @error="errorMessage = $event" />
    <BrowserModal :open="isMediaOpen" title-id="media-preview-title" class="media-lightbox" @close="closeMedia">
      <template v-if="isMediaOpen && selectedContent && selectedContent.source !== 'link'">
        <header class="mb-3 flex items-center justify-between gap-3">
          <h2 id="media-preview-title" class="text-lg font-black">{{ selectedContent.file.type.startsWith('image/') ? 'Tu foto' : 'Tu video' }}</h2>
          <button type="button" class="close-control shrink-0" aria-label="Cerrar vista ampliada" @click="closeMedia">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true" class="h-5 w-5"><path d="m6 6 12 12M6 18 18 6" /></svg>
          </button>
        </header>
        <img v-if="selectedContent.file.type.startsWith('image/')" :src="selectedContent.previewUrl" alt="Imagen seleccionada ampliada" class="lightbox-media rounded-2xl object-contain" />
        <video v-else ref="lightboxVideo" :src="selectedContent.previewUrl" controls playsinline preload="metadata" class="lightbox-media rounded-2xl object-contain" />
      </template>
    </BrowserModal>
    <LocalModal :open="isLinkModalOpen" title="Agregar enlace" title-id="link-title" @close="isLinkModalOpen = false">
      <form class="flex flex-col gap-4" novalidate @submit.prevent="addLink">
        <p class="text-sm">Pega el enlace de tu foto o video.</p>
        <label for="content-link" class="sr-only">Enlace de tu foto o video</label>
        <input id="content-link" v-model="linkDraft" type="url" placeholder="https://..." autocomplete="off" class="local-input" :aria-invalid="!!linkError" :aria-describedby="linkError ? 'link-error' : undefined" @input="linkError = ''" />
        <p v-if="linkError" id="link-error" class="text-sm font-bold text-red-700" role="alert">{{ linkError }}</p>
        <div class="grid grid-cols-2 gap-3">
          <button type="button" class="local-button" @click="isLinkModalOpen = false">Cancelar</button>
          <button type="submit" class="local-button local-primary">Agregar</button>
        </div>
      </form>
    </LocalModal>
  </section>
</template>
