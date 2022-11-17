<template>
  <div>
    <h4 class="fw-bold">출연진</h4>
    <div class="d-flex" style="margin-left: 10px">
      <ActorListItem
        v-for="actor in actors"
        :actor="actor"
        :key="actor.name"
        style="margin-right: 30px"
      />
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
      return this.movie.directors.concat(this.movie.actors).slice(0, 5)
    },
  },
}
</script>

<style></style>
