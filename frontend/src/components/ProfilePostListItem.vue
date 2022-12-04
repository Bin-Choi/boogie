<template>
  <div
    class="post_item d-flex p-1"
    style="cursor: pointer"
    @click.stop="toPostDetail">
    <div class="col-1">
      <span>{{ post.id }}</span>
    </div>
    <div class="col-7" style="text-align: left">
      <span>{{ post.title }}</span>
    </div>
    <div class="col-2">
      {{ createdAt }}
    </div>
    <div class="col-2">&#10084; {{ post.like_users_count }}</div>
  </div>
</template>

<script>
export default {
  name: 'PostListItem',
  props: {
    post: Object,
  },
  computed: {
    createdAt() {
      return new Date(this.post?.created_at).toLocaleDateString()
    },
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

<style scoped>
.post_item:hover {
  transition: transform 0.2s linear;
}

.post_item:hover {
  transform: scale(1.05);
  background-color: rgba(219, 219, 219, 0.459);
  border-radius: 10px;
}
</style>
