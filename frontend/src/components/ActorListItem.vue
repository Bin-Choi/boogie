<template>
  <div style="cursor: pointer" @click="searchActor">
    <div id="profile_box">
      <img :src="profile_path" />
    </div>
    <p class="text-center" style="font-size: 15px">{{ actor.name }}</p>
  </div>
</template>

<script>
export default {
  name: 'ActorListItem',
  props: {
    actor: Object,
  },
  computed: {
    profile_path() {
      if (this.actor.profile_path) {
        return `https://image.tmdb.org/t/p/original${this.actor.profile_path}`
      } else {
        return require('@/assets/actor_default_profile.png')
      }
    },
  },
  methods: {
    searchActor() {
      window.open(`https://www.google.com/search?q=${this.actor.name}`)
    },
  },
}
</script>

<style scoped>
#profile_box {
  width: 70px;
  height: 70px;
  border-radius: 70%;
  overflow: hidden;
}

#profile_box img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
