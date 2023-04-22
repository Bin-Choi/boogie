<template>
  <div
    @click="toMovieDetail"
    style="position: relative; width: 100%; padding-bottom: 133%">
    <img
      style="
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
      "
      :src="poster_url" />
  </div>
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
