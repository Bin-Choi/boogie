<template>
  <div>
    <div v-if="movie">
      <MovieDetailHeader :movie="movie"/>
      <div class="container">
        <div class="row">>
          <div class="col-8">
            <MovieDetailInfo :movie="movie"/>
            <ReviewList />
          </div>
          <div class="col-4">
            <VideoList :movie="movie"/>
          </div>
        </div>
      </div>
      <RecoMovieList />
    </div>
  </div>
</template>

<script>
import MovieDetailHeader from "@/components/MovieDetailHeader.vue"
import MovieDetailInfo from "@/components/MovieDetailInfo.vue"
import RecoMovieList from "@/components/RecoMovieList.vue"
import ReviewList from "@/components/ReviewList.vue"
import VideoList from "@/components/VideoList.vue"

import axios from "axios"
const LOCAL_URL = 'http://127.0.0.1:8000/'

export default {
  name: "DetailView",
  components: {
    MovieDetailHeader,
    MovieDetailInfo,
    ReviewList,
    VideoList,
    RecoMovieList,
  },
  data() {
    return {
      movie: null,
    }
  },
  methods: {
    getMovie() {
      axios({
        url: LOCAL_URL + `movies/detail/${this.$route.params.tmdb_id}`,
        method: 'get',
      })
        .then((response) => {
          this.movie = response.data
        })
        .catch((error) => console.log(error))
    },
    
  },
  created() {
    this.getMovie()
  },
}
</script>
