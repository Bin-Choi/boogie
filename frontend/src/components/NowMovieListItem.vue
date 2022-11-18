<template>
  <div>
    <div id="show_poster">
      <img :src="poster_url" alt="" />
    </div>
    {{ movie.title }}
    {{ movie.vote_average }}
    <hr />
  </div>
</template>

<script>
export default {
  name: "NowMovieListItem",
  props: {
    movie: Object,
  },
  computed: {
    poster_url() {
      return `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
    },
  },
}
</script>

<style></style>
