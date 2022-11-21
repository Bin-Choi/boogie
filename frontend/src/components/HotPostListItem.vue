<template>
  <div
    class="d-flex justify-content-between mt-3"
    @click="toPostDetail"
    style="cursor: pointer"
  >
    <div>
      <span>{{ post.title }}</span>
    </div>
    <span style="color: gray">{{ post.username }}</span>
  </div>
</template>

<script>
export default {
  name: 'HotPostListItem',
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
