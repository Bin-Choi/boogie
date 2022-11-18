<template>
  <div>
    <h4>최 근 리 뷰</h4>
    <hr />
    <RecentReviewListItem
      v-for="review in recentReviews"
      :key="review.id"
      :review="review"
    />
  </div>
</template>

<script>
import RecentReviewListItem from "./RecentReviewListItem.vue"

export default {
  components: { RecentReviewListItem },
  name: "RecentReviewList",

  computed: {
    recentReviews() {
      return this.$store.state.recentreviews
    },
  },
  created() {
    this.$store.dispatch("getRecentReviews")
  },
  methods: {},
}
</script>

<style></style>
