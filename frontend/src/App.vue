<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'index' }">Index</router-link> |
      <router-link :to="{ name: 'detail', params: { tmdb_id: 129 } }"
        >Detail</router-link
      >| <router-link :to="{ name: 'community' }">자유게시판</router-link> |
      <router-link :to="{ name: 'signup' }">회원가입</router-link> |
      <router-link :to="{ name: 'login' }">로그인</router-link> |
      <router-link :to="{ name: 'index' }" @click="$store.commit('LOG_OUT')"
        >로그아웃</router-link
      >
    </nav>
    <router-view />
  </div>
</template>

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
