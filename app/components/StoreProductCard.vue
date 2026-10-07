<script setup lang="ts">
import type { Product } from '~/data/products'
defineProps<{ product: Product }>()
</script>

<template>
  <NuxtLink to="/store/redeem-confirm" class="product-card flex min-w-0 flex-col" :aria-label="`Ver confirmación de canje: ${product.name}, ${product.price} coins`">
    <img :src="product.image" :alt="product.name" width="400" height="400" class="aspect-square w-full object-cover" loading="lazy" />
    <h2 class="product-name mt-2 flex-1 font-extrabold">{{ product.name }}</h2>
    <CoinCounter :amount="product.price" compact class="mt-2" />
  </NuxtLink>
</template>
