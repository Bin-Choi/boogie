import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'

import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

// dj-rest-auth docs
// https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html
const API_URL = 'http://127.0.0.1:8000'

const store = new Vuex.Store({
  plugins: [createPersistedState()],

  state: {
    token: null,
    user: null,
    posts: [],
    movie: null,
    // isVoted: false,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
  },
  mutations: {
    // 회원가입 && 로그인
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'index' })
    },
    GET_USER_INFO(state, userInfo) {
      state.user = userInfo
    },
    LOG_OUT(state) {
      state.token = null
      state.user = null
    },
    // 그 외
    GET_POSTS(state, posts) {
      state.posts = posts
    },
    GET_MOVIE(state, movie) {
      state.movie = movie
    },
  },
  actions: {
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        },
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
          context.dispatch('getUserInfo')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        },
      })
        .then((res) => {
          console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
          context.dispatch('getUserInfo')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    logOut(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${context.state.token}`,
        },
      })
        .then(() => {
          // console.log(res)
          context.commit('LOG_OUT')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getUserInfo(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${context.state.token}`,
        },
      })
        .then((res) => {
          const userInfo = {
            id: res.data.pk,
            username: res.data.username,
            email: res.data.email,
            firstName: res.data.first_name,
            lastName: res.data.last_name,
          }
          context.commit('GET_USER_INFO', userInfo)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getPosts(context) {
      axios({
        method: 'get',
        url: `${API_URL}/community/posts/`,
      })
        .then((res) => {
          context.commit('GET_POSTS', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getMovie(context, movieId) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${movieId}/`,
      })
        .then((res) => {
          console.log(res)
          const movie = res.data
          if (movie.like_users.includes(context.state.user?.id)) {
            movie.isLiked = true
          } else {
            movie.isLiked = false
          }
          context.commit('GET_MOVIE', movie)
        })
        .catch((err) => {
          router.push({ name: 'NotFound404' })
          console.log(err)
        })
    },
  },
})

export default store
