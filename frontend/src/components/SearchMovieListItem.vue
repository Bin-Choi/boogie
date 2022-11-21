<template>
  <div>
    <div style="width: 200px; cursor: pointer" @click="toMovieDetail">
      <img style="width: 100%; object-fit: cover" :src="poster_url" />
      <p>{{ movie.title }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProfileMovieListItem',
  props: {
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

<style></style>
