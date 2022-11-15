<template>
  <div>
    <h1>detail</h1>
    <movie-detail />
    <review-form />
    <review-list />
    <video-list />
    <reco-movie-list />
  </div>
</template>

<script>
import RecoMovieList from "../components/RecoMovieList.vue"
import MovieDetail from "../components/MovieDetail.vue"
import ReviewForm from "../components/ReviewForm.vue"
import ReviewList from "../components/ReviewList.vue"
import VideoList from "../components/VideoList.vue"

export default {
  name: "DetailView",
  components: {
    MovieDetail,
    RecoMovieList,
    ReviewForm,
    ReviewList,
    VideoList,
  },
}
</script>
