<script setup lang="ts">
useHead({ title: 'Crea tu cuenta · Pixlor' })
</script>

<template>
  <div class="auth-screen register-screen mx-auto">
    <PixlorLogo />
    <CharacterHero />
    <MagicPanel class="auth-panel">
      <h1 class="playful-heading text-center">Crea tu <span class="text-violet-700">cuenta</span></h1>
      <p class="mb-5 mt-2 text-center text-sm">Para empezar a explorar, crea tu cuenta<br />y vive el mundo de Pixlor.</p>
      <form class="flex flex-col gap-3" @submit.prevent>
        <FormField name="username" label="Nombre de usuario" icon="user" autocomplete="username" />
        <FormField name="email" label="Correo electrónico" type="email" icon="mail" autocomplete="email" />
        <FormField name="password" label="Contraseña" type="password" icon="lock" autocomplete="new-password" />
        <MagicButton arrow>Crear cuenta</MagicButton>
        <div class="divider flex items-center gap-2"><span class="flex-1" />o continuar con<span class="flex-1" /></div>
        <div class="register-social grid grid-cols-2 gap-2">
          <SocialButton provider="google" />
          <SocialButton provider="apple" />
        </div>
      </form>
      <NuxtLink to="/" class="mt-4 block text-center text-sm font-bold text-violet-700">Ya tengo una cuenta</NuxtLink>
    </MagicPanel>
  </div>
</template>
