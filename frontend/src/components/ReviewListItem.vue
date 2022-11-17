<template>
  <div
    @mouseenter="hover = !hover"
    @mouseleave="hover = !hover"
    class="d-flex justify-content-between mt-3">
    <div>
      <img :src="starsPath" style="width: 150px" />
      <span class="fs-6 fw-bold" style="margin-left: 20px">{{
        review.content
      }}</span>
    </div>
    <span style="color: gray">{{ review.username }}</span>
    <button
      v-if="hover"
      type="button"
      class="btn btn-danger"
      @click="deleteReview">
      X
    </button>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewListItem',
  props: {
    review: Object,
  },
  data() {
    return {
      hover: false,
    }
  },
  computed: {
    starsPath() {
      return require(`@/assets/stars_${this.review.vote}.png`)
    },
  },
  methods: {
    over() {
      this.hover = true
    },
    out() {
      this.hover = false
    },
    deleteReview() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/reviews/${this.review.id}/`,
      })
        .then(() => {
          this.$store.dispatch('getReviews', this.$route.params.tmdb_id)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
