<script setup lang="ts">
useHead({ title: 'Tu aventura · Pixlor' })
</script>

<template>
  <div class="auth-screen menu-screen relative mx-auto">
    <BackButton to="/upload" label="Volver a subir creación" class="auth-back absolute left-0 top-0" />
    <PixlorLogo />
    <CharacterHero variant="menu" />
    <MagicPanel variant="menu" class="menu-panel flex flex-col gap-5">
      <h1 class="sr-only">Menú principal de Pixlor</h1>
      <ArtworkButton to="/profile" asset="menu/profile" label="MI PERFIL" />
      <ArtworkButton to="/store" asset="menu/store" label="TIENDA" />
      <ArtworkButton to="/" asset="menu/logout" label="CERRAR SESIÓN" class="mt-3" />
    </MagicPanel>
    <NuxtLink to="/upload" class="preview-link">Sube tu creación <AppIcon name="arrow" /></NuxtLink>
  </div>
</template>
