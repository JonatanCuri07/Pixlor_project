<script setup lang="ts">
withDefaults(defineProps<{ register?: boolean }>(), { register: false })
const acceptsTerms = ref(false)
</script>

<template>
  <div class="auth-screen relative mx-auto">
    <BackButton v-if="register" class="auth-back absolute left-0 top-0" />
    <PixlorLogo />
    <CharacterHero />
    <MagicPanel>
      <h1 :class="register ? 'mb-4 text-center text-2xl font-black' : 'sr-only'">{{ register ? 'Crea tu cuenta' : 'Iniciar sesión en Pixlor' }}</h1>
      <form class="flex flex-col gap-3" novalidate @submit.prevent="navigateTo(register ? '/' : '/upload')">
        <FormField name="email" label="Correo electrónico" autocomplete="email" />
        <FormField name="password" label="Contraseña" type="password" :autocomplete="register ? 'new-password' : 'current-password'" />
        <FormField v-if="register" name="repeat-password" label="Repetir contraseña" type="password" autocomplete="new-password" />
        <label v-if="register" class="terms-label flex cursor-pointer items-start gap-2">
          <input v-model="acceptsTerms" type="checkbox" name="terms" class="mt-0.5 h-4 w-4 shrink-0 accent-violet-700" />
          <span>He leído y acepto los <button type="button" class="font-black text-violet-700 underline">Términos y Condiciones</button>.</span>
        </label>
        <p v-else class="signup-prompt text-center">¿No tienes una cuenta? <NuxtLink to="/register" class="font-black text-violet-700">Regístrate aquí</NuxtLink></p>
        <ArtworkButton :asset="register ? 'auth/register' : 'auth/login'" :desktop-asset="register ? 'auth/register' : 'auth/login'" :label="register ? 'REGISTRARME' : 'INICIAR SESIÓN'" :text="register" type="submit" />
        <template v-if="!register">
          <div class="divider flex items-center gap-3" aria-hidden="true"><span class="flex-1" />o<span class="flex-1" /></div>
          <div class="auth-socials flex flex-col gap-3">
            <SocialButton provider="google" />
            <SocialButton provider="facebook" />
          </div>
        </template>
        <p v-else class="signup-prompt text-center">¿Ya tienes una cuenta? <NuxtLink to="/" class="font-black text-violet-700">Inicia sesión</NuxtLink></p>
      </form>
    </MagicPanel>
  </div>
</template>
