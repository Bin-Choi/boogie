<template>
  <div>
    <h5>[HOT] 뜨거웡</h5>
    <hr />
    <HotPostListItem v-for="post in hotPosts" :key="post.id" :post="post" />
  </div>
</template>

<script>
import HotPostListItem from '@/components/HotPostListItem'
import axios from 'axios'

const API = 'http://127.0.0.1:8000'

export default {
  name: 'HotPostList',
  components: { HotPostListItem },
  data() {
    return {
      hotPosts: [],
    }
  },
  created() {
    this.getHotPosts()
  },
  methods: {
    getHotPosts() {
      axios({
        method: 'get',
        url: `${API}/community/posts/hot/`,
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
