<template>
  <div class="col-11 col-lg-8 mx-auto mt-3">
    <h4 class="fw-bold" :class="darkMode ? 'font-white' : 'font-black'">
      '{{ $route.params.query }}' 검색결과
    </h4>
    <div class="mt-3" :class="darkMode ? 'box-dark' : 'box-light'">
      <SearchMovieList />
    </div>
    <!-- <게시글 django in> -->
    <div class="mt-3" :class="darkMode ? 'box-dark' : 'box-light'">
      <SearchPostList />
    </div>

    <!-- <네이버 API> -->
    <div class="mt-3" :class="darkMode ? 'box-dark' : 'box-light'">
      <SearchNaver />
    </div>
  </div>
</template>

<script>
import SearchMovieList from '@/components/SearchMovieList.vue'
import SearchNaver from '@/components/SearchNaverList.vue'
import SearchPostList from '@/components/SearchPostList.vue'

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
  computed: {
    darkMode() {
      return this.$store.state.darkMode
    },
  },
}
</script>

<style></style>
