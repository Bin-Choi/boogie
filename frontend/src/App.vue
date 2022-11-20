<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'index' }">Index</router-link> |
      <router-link :to="{ name: 'movieDetail', params: { movieId: 129 } }"
        >Detail</router-link
      >| <router-link :to="{ name: 'community' }">자유게시판</router-link> |
      <!-- <router-link :to="{ name: 'signup' }">회원가입</router-link> | -->
      <button id="show-modal" @click="showSignUpModal = true">회원가입</button>

      <!-- use the modal component, pass in the prop -->
      <SignUpModal :show="showSignUpModal" @close="showSignUpModal = false">
        <template #header>
          <h3>SignUp</h3>
        </template>
      </SignUpModal>

      <!-- <router-link :to="{ name: 'login' }">로그인</router-link> | -->
      <button id="show-modal" @click="showLoginModal = true">로그인</button>

      <!-- use the modal component, pass in the prop -->
      <LoginModal :show="showLoginModal" @close="showLoginModal = false">
        <template #header>
          <h3>Login</h3>
        </template>
      </LoginModal>

      <router-link
        :to="{
          name: 'profile',
          params: { username: $store.state.user?.username },
        }"
        >내프로필</router-link
      >
      |
      <a @click.prevent="$store.commit('LOG_OUT')">로그아웃</a>|
      <input @keyup.enter="search" type="text" />
    </nav>
    <router-view />
  </div>
</template>

<script>
import LoginModal from './views/LoginModal.vue'
import SignUpModal from './views/SignUpModal.vue'

export default {
  name: 'App',
  components: {
    LoginModal,
    SignUpModal,
  },
  data() {
    return {
      showLoginModal: false,
      showSignUpModal: false,
    }
  },
  methods: {
    search(event) {
      const query = event.target.value
      event.target.value = null
      this.$router.push({
        name: 'search',
        params: { query: query },
      })
    },
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #f9f4f4;
}

nav {
  background-color: #56357b;
  padding: 15px;
}

nav a {
  font-weight: bold;
  color: #b9a0d4;
}

nav a.router-link-exact-active {
  color: #ffffff;
}
</style>
