import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'

import createPersistedState from 'vuex-persistedstate'

// vuex 암호화. 하지만 sessionStorage는 지원하지 않음
// import SecureLS from 'secure-ls'
// const ls = new SecureLS({ isCompression: false })
// window.sessionStorage.getItem = (key) => ls.get(key)
// window.sessionStorage.setItem = (key, value) => ls.set(key, value)
// window.sessionStorage.removeItem = (key) => ls.remove(key)

Vue.use(Vuex)

// dj-rest-auth docs
// https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html

const store = new Vuex.Store({
  plugins: [
    createPersistedState({
      // session storage에 저장
      storage: window.sessionStorage,
      // 해당 내용은 굳이 저장할 필요 없음
      blackList: ['posts', 'movie', 'users'],
    }),
  ],

  state: {
    // 로컬 Django 서버 주소
    API_URL: 'http://127.0.0.1:8000',
    darkMode: false,

    token: null,
    user: null,
    posts: [],
    movie: null,
    showLoginModal: false,
    showSignUpModal: false,
    showUsersModal: false,
    users: [],
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
    },
    GET_USER_INFO(state, userInfo) {
      state.user = userInfo
    },
    LOG_OUT(state) {
      state.token = null
      state.user = null
    },
    WITHDRAW(state) {
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
    TOGGLE_LOGIN_MODAL(state, boolean) {
      state.showLoginModal = boolean
    },
    TOGGLE_SIGNUP_MODAL(state, boolean) {
      state.showSignUpModal = boolean
    },
    TOGGLE_USERS_MODAL(state, boolean) {
      state.showUsersModal = boolean
    },
    SAVE_USERS(state, users) {
      state.users = users
    },
    TOGGLE_DARK_MODE(state, boolean) {
      state.darkMode = boolean
    },
  },
  actions: {
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${context.state.API_URL}/accounts/signup/`,
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
    logOut(context) {
      axios({
        method: 'post',
        url: `${context.state.API_URL}/accounts/logout/`,
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
        url: `${context.state.API_URL}/accounts/user/`,
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
        url: `${context.state.API_URL}/community/posts/`,
      })
        .then((res) => {
          context.commit('GET_POSTS', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getMovie(context, movieId) {
      if (context.getters.isLogin) {
        axios({
          method: 'get',
          url: `${context.state.API_URL}/movies/${movieId}/`,
          headers: {
            Authorization: `Token ${context.state.token}`,
          },
        })
          .then((res) => {
            console.log(res)
            const movie = res.data
            context.commit('GET_MOVIE', movie)
          })
          .catch((err) => {
            router.push({ name: 'NotFound404' })
            console.log(err)
          })
      } else {
        axios({
          method: 'get',
          url: `${context.state.API_URL}/movies/${movieId}/unlogin/`,
        })
          .then((res) => {
            console.log(res)
            const movie = res.data
            context.commit('GET_MOVIE', movie)
          })
          .catch((err) => {
            router.push({ name: 'NotFound404' })
            console.log(err)
          })
      }
    },
  },
})

export default store
