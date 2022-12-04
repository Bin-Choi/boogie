<template>
  <div id="app" :class="{ 'app-light': !darkMode, 'app-dark': darkMode }">
    <b-navbar class="nav" toggleable="lg" type="dark">
      <b-navbar-brand
        class="ms-3"
        id="logo-box"
        @click="$router.push({ name: 'index' })"
        style="cursor: pointer">
        <img :src="require('@/assets/logo.png')" alt="" />
      </b-navbar-brand>
      <b-nav-item :to="{ name: 'community' }">자유게시판</b-nav-item>
      <b-nav-item>
        <input
          id="search-bar"
          type="search"
          placeholder="Search"
          @keyup.enter="search" />
      </b-nav-item>

      <b-navbar-toggle class="me-3" target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="me-3 mx-auto">
          <b-nav-item
            v-if="!isLogin"
            id="show-modal"
            @click="toggleLoginModal(true)"
            class="ms-3">
            로그인
          </b-nav-item>
          <b-nav-item
            v-if="!isLogin"
            id="show-modal"
            class="ms-3"
            @click="toggleSignUpModal(true)">
            회원가입</b-nav-item
          >
          <b-nav-item
            v-if="isLogin"
            :to="{
              name: 'profile',
              params: { username: user?.username },
            }"
            class="ms-3"
            style="color: #b9a0d4"
            >{{ user?.username + ' 프로필' }}</b-nav-item
          >
          <b-nav-item v-if="isLogin" @click="logOut" class="ms-3"
            >로그아웃</b-nav-item
          >
        </b-navbar-nav>
      </b-collapse>
      <!-- use the modal component, pass in the prop -->
      <SignUpModal :show="showSignUpModal" @close="toggleSignUpModal(false)">
        <template #header>
          <h3>SignUp</h3>
        </template>
      </SignUpModal>
      <!-- use the modal component, pass in the prop -->
      <LoginModal :show="showLoginModal" @close="toggleLoginModal(false)">
        <template #header>
          <h3>Login</h3>
        </template>
      </LoginModal>
      <!-- use the modal component, pass in the prop -->
      <UsersModal
        :show="showUsersModal"
        :users="users"
        @close="toggleUsersModal(false)">
        <template #header>
          <h3>Users</h3>
        </template>
      </UsersModal>
    </b-navbar>

    <router-view />

    <div
      class="theme d-inline-block ms-1"
      @click="$store.commit('TOGGLE_DARK_MODE', !darkMode)">
      <img
        :src="
          darkMode ? require('@/assets/sun.png') : require('@/assets/moon.png')
        " />
    </div>

    <div id="footer" class="mt-3">
      <div class="container">
        <div class="row justify-content-center mt-3">
          <div style="text-align: center">
            <div>
              <span class="fw-bold">Boogie,</span> the sustainable movie
              community website
            </div>
            <div class="mt-1">&copy; 2022. Byongho96 & Bin-Choi</div>
          </div>
        </div>
        <div class="row justify-content-center mt-3">
          <div class="col-7 col-lg-3">
            <div class="fw-bold">Created by</div>
            <div class="mt-1">
              <div>이병호</div>
              <a
                href="https://github.com/Byongho96"
                target="_blank"
                style="
                  text-decoration: none;
                  color: rgba(255, 255, 255, 0.566);
                ">
                <img
                  width="20px"
                  src="@/assets/GitHub-Mark-Light-32px.png"
                  alt="github_logo"
                  style="opacity: 0.7" />
                link
              </a>
              <span class="mx-2">&#8729;</span>
              <span>
                <img
                  width="20px"
                  src="@/assets/gmail_logo.png"
                  alt="gmail_logo"
                  style="filter: brightness(1.5); opacity: 0.8" />
                unlike96</span
              >
            </div>
            <div>
              <div class="mt-2">최성빈</div>
              <a
                href="https://github.com/Bin-Choi"
                target="_blank"
                style="
                  text-decoration: none;
                  color: rgba(255, 255, 255, 0.566);
                ">
                <img
                  width="20px"
                  src="@/assets/GitHub-Mark-Light-32px.png"
                  alt="github_logo"
                  style="opacity: 0.7" />
                link
              </a>
              <span class="mx-2">&#8729;</span>
              <span
                ><img
                  width="20px"
                  src="@/assets/gmail_logo.png"
                  alt="gmail_logo"
                  style="filter: brightness(1.5); opacity: 0.8" />
                csb5268</span
              >
            </div>
          </div>
          <div class="col-5 col-lg-3">
            <span class="fw-bold">Powered by</span>
            <div class="mt-2">
              <a href="https://developers.naver.com/main/" target="_blank">
                <img
                  src="@/assets/naver_api_logo.jpg"
                  alt="naver_api_logo"
                  style="width: 100%; max-width: 200px; opacity: 0.8" />
              </a>
            </div>
            <div class="mt-2">
              <a
                href="https://developers.themoviedb.org/3/getting-started/introduction"
                target="_blank"
                style="padding-left: 4px">
                <img
                  src="@/assets/tmdb_logo.svg"
                  alt="tmdb_logo"
                  style="width: 100%; max-width: 200px; opacity: 0.8" />
              </a>
            </div>
            <div class="mt-2">
              <a
                href="https://developers.google.com/youtube"
                target="_blank"
                style="padding-left: 3px">
                <img
                  src="@/assets/developed-with-youtube-lowercase-light.png"
                  alt="developed-with-youtube-lowercase-light"
                  style="width: 100%; max-width: 200px; opacity: 0.7" />
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LoginModal from './views/LoginModal.vue'
import SignUpModal from './views/SignUpModal.vue'
import UsersModal from '@/views/UsersModal.vue'

