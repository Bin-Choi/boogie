<template>
  <div class="p-3" :class="darkMode ? 'box-dark' : 'box-light'">
    <h5 class="fw-bold">영화 &#10084;</h5>
    <div>
      <ProfileMovieListItem
        v-for="movie in likeMovies"
        :key="`movie-${movie.id}`"
        :movie="movie" />
    </div>
  </div>
</template>

<script>
import ProfileMovieListItem from '@/components/ProfileMovieListItem.vue'

export default {
  name: 'ProfileMovieList',
  components: {
    ProfileMovieListItem,
  },
  props: {
    likeMovies: Array,
  },
  computed: {
    darkMode() {
      return this.$store.state.darkMode
    },
  },
}
</script>

<style></style>
