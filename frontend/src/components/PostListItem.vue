<template>
  <div class="post_item" style="cursor: pointer" @click.stop="toPostDetail">
    <p>
      {{ post.title }}
      <span class="username" @click.stop="toProfile">{{ post.username }}</span>
      | 좋아요:{{ post.like_users_count }}
    </p>
    <hr />
  </div>
</template>

<script>
export default {
  name: 'PostListItem',
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

<style>
.post_item:hover {
  background-color: ivory;
}
.username:hover {
  background-color: lightgrey;
}
</style>
