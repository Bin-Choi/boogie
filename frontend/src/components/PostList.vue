<template>
  <div>
    <h4>PostList</h4>
    <hr>
    <PostListItem v-for="(post, index) in posts" :key="index" :post="post" />
  </div>
</template>

<script>
import PostListItem from "./PostListItem.vue"

export default {
  name: "PostList",
  components: { PostListItem },
  computed: {
    posts() {
      return this.$store.state.posts
    }
  }
}
</script>

<style>

</style>