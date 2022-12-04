<template>
  <div class="pt-4 pb-3 mt-3" :class="darkMode ? 'box-dark' : 'box-light'">
    <h4 class="fw-bold mb-2">비슷한 장르의 다른 영화</h4>
    <div>
      <RelatedMovieListItem
        class="ms-2 me-2 mt-2 mb-1"
        v-for="movie in relatedMovies"
        :key="movie.id"
        :movie="movie" />
    </div>
  </div>
</template>

<script>
import RelatedMovieListItem from '@/components/RelatedMovieListItem.vue'
import axios from 'axios'

// const API_URL = "https://boogiee.site"

export default {
  name: 'RecoMovieList',
  components: {
    RelatedMovieListItem,
  },
  data() {
    return {
      relatedMovies: null,
    }
  },
  computed: {
    API_URL() {
      return this.$store.state.API_URL
    },
    movie() {
      return this.$store.state.movie
    },
    darkMode() {
      return this.$store.state.darkMode
    },
  },
  watch: {
    movie() {
      this.getRelatedMovies(this.$route.params.movieId)
    },
  },
  created() {
    this.getRelatedMovies(this.$route.params.movieId)
  },
  methods: {
    getRelatedMovies(movieId) {
      axios({
        method: 'get',
        url: `${this.API_URL}/movies/${movieId}/related/`,
      })
        .then((res) => {
          console.log(res)
          this.relatedMovies = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style scoped></style>
