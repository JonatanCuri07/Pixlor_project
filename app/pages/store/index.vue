<script setup lang="ts">
import type { Product } from '~/data/products'
useHead({ title: 'Tienda de recompensas · Pixlor' })
const selectedProduct = shallowRef<Product | null>(null)
const stage = ref<'confirm' | 'success' | null>(null)
const selectProduct = (product: Product) => {
  selectedProduct.value = product
  stage.value = 'confirm'
}
const closeRedeem = () => {
  stage.value = null
  selectedProduct.value = null
}
</script>

<template>
  <StoreView @select="selectProduct" />
  <RedeemModal :product="selectedProduct" :stage="stage" @confirm="stage = 'success'" @close="closeRedeem" />
</template>
