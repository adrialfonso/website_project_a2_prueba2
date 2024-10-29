<template>
  <div>
    <div v-if="!isLogged">
      <router-link to="/login" v-slot="{ navigate }" custom>
        <button @click="navigate" class="btn">Log In</button>
      </router-link>

      <router-link to="/account" v-slot="{ navigate }" custom>
        <button @click="navigate" class="btn">Sign Up</button>
      </router-link>
    </div>
    <div v-else>
      <p>Welcome</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data () {
    return {
      isLogged: false
    }
  },
  created () {
    this.initializeFromRoute()
  },
  watch: {
    '$route.query': {
      handler () {
        this.initializeFromRoute()
      },
      immediate: true
    }
  },
  methods: {
    initializeFromRoute () {
      this.isLogged = this.$route.query.logged === 'true'
      this.username = this.$route.query.username
      this.token = this.$route.query.token
      if (this.isLogged === undefined) {
        this.isLogged = false
      }
    },
    async reload () {
      if (localStorage.access_token) {
        this.token = localStorage.access_token
      }
    }
  },
  async mounted () {
    await this.reload()
  }
}
</script>

<style>
</style>
