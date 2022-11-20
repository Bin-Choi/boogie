<template>
  <div>
    <h4>최 근 리 뷰</h4>
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

const API = 'http://127.0.0.1:8000'

export default {
  components: { RecentReviewListItem },
  name: 'RecentReviewList',
  data() {
    return {
      recentReviews: [],
    }
  },
  created() {
    this.getRecentReviews()
  },
  methods: {
    getRecentReviews() {
      axios({
        method: 'get',
        url: `${API}/movies/reviews/recent/`,
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
