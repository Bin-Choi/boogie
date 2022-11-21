<template>
  <div>
    <SearchMovieListItem
      v-for="(movie, index) in searchMovies"
      :key="index"
      :movie="movie"
    />
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
  created() {
    this.getSearchMovies()
  },
  methods: {
    getSearchMovies() {
      const params = {
        api_key: '6f44898888940b2a302f0cdbee081d68',
        language: 'ko-KO',
        query: this.$route.params.query,
      }

      axios({
        method: 'get',
        url: 'https://api.themoviedb.org/3/search/movie',
        params,
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
