<template>
  <div>
    <h4>PostList</h4>
    <hr />
    <PostListItem v-for="post in posts" :key="post.id" :post="post" />
  </div>
</template>

<script>
import PostListItem from './PostListItem.vue'

export default {
  name: 'PostList',
  components: { PostListItem },
  computed: {
    posts() {
      return this.$store.state.posts
    },
  },
}
</script>

<style></style>
