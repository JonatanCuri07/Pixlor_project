<script setup lang="ts">
import { isAuthError, isAuthSessionMissingError } from '@supabase/supabase-js'

const props = withDefaults(defineProps<{ register?: boolean }>(), { register: false })
const supabase = props.register ? useSupabase() : null
const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const acceptsTerms = ref(false)
const isLoading = ref(false)
const errorMessage = ref('')

function getRegistrationError(error: unknown) {
  if (isAuthError(error)) {
    if (['user_already_exists', 'email_exists'].includes(error.code ?? '')) {
      return 'Ya existe una cuenta con este correo electrónico.'
    }
    if (error.code === 'weak_password') {
      return 'La contraseña debe tener al menos 8 caracteres.'
    }
    if (error.status === 429 || ['over_request_rate_limit', 'over_email_send_rate_limit'].includes(error.code ?? '')) {
      return 'Se realizaron demasiados intentos. Inténtalo nuevamente en unos minutos.'
    }
    if (['email_address_invalid', 'email_address_not_authorized'].includes(error.code ?? '')) {
      return 'Ingresa un correo electrónico válido.'
    }
  }

  return 'No pudimos crear tu cuenta. Inténtalo nuevamente.'
}

async function handleSubmit() {
  if (isLoading.value) return
  if (!props.register || !supabase) {
    await navigateTo('/upload')
    return
  }

  errorMessage.value = ''
  const normalizedEmail = email.value.trim()

  if (!normalizedEmail || !password.value || !confirmPassword.value) {
    errorMessage.value = 'Completa todos los campos.'
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(normalizedEmail)) {
    errorMessage.value = 'Ingresa un correo electrónico válido.'
  } else if (password.value.length < 8) {
    errorMessage.value = 'La contraseña debe tener al menos 8 caracteres.'
  } else if (password.value !== confirmPassword.value) {
    errorMessage.value = 'Las contraseñas no coinciden.'
  } else if (!acceptsTerms.value) {
    errorMessage.value = 'Debes aceptar los Términos y Condiciones.'
  }

  if (errorMessage.value) return

  isLoading.value = true

  try {
    const { error } = await supabase.auth.signUp({
      email: normalizedEmail,
      password: password.value,
    })

    if (error) {
      errorMessage.value = getRegistrationError(error)
      if (import.meta.dev) console.error('Supabase signUp:', error.code, error.status)
      return
    }

    password.value = ''
    confirmPassword.value = ''

    const { error: signOutError } = await supabase.auth.signOut({ scope: 'local' })

    if (signOutError && !isAuthSessionMissingError(signOutError)) {
      errorMessage.value = 'Tu cuenta fue creada, pero no pudimos cerrar la sesión automática. Recarga la página e inténtalo nuevamente.'
      if (import.meta.dev) console.error('Supabase signOut:', signOutError.code, signOutError.status)
      return
    }

    await navigateTo('/')
  } catch (error) {
    errorMessage.value = getRegistrationError(error)
    if (import.meta.dev) console.error('Supabase registration:', isAuthError(error) ? error.code : 'unexpected_error')
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="auth-screen relative mx-auto">
    <BackButton v-if="register" class="auth-back absolute left-0 top-0" />
    <PixlorLogo />
    <CharacterHero />
    <MagicPanel>
      <h1 :class="register ? 'mb-4 text-center text-2xl font-black' : 'sr-only'">{{ register ? 'Crea tu cuenta' : 'Iniciar sesión en Pixlor' }}</h1>
      <form class="flex flex-col gap-3" novalidate :aria-busy="isLoading" @submit.prevent="handleSubmit">
        <FormField v-model="email" name="email" label="Correo electrónico" autocomplete="email" />
        <FormField v-model="password" name="password" label="Contraseña" type="password" :autocomplete="register ? 'new-password' : 'current-password'" />
        <FormField v-if="register" v-model="confirmPassword" name="repeat-password" label="Repetir contraseña" type="password" autocomplete="new-password" />
        <label v-if="register" class="terms-label flex cursor-pointer items-start gap-2">
          <input v-model="acceptsTerms" type="checkbox" name="terms" class="mt-0.5 h-4 w-4 shrink-0 accent-violet-700" />
          <span>He leído y acepto los <button type="button" class="font-black text-violet-700 underline">Términos y Condiciones</button>.</span>
        </label>
        <p v-else class="signup-prompt text-center">¿No tienes una cuenta? <NuxtLink to="/register" class="font-black text-violet-700">Regístrate aquí</NuxtLink></p>
        <p v-if="errorMessage" role="alert" class="signup-prompt text-center font-bold text-red-700">{{ errorMessage }}</p>
        <ArtworkButton :asset="register ? 'auth/register' : 'auth/login'" :desktop-asset="register ? 'auth/register' : 'auth/login'" :label="register ? (isLoading ? 'Registrando...' : 'REGISTRARME') : 'INICIAR SESIÓN'" :text="register" type="submit" :disabled="isLoading" />
        <p v-if="register" class="signup-prompt text-center">¿Ya tienes una cuenta? <NuxtLink to="/" class="font-black text-violet-700">Inicia sesión</NuxtLink></p>
      </form>
    </MagicPanel>
  </div>
</template>
