<template>
  <div>
    <h1>Search</h1>
    <hr />
    <div>
      <SearchMovieList />
    </div>
    <!-- <게시글 django in> -->
    <div>
      <SearchPostList />
    </div>

    <!-- <네이버 API> -->
    <div>
      <SearchNaver />
    </div>
  </div>
</template>

<script>
import SearchMovieList from '@/components/SearchMovieList.vue'
import SearchNaver from '@/components/SearchNaverList.vue'
import SearchPostList from '@/components/SearchPostList.vue'

// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'SearchView',
  data() {
    return {
      searchMovies: [],
    }
  },
  components: {
    SearchMovieList,
    SearchNaver,
    SearchPostList,
  },
}
</script>

<style></style>
