<template>
  <div>
    <div>
      <NowMovieList />
    </div>
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-12 col-lg-5 mt-3">
          <HotPostList />
        </div>
        <div class="col-12 col-lg-5 mt-3">
          <RecentReviewList />
        </div>
      </div>
      <div class="row justify-content-center">
        <div class="col-12 col-lg-10 mt-3">
          <RecoMovieList />
        </div>
      </div>
      <div class="row justify-content-center">
        <div class="col-12 col-lg-10 mt-3">
          <BoxOffice />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import RecentReviewList from '@/components/RecentReviewList.vue'
import NowMovieList from '@/components/NowMovieList.vue'
import HotPostList from '@/components/HotPostList.vue'
import RecoMovieList from '@/components/RecoMovieList.vue'
import BoxOffice from '@/components/BoxOffice.vue'

export default {
  name: 'IndexView',
  components: {
    RecentReviewList,
    NowMovieList,
    HotPostList,
    RecoMovieList,
    BoxOffice,
  },
  computed: {
    darkMode() {
      return this.$store.state.darkMode
    },
  },
}
</script>
