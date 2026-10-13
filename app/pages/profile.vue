<script setup lang="ts">
useHead({ title: 'Mi perfil · Pixlor' })
const newPassword = ref('')
const confirmPassword = ref('')
const passwordError = ref('')
const passwordFeedback = ref('')
const deleteFeedback = ref('')
const isDeleteModalOpen = ref(false)

const changePassword = () => {
  passwordFeedback.value = ''
  if (!newPassword.value || !confirmPassword.value) {
    passwordError.value = 'Completa los dos campos de contraseña.'
    return
  }
  if (newPassword.value !== confirmPassword.value) {
    passwordError.value = 'Las contraseñas no coinciden.'
    return
  }
  passwordError.value = ''
  newPassword.value = ''
  confirmPassword.value = ''
  passwordFeedback.value = 'Cambio de contraseña demostrado. No se han guardado cambios.'
}
const confirmDelete = () => {
  isDeleteModalOpen.value = false
  deleteFeedback.value = 'Demostración completada. No se eliminó ninguna cuenta.'
}
</script>

<template>
  <div class="profile-screen mx-auto">
    <AppTopBar />
    <MagicPanel class="mt-5">
      <h1 class="mb-5 text-center text-3xl font-black">Mi perfil</h1>
      <section aria-labelledby="profile-information">
        <h2 id="profile-information" class="mb-3 text-lg font-black">Tu cuenta</h2>
        <p class="mb-1 text-sm font-bold">Correo electrónico</p>
        <FormField name="profile-email" label="Correo electrónico" model-value="usuario@pixlor.com" readonly />
      </section>
      <section class="mt-6 border-t border-orange-200 pt-5" aria-labelledby="change-password-title">
        <h2 id="change-password-title" class="mb-3 text-lg font-black">Cambiar contraseña</h2>
        <form class="flex flex-col gap-3" novalidate @submit.prevent="changePassword">
          <FormField v-model="newPassword" name="new-password" label="Nueva contraseña" type="password" autocomplete="new-password" />
          <FormField v-model="confirmPassword" name="confirm-password" label="Repetir nueva contraseña" type="password" autocomplete="new-password" />
          <p v-if="passwordError" class="text-sm font-bold text-red-700" role="alert">{{ passwordError }}</p>
          <p v-if="passwordFeedback" class="text-sm font-bold text-green-800" role="status">{{ passwordFeedback }}</p>
          <button type="submit" class="local-button local-primary">Cambiar contraseña</button>
        </form>
      </section>
      <section class="mt-6 rounded-2xl border border-red-200 bg-red-50 p-4" aria-labelledby="delete-account-title">
        <h2 id="delete-account-title" class="text-lg font-black text-red-800">Eliminar cuenta</h2>
        <p class="mt-2 text-sm">Esta acción eliminará permanentemente tu cuenta.</p>
        <button type="button" class="local-button local-danger mt-4 w-full" @click="isDeleteModalOpen = true">Eliminar cuenta</button>
        <p v-if="deleteFeedback" class="mt-3 text-sm font-bold" role="status">{{ deleteFeedback }}</p>
      </section>
    </MagicPanel>
    <LocalModal :open="isDeleteModalOpen" title="¿Seguro que quieres eliminar tu cuenta?" title-id="delete-modal-title" @close="isDeleteModalOpen = false">
      <p class="text-sm">Esta versión es una demostración. Tu cuenta no se eliminará.</p>
      <div class="mt-5 flex flex-wrap gap-3">
        <button type="button" class="local-button flex-1" @click="isDeleteModalOpen = false">Cancelar</button>
        <button type="button" class="local-button local-danger flex-1" @click="confirmDelete">Eliminar cuenta</button>
      </div>
    </LocalModal>
  </div>
</template>
