<template>
  <div class="p-3" :class="darkMode ? 'box-dark' : 'box-light'">
    <h5 class="fw-bold">HOT 게시글</h5>
    <hr />
    <HotPostListItem v-for="post in hotPosts" :key="post.id" :post="post" />
  </div>
</template>

<script>
import HotPostListItem from '@/components/HotPostListItem'
import axios from 'axios'

// const API_URL = 'https://boogiee.site'

export default {
  name: 'HotPostList',
  components: { HotPostListItem },
  data() {
    return {
      hotPosts: [],
    }
  },
  computed: {
    API_URL() {
      return this.$store.state.API_URL
    },
    darkMode() {
      return this.$store.state.darkMode
    },
  },
  created() {
    this.getHotPosts()
  },
  methods: {
    getHotPosts() {
      axios({
        method: 'get',
        url: `${this.API_URL}/community/posts/hot/`,
      })
        .then((res) => {
          this.hotPosts = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
