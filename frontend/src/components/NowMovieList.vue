<template>
  <div>
    <h3>Show Box</h3>
    <div clss="d-flex">
      <NowMovieListItem
        v-for="movie in nowMovies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import NowMovieListItem from '@/components/NowMovieListItem.vue'
import axios from 'axios'

const API = 'http://127.0.0.1:8000'

export default {
  name: 'NowMovieList',
  components: { NowMovieListItem },
  data() {
    return {
      nowMovies: [],
    }
  },
  created() {
    this.getNowMovies()
  },
  methods: {
    getNowMovies() {
      axios({
        method: 'get',
        url: `${API}/movies/now/`,
      })
        .then((res) => {
          this.nowMovies = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
