<script setup lang="ts">
const props = withDefaults(defineProps<{ label: string; type?: 'email' | 'password' | 'text'; icon: string; autocomplete?: string; name: string }>(), { type: 'text' })
const isVisible = ref(false)
const inputType = computed(() => props.type === 'password' && isVisible.value ? 'text' : props.type)
</script>

<template>
  <label class="form-field flex items-center gap-3">
    <span class="sr-only">{{ label }}</span>
    <AppIcon :name="icon" class="shrink-0" />
    <input :type="inputType" :name="name" :placeholder="label" :autocomplete="autocomplete" class="min-w-0 flex-1 bg-transparent outline-none" />
    <button v-if="type === 'password'" type="button" :aria-label="isVisible ? 'Ocultar la contraseña' : 'Mostrar la contraseña'" :aria-pressed="isVisible" class="password-toggle shrink-0" @click="isVisible = !isVisible">
      <AppIcon :name="isVisible ? 'eye' : 'eyeOff'" />
    </button>
  </label>
</template>
