<template>
  <div class="p-3" :class="darkMode ? 'box-dark' : 'box-light'">
    <h5 class="fw-bold">글 &#128077;</h5>
    <ProfileLikePostListItem
      v-for="post in posts"
      :key="`my-${post.id}`"
      :post="post" />
  </div>
</template>

<script>
import ProfileLikePostListItem from '@/components/ProfileLikePostListItem.vue'
export default {
  name: 'ProfilePostList',
  components: {
    ProfileLikePostListItem,
  },
  props: {
    posts: Array,
    postTitle: String,
  },
  computed: {
    darkMode() {
      return this.$store.state.darkMode
    },
  },
}
</script>

<style></style>
