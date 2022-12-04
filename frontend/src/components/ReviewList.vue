<template>
  <div class="text-start p-3" :class="darkMode ? 'box-dark' : 'box-light'">
    <h5 class="fw-bold" style="height: 15px">한줄평</h5>
    <div class="review-list">
      <ReviewListItem
        v-for="review in reviews"
        :key="review.id"
        :review="review" />
    </div>
  </div>
</template>

<script>
import ReviewListItem from './ReviewListItem.vue'
import axios from 'axios'

// const API_URL = "https://boogiee.site"

export default {
  name: 'ReviewList',
  components: { ReviewListItem },
  data() {
    return {
      reviews: null,
    }
  },
  computed: {
    API_URL() {
      return this.$store.state.API_URL
    },
    movie() {
      return this.$store.state.movie
    },
    user() {
      return this.$store.state.user
    },
    darkMode() {
      return this.$store.state.darkMode
    },
  },
  watch: {
    $route() {
      this.getReviews(this.$route.params.movieId)
    },
  },
  created() {
    this.getReviews(this.$route.params.movieId)
  },
  methods: {
    getReviews(movieId) {
      axios({
        method: 'get',
        url: `${this.API_URL}/movies/${movieId}/reviews/`, // token이 없을 때는 보내면 안됨
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
.review-list {
  max-height: 90%;
  overflow-y: auto;
}
.review-list::-webkit-scrollbar {
  width: 15px; /*스크롤바의 너비*/
}

.review-list::-webkit-scrollbar-thumb {
  background-color: rgb(171, 149, 192); /*스크롤바의 색상*/
  border-radius: 10px; /*스크롤바 라운드*/
}

.review-list::-webkit-scrollbar-track {
  background-color: rgb(234, 215, 235); /*스크롤바 트랙 색상*/
  border-radius: 10px; /*스크롤바 트랙 라운드*/
  /* box-shadow: inset 0px 0px 5px rgba(0, 0, 0, 0.2); */
}
</style>
