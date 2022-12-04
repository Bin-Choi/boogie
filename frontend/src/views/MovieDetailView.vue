<template>
  <div>
    <div id="movie_detail_backdrop">
      <img :src="backdrop_url" />
    </div>
    <div v-if="movie">
      <MovieDetailHeader />
      <div class="container" style="max-width: 1200px">
        <div class="row justify-content-center">
          <div
            class="col-12 col-lg-6 d-flex flex-column mt-3"
            style="height: 844px">
            <MovieDetailInfo style="height: 574px" />
            <ReviewList style="margin-top: 15px; height: 255px" />
          </div>
          <div class="col-12 col-lg-3 mt-3">
            <VideoList class="video-list" />
          </div>
        </div>
        <div class="row justify-content-center">
          <div class="col-12 col-lg-9">
            <RelatedMovieList style="max-width: 1200px" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieDetailHeader from '@/components/MovieDetailHeader.vue'
import MovieDetailInfo from '@/components/MovieDetailInfo.vue'
import RelatedMovieList from '@/components/RelatedMovieList.vue'
import ReviewList from '@/components/ReviewList.vue'
import VideoList from '@/components/VideoList.vue'

export default {
  name: 'DetailView',
  components: {
    MovieDetailHeader,
    MovieDetailInfo,
    ReviewList,
    VideoList,
    RelatedMovieList,
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
    this.getMovie(this.$route.params.movieId)
  },
  methods: {
    getMovie(movieId) {
      this.$store.dispatch('getMovie', movieId)
    },
  },
  beforeRouteUpdate(to, from, next) {
    this.getMovie(to.params.movieId)
    next()
  },
}
</script>

<style scoped>
@media (min-width: 992px) {
  .video-list {
    height: 844px;
  }
}

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
