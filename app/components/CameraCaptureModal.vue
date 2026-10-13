<script setup lang="ts">
const props = defineProps<{ open: boolean }>()
const emit = defineEmits<{ close: []; captured: [file: File]; error: [message: string] }>()
const video = ref<HTMLVideoElement>()
const loading = ref(false)
const ready = ref(false)
const capturing = ref(false)
let stream: MediaStream | null = null
let requestVersion = 0

const stopCamera = () => {
  requestVersion++
  stream?.getTracks().forEach(track => track.stop())
  stream = null
  if (video.value) video.value.srcObject = null
  loading.value = false
  ready.value = false
  capturing.value = false
}

const startCamera = async () => {
  stopCamera()
  const version = requestVersion
  if (!navigator.mediaDevices?.getUserMedia) {
    emit('error', 'Este navegador no permite usar la cámara. Puedes seleccionar una foto desde Galería.')
    emit('close')
    return
  }
  loading.value = true
  try {
    const activeStream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false })
    if (version !== requestVersion || !props.open) {
      activeStream.getTracks().forEach(track => track.stop())
      return
    }
    stream = activeStream
    await nextTick()
    if (version !== requestVersion || !video.value) {
      activeStream.getTracks().forEach(track => track.stop())
      return
    }
    video.value.srcObject = activeStream
    await video.value.play()
    if (version === requestVersion) loading.value = false
  } catch (error) {
    if (version !== requestVersion) return
    const name = error instanceof DOMException ? error.name : ''
    const message = name === 'NotAllowedError' || name === 'SecurityError'
      ? 'No se concedió permiso para usar la cámara. Puedes volver a intentarlo o usar Galería.'
      : name === 'NotFoundError' || name === 'OverconstrainedError'
        ? 'No encontramos una cámara disponible. Puedes seleccionar una foto desde Galería.'
        : 'No se pudo activar la cámara. Comprueba que esté disponible e inténtalo otra vez.'
    stopCamera()
    emit('error', message)
    emit('close')
  }
}

const close = () => {
  stopCamera()
  emit('close')
}

const capture = async () => {
  if (!video.value || !ready.value || capturing.value) return
  const version = requestVersion
  capturing.value = true
  try {
    const canvas = document.createElement('canvas')
    canvas.width = video.value.videoWidth
    canvas.height = video.value.videoHeight
    const context = canvas.getContext('2d')
    if (!context) throw new Error('Canvas unavailable')
    context.drawImage(video.value, 0, 0)
    const blob = await new Promise<Blob | null>(resolve => canvas.toBlob(resolve, 'image/jpeg', .92))
    if (version !== requestVersion || !props.open) return
    if (!blob) throw new Error('Capture unavailable')
    const file = new File([blob], 'captura-pixlor.jpg', { type: 'image/jpeg' })
    stopCamera()
    emit('captured', file)
    emit('close')
  } catch {
    if (version === requestVersion) {
      capturing.value = false
      emit('error', 'No se pudo capturar la foto. Inténtalo de nuevo.')
    }
  }
}

watch(() => props.open, open => open ? startCamera() : stopCamera(), { flush: 'post' })
onMounted(() => { if (props.open) startCamera() })
onBeforeUnmount(stopCamera)
</script>

<template>
  <LocalModal :open="open" title="Tu cámara" title-id="camera-title" @close="close">
    <p v-if="loading" class="mb-3 text-sm" role="status">Activando cámara…</p>
    <video ref="video" autoplay muted playsinline class="camera-video block w-full rounded-2xl bg-slate-950 object-contain" @loadeddata="ready = !!video?.videoWidth && !!video?.videoHeight" />
    <div class="mt-4 grid grid-cols-2 gap-3">
      <button type="button" class="local-button" @click="close">Cancelar</button>
      <button type="button" class="local-button local-primary" :disabled="!ready || loading || capturing" @click="capture">{{ capturing ? 'Capturando…' : 'Capturar' }}</button>
    </div>
  </LocalModal>
</template>
