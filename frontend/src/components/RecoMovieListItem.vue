<template>
  <div class="poster d-inline-block ms-2 me-1 mt-2" @click="toMovieDetail">
    <img style="width: 100%; object-fit: cover" :src="poster_url" />
  </div>
</template>

<script>
export default {
  name: 'RecoMovieListItem',
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
  width: 140px;
  height: 200px;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.2s linear;
  border-radius: 20px;
  box-shadow: 0 3px 5px 3px rgb(110, 110, 110);
}

.poster:hover {
  transform: scale(1.1);
}
</style>
