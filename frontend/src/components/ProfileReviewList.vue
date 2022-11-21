<template>
  <div>
    <p>내 리뷰</p>
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
}
</script>

<style></style>
