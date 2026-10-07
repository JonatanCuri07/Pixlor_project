<script setup lang="ts">
useHead({ title: 'Iniciar sesión · Pixlor' })
</script>

<template>
  <div class="auth-screen mx-auto">
    <PixlorLogo />
    <CharacterHero />
    <MagicPanel class="auth-panel">
      <h1 class="sr-only">Iniciar sesión en Pixlor</h1>
      <form class="flex flex-col gap-4" @submit.prevent>
        <FormField name="email" label="Correo electrónico" type="email" icon="mail" autocomplete="email" />
        <FormField name="password" label="Contraseña" type="password" icon="lock" autocomplete="current-password" />
        <p class="signup-prompt text-center">¿No tienes una cuenta? <NuxtLink to="/register" class="font-black text-violet-700">Regístrate</NuxtLink></p>
        <MagicButton>INICIAR SESIÓN</MagicButton>
        <div class="divider flex items-center gap-3" aria-hidden="true"><span class="flex-1" />o<span class="flex-1" /></div>
        <SocialButton provider="google" />
        <SocialButton provider="facebook" />
      </form>
    </MagicPanel>
    <NuxtLink to="/menu" class="preview-link">Explorar las pantallas <AppIcon name="arrow" /></NuxtLink>
  </div>
</template>