export default {
  name: 'App',
  components: {
    LoginModal,
    SignUpModal,
    UsersModal,
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    user() {
      return this.$store.state.user
    },
    showLoginModal() {
      return this.$store.state.showLoginModal
    },
    showSignUpModal() {
      return this.$store.state.showSignUpModal
    },
    showUsersModal() {
      return this.$store.state.showUsersModal
    },
    users() {
      return this.$store.state.users
    },
    darkMode() {
      return this.$store.state.darkMode
    },
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
    toggleLoginModal(boolean) {
      this.$store.commit('TOGGLE_LOGIN_MODAL', boolean)
    },
    toggleSignUpModal(boolean) {
      this.$store.commit('TOGGLE_SIGNUP_MODAL', boolean)
    },
    toggleUsersModal(boolean) {
      this.$store.commit('TOGGLE_USERS_MODAL', boolean)
    },
    logOut() {
      this.$store.commit('LOG_OUT')
      this.$router.push({ name: 'index' })
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
}

input::placeholder {
  color: rgba(255, 255, 255, 0.452);
}

#search-bar {
  color: white;
  max-width: 250px;
  height: 35px;
  border: 0;
  border-radius: 15px;
  outline: none;
  padding-left: 10px;
  background-color: rgba(255, 255, 255, 0.363);
}

.nav {
  background-color: #310e58;
  padding: 15px;
}

.nav a {
  text-decoration: none;
  color: #b9a0d4;
  font-family: Helvetica;
}

.nav span {
  cursor: pointer;
  font-family: Helvetica;
  color: #b9a0d4;
}

.nav a.router-link-exact-active {
  color: #ffffffe0;
}

#logo-box {
  display: inline-block;
  max-width: 100px;
}

#logo-box img {
  width: 100%;
}

#footer {
  background-color: #310e58;
  min-height: 200px;
  padding: 15px;
  color: rgba(255, 255, 255, 0.566);
  font-size: 15px;
  text-align: left;
}

/* 다크모드 */
.theme {
  background-color: #2e0b5775;
  border-radius: 7px;
  padding: 5px;
  cursor: pointer;
  width: 40px;
  height: 40px;
  position: fixed;
  right: 20px;
  bottom: 20px;
}

.theme img {
  width: 100%;
  filter: brightness(120%);
}

.font-white {
  color: white;
}

.font-black {
  color: black;
}

.app-light {
  background-color: #1c053111;
}

.app-dark {
  background-color: #141316c9;
}

.box-light {
  color: black;
  border-radius: 10px;
  background-color: white;
}

.box-dark {
  color: white;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.137);
}
</style>
