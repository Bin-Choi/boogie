<template>
  <div>
    <h1>Movie detail</h1>
    <p>{{ movie }}</p>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "MovieItem",
  data() {
    return {
      movie: null,
    }
  },
  methods: {
    getMovie() {
      axios
        .get(
          `http://127.0.0.1:8000/movies/detail/${this.$route.params.tmdb_id}`
        )
        .then((response) => {
          this.movie = response.data
        })
        .catch((error) => console.log(error))
    },
  },
  created() {
    this.getMovie()
  },
}
</script>

<style></style>
