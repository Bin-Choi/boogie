<template>
  <div>
    <h5 class="fw-bold p-3" style="text-align: left">네이버 블로그 검색결과</h5>
    <div class="search-naver-list px-3 mb-3">
      <SearchNaverListItem
        v-for="(blog, index) in searchList"
        :key="index"
        :blog="blog" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchNaverListItem from '@/components/SearchNaverListItem.vue'

// const API_URL = "https://boogiee.site"

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
        url: `${this.API_URL}/movies/naver/${this.$route.params.query}+영화/`,
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

<style scoped>
.search-naver-list {
  max-height: 800px;
  margin-left: 10px;
  margin-right: 10px;
  overflow-x: visible;
  overflow-y: scroll;
}
.search-naver-list::-webkit-scrollbar {
  width: 15px; /*스크롤바의 너비*/
}

.search-naver-list::-webkit-scrollbar-thumb {
  background-color: rgb(171, 149, 192); /*스크롤바의 색상*/
  border-radius: 10px; /*스크롤바 라운드*/
}

.search-naver-list::-webkit-scrollbar-track {
  background-color: rgb(234, 215, 235); /*스크롤바 트랙 색상*/
  border-radius: 10px; /*스크롤바 트랙 라운드*/
  /* box-shadow: inset 0px 0px 5px rgba(0, 0, 0, 0.2); */
}
</style>
