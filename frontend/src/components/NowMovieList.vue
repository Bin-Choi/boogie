<template>
  <div>
    <h3>Show Box</h3>
    <NowMovieListItem
      v-for="movie in nowmovies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script>
import NowMovieListItem from "./NowMovieListItem.vue"
import axios from "axios"
const API = "http://127.0.0.1:8000"

export default {
  name: "NowMovieList",
  components: { NowMovieListItem },
  data() {
    return {
      nowmovies: [],
    }
  },
  computed: {
    nowMovie() {
      return this.$store.state.nowmovie
    },
  },
  methods: {
    getNowMovies() {
      axios({
        method: "get",
        url: `${API}/movies/show/`,
      })
        .then((res) => {
          this.nowmovies = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.getNowMovies()
  },
}
</script>

<style></style>
