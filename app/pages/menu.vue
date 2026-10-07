<script setup lang="ts">
useHead({ title: 'Tu aventura · Pixlor' })
</script>

<template>
  <div class="auth-screen menu-screen mx-auto">
    <PixlorLogo />
    <CharacterHero />
    <MagicPanel class="menu-panel flex flex-col">
      <h1 class="sr-only">Menú principal de Pixlor</h1>
      <MagicButton icon="user" class="menu-button"><span>MI PERFIL</span><AppIcon name="chevron" /></MagicButton>
      <MagicButton to="/store" color="orange" icon="cart" class="menu-button"><span>TIENDA</span><AppIcon name="chevron" /></MagicButton>
      <MagicButton color="red" icon="logout" class="menu-button logout-button">CERRAR SESIÓN</MagicButton>
    </MagicPanel>
    <NuxtLink to="/upload" class="preview-link">Sube tu creación <AppIcon name="arrow" /></NuxtLink>
    <NuxtLink to="/" class="preview-link mt-2">Volver al inicio</NuxtLink>
  </div>
</template>
