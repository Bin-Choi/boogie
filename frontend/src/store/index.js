import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import createPersistedState from 'vuex-persistedstate'



Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],

  state: {
    posts: [],

  },
  getters: {
  },
  mutations: {
    GET_POSTS(state, posts){
      state.posts = posts
    },
  },
  actions: {
    getPosts(context){
      axios({
        method: 'get',
        url: `${API_URL}/community/posts/`,
        // headers: {
        //   Authorization: `Token ${context.state.token}`
        // }
      })
        .then((res) => {
          // console.log(res, context)
          console.log(res.data)
          context.commit('GET_POSTS', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },

  },
  modules: {
  }
})
