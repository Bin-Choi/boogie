<template>
  <div>
    <div class="home">
      <img alt="Vue logo" src="../assets/logo.png" />
    </div>
    <hr />
    <div>
      <RecentReviewList />
    </div>
    <div>
      <HotPostList />
    </div>
    <div>
      <NowMovieList />
    </div>
    <div>
      <BoxOffice />
    </div>
  </div>
</template>

<script>
import RecentReviewList from '@/components/RecentReviewList.vue'
import NowMovieList from '@/components/NowMovieList.vue'
import BoxOffice from '@/components/BoxOffice.vue'
import HotPostList from '@/components/HotPostList.vue'

export default {
  name: 'IndexView',
  components: {
    RecentReviewList,
    NowMovieList,
    BoxOffice,
    HotPostList,
  },
}
</script>
