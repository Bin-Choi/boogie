<template>
  <div id="movie_detail_info" class="text-start p-3">
    <h4 class="fw-bold">한줄평</h4>
    <hr />
    <ReviewListItem
      v-for="(review, index) in reviews"
      :key="index"
      :review="review" />
  </div>
</template>

<script>
import ReviewListItem from './ReviewListItem.vue'

export default {
  name: 'ReviewList',
  components: { ReviewListItem },
  computed: {
    reviews() {
      return this.$store.state.reviews
    },
    movie() {
      return this.$store.state.movie
    },
  },
  methods: {},
  created() {
    this.$store.dispatch('getReviews', this.$route.params.tmdb_id)
  },
}
</script>

<style>
#review_list {
  background-color: white;
}
</style>
