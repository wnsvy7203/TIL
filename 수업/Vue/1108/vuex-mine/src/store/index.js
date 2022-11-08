import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'message in store',
  },
  getters: {
    message(state) {
      return state.message
    }
  },
  mutations: {
    CHANGE_MESSAGE(state, newMessage) {
      state.message = newMessage
    }
  },
  actions: {
    changeMessage(context, newMessage) {
      context.commit('CHANGE_MESSAGE', newMessage)
    }
  },
  modules: {
  }
})
