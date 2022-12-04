<template>
  <div
    id="movie_detail_info"
    class="text-start p-3"
    :class="darkMode ? 'box-dark' : 'box-light'">
    <h5 class="fw-bold">줄거리</h5>
    <p class="mt-3 overview">{{ movie.overview }}</p>
    <hr />
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

    darkMode() {
      return this.$store.state.darkMode
    },
  },
}
</script>

<style scoped>
.overview {
  height: 270px;
  overflow-y: auto;
}
.overview::-webkit-scrollbar {
  width: 15px; /*스크롤바의 너비*/
}

.overview::-webkit-scrollbar-thumb {
  background-color: rgb(171, 149, 192); /*스크롤바의 색상*/
  border-radius: 10px; /*스크롤바 라운드*/
}

.overview::-webkit-scrollbar-track {
  background-color: rgb(234, 215, 235); /*스크롤바 트랙 색상*/
  border-radius: 10px; /*스크롤바 트랙 라운드*/
  /* box-shadow: inset 0px 0px 5px rgba(0, 0, 0, 0.2); */
}
</style>
