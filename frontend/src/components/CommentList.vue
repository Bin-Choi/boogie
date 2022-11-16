<template>
  <div class="comment-list">
    <h3>comment List</h3>
    <comment-list-item
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    />
  </div>
</template>

<script>
import CommentListItem from "./CommentListItem.vue"

export default {
  components: { CommentListItem },
  name: "CommentList",
  computed: {
    comments() {
      return this.$store.state.comments
    },
  },
}
</script>

<style></style>
