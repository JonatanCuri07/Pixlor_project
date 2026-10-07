<script setup lang="ts">
useHead({ title: 'Sube tu creación · Pixlor' })
const uploadOptions = [
  { label: 'Cámara', icon: 'camera', color: 'green' },
  { label: 'Galería', icon: 'gallery', color: 'purple' },
  { label: 'Link', icon: 'link', color: 'orange' },
] as const
</script>

<template>
  <div class="upload-screen mx-auto">
    <AppTopBar menu />
    <h1 class="upload-title text-center"><span>Sube tu</span><strong>creación</strong></h1>
    <p class="upload-subtitle mx-auto text-center font-extrabold">Comparte tu reto y gana<br />Pixlor Coins.</p>
    <CharacterHero />
    <section class="upload-board relative">
      <h2 class="sr-only">Selecciona tu contenido</h2>
      <button type="button" class="upload-dropzone flex w-full flex-col items-center justify-center text-center">
        <AppIcon name="upload" class="upload-cloud" />
        <strong class="mt-5">Arrastra tu foto o video aquí</strong>
        <span class="mt-1 text-indigo-200">o selecciona un archivo</span>
      </button>
      <div class="upload-options grid grid-cols-3 gap-5">
        <div v-for="option in uploadOptions" :key="option.icon" class="min-w-0 text-center">
          <MagicButton :color="option.color" class="upload-option" :aria-label="option.label"><AppIcon :name="option.icon" /></MagicButton>
          <span class="mt-2 block font-extrabold text-white">{{ option.label }}</span>
        </div>
      </div>
      <span class="leaf-cluster leaf-top" aria-hidden="true" />
      <span class="leaf-cluster leaf-bottom" aria-hidden="true" />
    </section>
    <MagicButton arrow class="upload-submit mt-5">Subir contenido</MagicButton>
    <p class="upload-note mt-4 flex items-center justify-center gap-2 text-center text-white"><AppIcon name="lock" class="shrink-0" />Tu contenido es revisado por nuestro equipo.</p>
  </div>
</template>
