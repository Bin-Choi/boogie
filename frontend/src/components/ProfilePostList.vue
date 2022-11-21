<template>
  <div>
    <p>{{ postTitle }}</p>
    <ProfilePostListItem
      v-for="post in posts"
      :key="`my-${post.id}`"
      :post="post"
    />
  </div>
</template>

<script>
import ProfilePostListItem from '@/components/PostListItem.vue'
export default {
  name: 'ProfilePostList',
  components: {
    ProfilePostListItem,
  },
  props: {
    posts: Array,
    postTitle: String,
  },
}
</script>

<style></style>
