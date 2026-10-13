<script setup lang="ts">
useHead({ title: 'Sube tu creación · Pixlor' })
</script>

<template>
  <div class="upload-screen mx-auto">
    <AppTopBar variant="upload" />
    <h1 class="upload-title mx-auto"><picture><source media="(min-width: 1024px)" srcset="/images/official/desktop/upload/title.webp" /><img src="/images/official/upload/title.webp" alt="Sube tu creación" class="block h-auto w-full object-contain" /></picture></h1>
    <p class="upload-subtitle mx-auto text-center font-extrabold">Comparte tu reto y gana<br />Pixlor Coins.</p>
    <CharacterHero variant="upload" />
    <img src="/images/official/desktop/upload/bunny.webp" alt="" aria-hidden="true" class="upload-bunny hidden lg:block" />
    <UploadContent />
  </div>
</template>
