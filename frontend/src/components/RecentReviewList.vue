<template>
  <div class="p-3" :class="darkMode ? 'box-dark' : 'box-light'">
    <h5 class="fw-bold">최근 리뷰</h5>
    <hr />
    <RecentReviewListItem
      v-for="review in recentReviews"
      :key="review.id"
      :review="review" />
  </div>
</template>

<script>
import RecentReviewListItem from './RecentReviewListItem.vue'
import axios from 'axios'

// const API_URL = 'https://boogiee.site'

export default {
  components: { RecentReviewListItem },
  name: 'RecentReviewList',
  data() {
    return {
      recentReviews: [],
    }
  },
  computed: {
    API_URL() {
      return this.$store.state.API_URL
    },
    darkMode() {
      return this.$store.state.darkMode
    },
  },
  created() {
    this.getRecentReviews()
  },
  methods: {
    getRecentReviews() {
      axios({
        method: 'get',
        url: `${this.API_URL}/movies/reviews/recent/`,
      })
        .then((res) => {
          this.recentReviews = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
