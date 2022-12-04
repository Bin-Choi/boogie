<template>
  <div
    class="post_item d-flex p-1 align-items-center"
    style="cursor: pointer; height: 40px"
    @click.stop="toPostDetail">
    <div class="col-8 fw-bold" style="text-align: left">
      <span>{{ post.title }}</span>
    </div>
    <div class="col-2 username" @click.stop="toProfile">
      {{ post.username }}
    </div>
    <div class="col-2">&#10084; {{ post.like_users_count }}</div>
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
    toProfile() {
      this.$router
        .push({
          name: 'profile',
          params: { username: this.post.username },
        })
        .catch(() => {})
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
.username {
  color: gray;
}
.username:hover {
  background-color: rgb(194, 194, 194);
  border-radius: 3px;
}
</style>
