<template>
  <div>
    <h5>네이버</h5>
    <hr />
    <SearchNaverListItem
      v-for="(blog, index) in searchList"
      :key="index"
      :blog="blog"
    />
  </div>
</template>

<script>
import axios from 'axios'
import SearchNaverListItem from '@/components/SearchNaverListItem.vue'
const API = 'http://127.0.0.1:8000'

export default {
  name: 'SearchNaverList',
  components: {
    SearchNaverListItem,
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
        url: `${API}/movies/naver/${this.$route.params.query}/`,
      })
        .then((res) => {
          this.searchList = res.data.items
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
