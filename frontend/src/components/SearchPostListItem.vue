<template>
  <div @click="toPostDetail">
    <p>{{ post.title }}</p>
  </div>
</template>

<script>
export default {
  name: 'SearchPostListItem',
  props: {
    post: Object,
  },
  methods: {
    toPostDetail() {
      this.$router.push({
        name: 'postDetail',
        params: { postId: this.post.id },
      })
    },
  },
}
</script>

<style></style>
