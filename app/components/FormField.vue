<script setup lang="ts">
const props = withDefaults(defineProps<{ label: string; type?: 'email' | 'password'; autocomplete?: string; name: string; readonly?: boolean }>(), { type: 'email', readonly: false })
const model = defineModel<string>({ default: '' })
const isVisible = ref(false)
const inputType = computed(() => props.type === 'password' && isVisible.value ? 'text' : props.type)
</script>

<template>
  <div :class="['form-field relative flex items-center', `field-${type}`]">
    <label :for="name" class="sr-only">{{ label }}</label>
    <input :id="name" v-model="model" :type="inputType" :name="name" :readonly="readonly" :placeholder="label" :autocomplete="autocomplete" class="min-w-0 w-full bg-transparent outline-none" />
    <button v-if="type === 'password'" type="button" :aria-label="isVisible ? 'Ocultar la contraseña' : 'Mostrar la contraseña'" :aria-pressed="isVisible" class="password-toggle absolute inset-y-0 right-0" @click="isVisible = !isVisible">
      <span class="sr-only">{{ isVisible ? 'Ocultar' : 'Mostrar' }}</span>
    </button>
  </div>
</template>
