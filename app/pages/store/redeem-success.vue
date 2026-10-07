<script setup lang="ts">
useHead({ title: 'Premio canjeado · Pixlor' })
</script>

<template>
  <StoreView covered />
  <MagicModal title-id="success-title">
    <div class="success-content relative text-center">
      <img src="/images/characters/bunny-success.webp" alt="" class="success-character" aria-hidden="true" width="500" height="700" />
      <div class="success-copy relative">
        <h2 id="success-title" class="playful-heading">¡LISTO!</h2>
        <p class="mt-2 text-lg font-black">Tu premio ha sido canjeado.</p>
        <p class="mt-2 leading-snug">Ahora comunícate con nuestro asistente de Pixlor por WhatsApp para conocer los métodos de recojo y dónde puedes recoger tu premio.</p>
        <MagicButton color="green" icon="whatsapp" arrow class="mt-4">Hablar por WhatsApp</MagicButton>
        <NuxtLink to="/store" class="secondary-button mt-3 flex items-center justify-center gap-3"><AppIcon name="back" />Volver a la tienda</NuxtLink>
      </div>
    </div>
  </MagicModal>
</template>
