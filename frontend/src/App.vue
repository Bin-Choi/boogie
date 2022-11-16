<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'index' }">Index</router-link> |
      <router-link :to="{ name: 'detail', params: { tmdb_id: 129 } }"
        >Detail</router-link
      >|
      <router-link :to="{ name: 'community' }">자유게시판</router-link>
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
  background-color: #F9F4F4; 
}

nav {
  background-color: #56357B;
  padding: 15px;
}

nav a {
  font-weight: bold;
  color: #B9A0D4;
}

nav a.router-link-exact-active {
  color: #FFFFFF;
}
</style>
