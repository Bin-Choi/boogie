<template>
  <div id="movie_detail_info" class="text-start p-3">
    <h4 class="fw-bold">한줄평</h4>
    <hr />
    <ReviewListItem
      v-for="review in reviews"
      :key="review.id"
      :review="review" />
  </div>
</template>

<script>
import ReviewListItem from './ReviewListItem.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewList',
  components: { ReviewListItem },
  data() {
    return {
      reviews: null,
    }
  },
  computed: {
    movie() {
      return this.$store.state.movie
    },
    user() {
      return this.$store.state.user
    },
  },
  created() {
    this.getReviews(this.$route.params.movieId)
  },
  methods: {
    getReviews(movieId) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${movieId}/reviews/`, // token이 없을 때는 보내면 안됨
      })
        .then((res) => {
          const reviews = res.data
          for (let i = 0; i < reviews.length; i++) {
            if (reviews[i].username === this.user?.username) {
              reviews.splice(i, 1)
              break
            }
          }
          this.reviews = reviews
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style>
#review_list {
  background-color: white;
}
</style>
