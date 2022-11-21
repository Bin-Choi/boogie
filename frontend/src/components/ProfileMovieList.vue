<template>
  <div>
    <p>영화 &#10084;</p>
    <ProfileMovieListItem
      v-for="movie in likeMovies"
      :key="`movie-${movie.id}`"
      :movie="movie"
    />
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
}
</script>

<style></style>
