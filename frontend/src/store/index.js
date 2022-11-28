import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    backendUrl: 'http://84.38.180.149:8000'
  },
  mutations: {},
  actions: {},
  modules: {},
  getters: {
    getServerUrl: state => {
      return state.backendUrl
    }
  }
})

export default store
