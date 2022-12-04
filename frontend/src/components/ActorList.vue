<template>
  <div style="height: 204px">
    <h5 class="fw-bold">출연진</h5>
    <div class="d-flex actor-list">
      <ActorListItem
        class="mt-1"
        v-for="actor in actors"
        :actor="actor"
        :key="actor.name"
        style="margin-right: 30px" />
    </div>
  </div>
</template>

<script>
import ActorListItem from '@/components/ActorListItem.vue'

export default {
  name: 'ActorList',
  components: {
    ActorListItem,
  },
  computed: {
    movie() {
      return this.$store.state.movie
    },
    actors() {
      return this.movie.directors.concat(this.movie.actors)
    },
  },
}
</script>

<style scoped>
.actor-list {
  margin-left: 10px;
  margin-right: 10px;
  overflow-x: scroll;
}
.actor-list::-webkit-scrollbar {
  height: 15px; /*스크롤바의 너비*/
}

.actor-list::-webkit-scrollbar-thumb {
  background-color: rgb(171, 149, 192); /*스크롤바의 색상*/
  border-radius: 10px; /*스크롤바 라운드*/
}

.actor-list::-webkit-scrollbar-track {
  background-color: rgb(234, 215, 235); /*스크롤바 트랙 색상*/
  border-radius: 10px; /*스크롤바 트랙 라운드*/
  /* box-shadow: inset 0px 0px 5px rgba(0, 0, 0, 0.2); */
}
</style>
