import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [createPersistedState()],

  state: {
    posts: [],
    reviews: [],
    movie: null,
    isVoted: false,
  },
  getters: {},
  mutations: {
    GET_POSTS(state, posts) {
      state.posts = posts
    },
    GET_MOVIE(state, movie) {
      state.movie = movie
    },
    GET_REVIEWS(state, reviews) {
      state.reviews = reviews
    },
    SWITCH_IS_VOTED(state, boolValue) {
      state.isVoted = boolValue
    },
    // DELETE_FIRST_REVIEW(state) {
    //   state.reviews.splice(0, 1)
    // },
  },
  actions: {
    getPosts(context) {
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
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        },
      }).then((res) => {
        context.commit(res.data.key)
      })
    },
    getReviews(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/reviews/movie/${this.movie.id}/`,
      })
        .then((res) => {
          context.commit('GET_REVIEWS', res.data.reviews)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  modules: {},
})
