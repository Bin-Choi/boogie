<template>
  <div
    class="poster d-inline-block ms-5"
    style="width: 200px; cursor: pointer"
    @click="toMovieDetail"
  >
    <img style="width: 100%; object-fit: cover" :src="poster_url" />
    <p>{{ movie.title }}</p>
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

<style scoped>
.poster {
  overflow: hidden;
  transition: transform 0.2s linear;
  border-radius: 20px;
  box-shadow: 0 5px 10px 5px rgb(110, 110, 110);
}

.poster:hover {
  transform: scale(1.1);
}
</style>
