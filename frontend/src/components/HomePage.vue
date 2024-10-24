<template>
  <div>
      <router-link to="/login" v-slot="{ href }">
        <button :href="href" class="btn">Log In</button>
      </router-link>

      <router-link to="/account" v-slot="{ href }">
        <button :href="href" class="btn">Sign Up</button>
      </router-link>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
}
</script>

<style>
</style>
