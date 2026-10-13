<script setup lang="ts">
import { products } from '~/data/products'
import type { Product } from '~/data/products'
const emit = defineEmits<{ select: [product: Product] }>()
</script>

<template>
  <div class="store-screen mx-auto">
    <AppTopBar />
    <CharacterHero variant="store" />
    <h1 class="store-banner mx-auto"><picture><source media="(min-width: 1024px)" srcset="/images/official/desktop/store/banner.webp" /><img src="/images/official/store/banner.webp" alt="Tienda de recompensas" class="block h-auto w-full object-contain" /></picture></h1>
    <img src="/images/official/store/stripe.webp" alt="" aria-hidden="true" class="store-stripe block h-auto w-full" />
    <section class="product-grid grid grid-cols-2 gap-3" aria-label="Tienda de recompensas">
      <StoreProductCard v-for="product in products" :key="product.id" :product="product" @select="emit('select', $event)" />
    </section>
    <WhatsappHelpBar class="mt-4" />
  </div>
</template>
