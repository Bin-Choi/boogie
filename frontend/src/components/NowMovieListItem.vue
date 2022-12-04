<template>
  <figure @click="toMovieDetail">
    <img :src="poster_url" style="height: 100%" />
  </figure>
</template>

<script>
export default {
  name: 'ProfileMovieListItem',
  props: {
    index: Number,
    movie: Object,
  },
  computed: {
    poster_url() {
      if (this.movie.poster_path) {
        return `https://image.tmdb.org/t/p/original${this.movie.poster_path}`
      } else {
        return require('@/assets/movie_default_poster.png')
      }
    },
  },
  methods: {
    toMovieDetail() {
      this.$router.push({
        name: 'movieDetail',
        params: { movieId: this.movie.id },
      })
    },
  },
}
</script>

<style scoped></style>
