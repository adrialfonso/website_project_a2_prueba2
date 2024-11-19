import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    username: localStorage.getItem('username') || '',
    displayMode: localStorage.getItem('displayMode') || 'grid'
  },
  mutations: {
    setUser (state, payload) {
      state.username = payload.username
      localStorage.setItem('username', payload.username)
    },
    setDisplayMode (state, display) {
      state.displayMode = display
      localStorage.setItem('displayMode', display)
    }
  },
  actions: {
    setUser ({ commit }, payload) {
      commit('setUser', payload)
    },
    setDisplayMode ({ commit }, display) {
      commit('setDisplayMode', display)
    }
  },
  getters: {
    username: state => state.username,
    displayMode: state => state.displayMode
  }
})
