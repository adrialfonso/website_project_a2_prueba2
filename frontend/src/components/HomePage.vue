<template>
  <div>
<router-link to="/login" v-slot="{ navigate }" custom>
  <button @click="navigate" class="btn">Log In</button>
</router-link>

<router-link to="/account" v-slot="{ navigate }" custom>
  <button @click="navigate" class="btn">Sign Up</button>
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
