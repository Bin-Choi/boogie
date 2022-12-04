<template>
  <div class="p-3" :class="darkMode ? 'box-dark' : 'box-light'">
    <h5 class="fw-bold">내가 작성한 글</h5>
    <ProfilePostListItem
      v-for="post in posts"
      :key="`my-${post.id}`"
      :post="post"
    />
  </div>
</template>

<script>
import ProfilePostListItem from '@/components/ProfilePostListItem.vue'
export default {
  name: 'ProfilePostList',
  components: {
    ProfilePostListItem,
  },
  props: {
    posts: Array,
  },
  computed: {
    darkMode() {
      return this.$store.state.darkMode
    },
  },
}
</script>

<style></style>
