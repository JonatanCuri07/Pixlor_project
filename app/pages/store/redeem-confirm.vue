<script setup lang="ts">
useHead({ title: 'Confirmación de canje · Pixlor' })
</script>

<template>
  <StoreView covered />
  <MagicModal title-id="confirm-title">
    <h2 id="confirm-title" class="confirmation-title text-center font-black">¿ESTÁS SEGURO QUE QUIERES CANJEAR ESTE ARTÍCULO?</h2>
    <div class="confirmation-actions mt-6 grid grid-cols-2 gap-3">
      <MagicButton to="/store/redeem-success" color="green">SÍ,<br />CANJEAR</MagicButton>
      <MagicButton to="/store" color="red">CANCELAR</MagicButton>
    </div>
  </MagicModal>
</template>
