<template>
  <div>
    <h5>게 시 판</h5>
    <hr />
    <SearchPostListItem
      v-for="(post, index) in searchList"
      :key="index"
      :post="post"
    />
  </div>
</template>

<script>
import SearchPostListItem from '@/components/SearchPostListItem.vue'
import axios from 'axios'

const URL = 'http://127.0.0.1:8000'

export default {
  name: 'SearchPostList',
  components: {
    SearchPostListItem,
  },
  data() {
    return {
      searchList: [],
    }
  },
  created() {
    this.getSearchList()
  },
  methods: {
    getSearchList() {
      axios({
        method: 'get',
        url: `${URL}/community/posts/search/${this.$route.params.query}/`,
      })
        .then((res) => {
          console.log(res)
          this.searchList = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
