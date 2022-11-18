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
      <NowMovieList />
    </div>
  </div>
</template>

<script>
import RecentReviewList from "../components/RecentReviewList.vue"
import NowMovieList from "../components/NowMovieList.vue"

export default {
  name: "IndexView",
  components: { RecentReviewList, NowMovieList },
}
</script>
