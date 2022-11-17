<template>
  <div id="movie_detail_info" class="text-start p-3">
    <h4 class="fw-bold">줄거리</h4>
    <p class="mt-3">{{ movie.overview }}</p>
    <ActorList />
  </div>
</template>

<script>
import ActorList from '@/components/ActorList.vue'

export default {
  name: 'MovieDetailInfo',
  components: {
    ActorList,
  },
  computed: {
    movie() {
      return this.$store.state.movie
    },
  },
}
</script>

<style>
#movie_detail_info {
  background-color: white;
}
</style>
