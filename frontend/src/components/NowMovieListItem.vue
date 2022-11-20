<template>
  <div>
    <router-link :to="{ name: 'detail', params: { tdmb_id: movie.id } }">
      <div id="show_poster">
        <img :src="poster_url" alt="" height="280" width="180" />
      </div>
      <br />
      <h5>{{ movie.title }}</h5>
    </router-link>
    <p>평점: {{ movie.vote_average }}</p>
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
