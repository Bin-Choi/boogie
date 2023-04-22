<template>
  <div class="p-3" :class="darkMode ? 'box-dark' : 'box-light'">
    <h5 class="fw-bold mb-3">
      <span v-if="isLogin">{{ user?.username }}님을 위한</span>추천영화
    </h5>
    <div>
      <RecoMovieListItem
        v-for="movie in recoMovies"
        :key="movie.id"
        :movie="movie" />
    </div>
  </div>
</template>

<script>
import RecoMovieListItem from '@/components/RecoMovieListItem.vue'
import axios from 'axios'

// const API_URL = 'https://boogiee.site'

export default {
  name: 'RecoMovieList',
  components: {
    RecoMovieListItem,
  },
  data() {
    return {
      recoMovies: null,
    }
  },
  computed: {
    API_URL() {
      return this.$store.state.API_URL
    },
    user() {
      return this.$store.state.user
    },
    isLogin() {
      return this.$store.getters.isLogin
    },
    darkMode() {
      return this.$store.state.darkMode
    },
  },
  watch: {
    user() {
      this.getRecoMovies()
    },
  },
  created() {
    this.getRecoMovies()
  },
  methods: {
    getRecoMovies() {
      if (this.isLogin) {
        axios({
          method: 'get',
          url: `${this.API_URL}/movies/recommend/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
          .then((res) => {
            this.recoMovies = res.data
          })
          .catch((err) => {
            console.log(err)
          })
      } else {
        axios({
          method: 'get',
          url: `${this.API_URL}/movies/recommend/unlogin/`,
        })
          .then((res) => {
            this.recoMovies = res.data
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
  },
}
</script>

<style></style>
