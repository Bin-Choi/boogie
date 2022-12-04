<template>
  <div class="p-3" :class="darkMode ? 'box-dark' : 'box-light'">
    <h5 class="fw-bold">내 리뷰</h5>
    <ProfileReviewListItem
      v-for="review in myReviews"
      :key="`review-${review.id}`"
      :review="review"
    />
  </div>
</template>

<script>
import ProfileReviewListItem from '@/components/ProfileReviewListItem.vue'
export default {
  name: 'ProfileReviewList',
  components: {
    ProfileReviewListItem,
  },
  props: {
    myReviews: Array,
  },
  computed: {
    darkMode() {
      return this.$store.state.darkMode
    },
  },
}
</script>

<style></style>
