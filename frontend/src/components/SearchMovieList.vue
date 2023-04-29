<template>
  <div class="py-3 px-2">
    <h5 class="fw-bold">영화 검색결과</h5>
    <div class="mt-3 mb-2">
      <SearchMovieListItem
        v-for="(movie, index) in searchMovies"
        :key="index"
        :movie="movie" />
    </div>
  </div>
</template>

<script>
import SearchMovieListItem from '@/components/SearchMovieListItem.vue'
import axios from 'axios'

export default {
  name: 'SearchMovieList',
  components: {
    SearchMovieListItem,
  },
  data() {
    return {
      searchMovies: [],
    }
  },
  computed: {
    API_URL() {
      return this.$store.state.API_URL
    },
  },
  watch: {
    $route() {
      this.getSearchMovies()
    },
  },
  created() {
    this.getSearchMovies()
  },
  methods: {
    getSearchMovies() {
      axios({
        method: 'get',
        url: `${this.API_URL}/movies/${this.$route.params.query}/tmdb/`,
      })
        .then((res) => {
          this.searchMovies = res.data.results.slice(0, 5)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
