<script setup lang="ts">
withDefaults(defineProps<{ asset: string; desktopAsset?: string; label: string; to?: string; text?: boolean; type?: 'button' | 'submit'; disabled?: boolean }>(), { text: false, type: 'button', disabled: false })
</script>

<template>
  <NuxtLink v-if="to" :to="to" class="artwork-control relative block w-full" :aria-label="label">
    <picture class="block"><source v-if="desktopAsset" media="(min-width: 1024px)" :srcset="`/images/official/desktop/${desktopAsset}.webp`" /><img :src="`/images/official/${asset}.webp`" alt="" aria-hidden="true" class="block h-auto w-full object-contain" /></picture>
    <span v-if="text" class="artwork-label absolute inset-0 flex items-center justify-center font-black text-white">{{ label }}</span>
  </NuxtLink>
  <button v-else :type="type" :disabled="disabled" class="artwork-control relative block w-full" :aria-label="label">
    <picture class="block"><source v-if="desktopAsset" media="(min-width: 1024px)" :srcset="`/images/official/desktop/${desktopAsset}.webp`" /><img :src="`/images/official/${asset}.webp`" alt="" aria-hidden="true" class="block h-auto w-full object-contain" /></picture>
    <span v-if="text" class="artwork-label absolute inset-0 flex items-center justify-center font-black text-white">{{ label }}</span>
  </button>
</template>
