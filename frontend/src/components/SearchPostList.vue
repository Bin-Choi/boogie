<template>
  <div class="pb-3">
    <h5 class="fw-bold p-3" style="text-align: left">게시판 검색결과</h5>
    <SearchPostListItem
      v-for="(post, index) in searchList"
      :key="index"
      :post="post" />
  </div>
</template>

<script>
import SearchPostListItem from '@/components/SearchPostListItem.vue'
import axios from 'axios'

// const API_URL = "https://boogiee.site"

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
  computed: {
    API_URL() {
      return this.$store.state.API_URL
    },
  },
  watch: {
    $route() {
      this.getSearchList()
    },
  },
  created() {
    this.getSearchList()
  },
  methods: {
    getSearchList() {
      axios({
        method: 'get',
        url: `${this.API_URL}/community/posts/search/${this.$route.params.query}/`,
      })
        .then((res) => {
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
