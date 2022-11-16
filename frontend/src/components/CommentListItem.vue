<template>
  <div>
    <h3>{{ comment.content }}</h3>
  </div>
</template>

<script>
export default {
  name: "CommentListItem",
  props: {
    comment: Object,
  },
}
</script>

<style></style>
