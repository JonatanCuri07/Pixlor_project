<script setup lang="ts">
import { products } from '~/data/products'
withDefaults(defineProps<{ covered?: boolean }>(), { covered: false })
</script>

<template>
  <div class="store-screen mx-auto" :inert="covered || undefined" :aria-hidden="covered || undefined">
    <AppTopBar />
    <CharacterHero />
    <div class="wood-banner relative flex items-center justify-center gap-3">
      <span class="store-cart grid shrink-0 place-items-center"><AppIcon name="cart" /></span>
      <h1 class="font-black"><span class="block text-white">TIENDA DE</span><span class="text-yellow-300">RECOMPENSAS</span></h1>
      <span class="leaf-cluster leaf-top" aria-hidden="true" />
      <span class="leaf-cluster leaf-bottom" aria-hidden="true" />
    </div>
    <div class="store-stripe" aria-hidden="true" />
    <section class="product-grid grid grid-cols-2 gap-3" aria-label="Tienda de recompensas">
      <StoreProductCard v-for="product in products" :key="product.id" :product="product" />
    </section>
    <WhatsappHelpBar class="mt-4" />
  </div>
</template>
