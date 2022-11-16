<template>
  <div>
    <h4>한줄평</h4>
    <ReviewListItem v-for="(review, index) in reviews" :key="index" :review="review"/>
  </div>
</template>

<script>
import ReviewListItem from "./ReviewListItem.vue"

export default {
  name: "ReviewList",
  components: { ReviewListItem },
  data() {
    return {
      reviews: []
    }
  }
}
</script>

<style></style>
