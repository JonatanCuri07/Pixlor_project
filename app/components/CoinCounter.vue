<script setup lang="ts">
withDefaults(defineProps<{ amount?: number; compact?: boolean }>(), { amount: 250, compact: false })
</script>

<template>
  <span :class="['coin-counter inline-flex items-center gap-2', { 'coin-compact': compact }]" :aria-label="`${amount} Pixlor Coins`">
    <svg viewBox="0 0 48 48" aria-hidden="true" class="coin-art shrink-0">
      <circle cx="24" cy="24" r="22" fill="#f8a600" stroke="#fff0a0" stroke-width="2" />
      <circle cx="24" cy="24" r="17.5" fill="#ffd547" stroke="#d47c05" stroke-width="1.5" />
      <path d="m24 10 4.2 8.5 9.4 1.4-6.8 6.6 1.6 9.4-8.4-4.4-8.4 4.4 1.6-9.4-6.8-6.6 9.4-1.4Z" fill="#fff29b" stroke="#e59400" stroke-width="1.4" />
      <path d="M10 17a17 17 0 0 1 15-10" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" />
    </svg>
    <span>{{ amount }}</span>
  </span>
</template>
