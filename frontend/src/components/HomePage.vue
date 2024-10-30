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
      if (this.isLogged === undefined) {
        this.isLogged = false
      }
    },
    async reload () {
      /* Function called every time the page is mounted */
    }
  },
  async mounted () {
    await this.reload()
  }
}
</script>

<style>
</style>
