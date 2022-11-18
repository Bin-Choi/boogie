<template>
  <div>
    <p>{{ review.content }}</p>
    <hr />
  </div>
</template>

<script>
export default {
  name: "RecentReviewListItem",
  props: {
    review: Object,
  },
}
</script>

<style></style>
