<script setup lang="ts">
import type { Product } from '~/data/products'
defineProps<{ product: Product | null; stage: 'confirm' | 'success' | null }>()
const emit = defineEmits<{ confirm: []; close: [] }>()
</script>

<template>
  <MagicModal :open="stage !== null" :title-id="stage === 'success' ? 'success-title' : 'confirm-title'" :variant="stage === 'success' ? 'success' : 'confirm'" @close="emit('close')">
    <template #artwork>
      <div v-if="stage === 'confirm'" class="confirmation-actions absolute grid grid-cols-2 gap-2">
        <ArtworkButton asset="confirm/accept" desktop-asset="confirm/accept" label="SÍ, CANJEAR" @click="emit('confirm')" />
        <ArtworkButton asset="confirm/cancel" desktop-asset="confirm/cancel" label="CANCELAR" @click="emit('close')" />
      </div>
      <template v-else-if="stage === 'success'">
        <img src="/images/official/desktop/success/bunny.webp" alt="" aria-hidden="true" class="success-bunny hidden lg:block" />
        <div class="success-copy sr-only">
          <h2 id="success-title">¡LISTO!</h2>
          <p class="success-copy-heading">Tu premio ha sido canjeado.</p>
          <p>Comunícate con nuestro asistente de Pixlor por WhatsApp para conocer los métodos de recojo y dónde puedes recoger tu premio.</p>
        </div>
        <ArtworkButton asset="success/whatsapp" desktop-asset="success/whatsapp" label="Hablar por WhatsApp" class="success-whatsapp absolute" />
      </template>
    </template>
    <h2 v-if="stage !== 'success'" id="confirm-title" class="sr-only">¿ESTÁS SEGURO QUE QUIERES CANJEAR ESTE ARTÍCULO?</h2>
    <p v-if="product" class="modal-product mx-auto mt-2 w-fit max-w-full rounded-2xl bg-orange-50 px-4 py-2 text-center text-sm font-black">{{ product.name }} · {{ product.price }} Coins</p>
    <div v-if="stage === 'success'" class="success-actions mx-auto mt-2">
      <ArtworkButton asset="success/return" desktop-asset="success/return" label="Volver a la tienda" @click="emit('close')" />
    </div>
  </MagicModal>
</template>
