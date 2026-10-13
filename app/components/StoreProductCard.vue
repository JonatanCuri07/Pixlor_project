<script setup lang="ts">
import type { Product } from '~/data/products'
defineProps<{ product: Product }>()
const emit = defineEmits<{ select: [product: Product] }>()
</script>

<template>
  <button type="button" class="artwork-control product-card block min-w-0" :data-product-id="product.id" :aria-label="`Ver confirmación de canje: ${product.name}, ${product.price} coins`" @click="emit('select', product)">
    <picture class="block"><source media="(min-width: 1024px)" :srcset="`/images/official/desktop/store/${product.id}.webp`" /><img :src="product.image" alt="" aria-hidden="true" width="166" height="227" class="block h-auto w-full object-contain" /></picture>
    <h2 class="sr-only">{{ product.name }} — {{ product.price }} Pixlor Coins</h2>
  </button>
</template>
