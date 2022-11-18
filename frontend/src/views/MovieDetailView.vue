<template>
  <div>
    <div id="movie_detail_backdrop">
      <img :src="backdrop_url" />
    </div>
    <div v-if="movie">
      <MovieDetailHeader />
      <div class="d-flex col-8 mx-auto mt-5" style="max-width: 1200px">
        <div class="col-8" style="margin-right: 30px">
          <MovieDetailInfo />
          <ReviewList class="mt-3" />
        </div>
        <VideoList class="col-4" />
      </div>
      <RecoMovieList />
    </div>
  </div>
</template>

<script>
import MovieDetailHeader from '@/components/MovieDetailHeader.vue'
import MovieDetailInfo from '@/components/MovieDetailInfo.vue'
import RecoMovieList from '@/components/RecoMovieList.vue'
import ReviewList from '@/components/ReviewList.vue'
import VideoList from '@/components/VideoList.vue'

import axios from 'axios'
const LOCAL_URL = 'http://127.0.0.1:8000/'

export default {
  name: 'DetailView',
  components: {
    MovieDetailHeader,
    MovieDetailInfo,
    ReviewList,
    VideoList,
    RecoMovieList,
  },
  computed: {
    movie() {
      return this.$store.state.movie
    },
    backdrop_url() {
      if (this.movie?.backdrop_path) {
        return `https://image.tmdb.org/t/p/original${this.movie.backdrop_path}`
      } else {
        return require('@/assets/movie_default_backdrop.png')
      }
    },
  },
  created() {
    this.getMovie()
  },
  methods: {
    getMovie() {
      axios({
        url: LOCAL_URL + `movies/detail/${this.$route.params.tmdb_id}/`,
        method: 'get',
      })
        .then((response) => {
          this.$store.commit('GET_MOVIE', response.data)
        })
        .catch((error) => console.log(error))
    },
  },
}
</script>

<style>
#movie_detail_backdrop {
  width: 100%;
  height: 300px;
  overflow: hidden;
}

#movie_detail_backdrop img {
  width: 100%;
  height: 500px;
  object-fit: cover;
}
</style>
