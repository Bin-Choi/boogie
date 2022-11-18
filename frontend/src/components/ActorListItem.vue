<template>
  <div>
    <div id="profile_box">
      <img :src="profile_path" />
    </div>
    <p class="fw-bold text-center">{{ actor.name }}</p>
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
}
</script>

<style>
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
