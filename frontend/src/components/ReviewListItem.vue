<template>
  <div class="d-flex justify-content-between mt-3">
    <div>
      <img :src="starsPath" style="width: 120px" />
      <span class="fs-6" style="margin-left: 20px">{{ review.content }}</span>
    </div>
    <span class="username" style="color: gray" @click.stop="toProfile">{{
      review.username
    }}</span>
  </div>
</template>

<script>
export default {
  name: 'ReviewListItem',
  props: {
    review: Object,
  },
  computed: {
    starsPath() {
      return require(`@/assets/stars_${this.review.vote}.png`)
    },
  },
  methods: {
    toProfile() {
      this.$router
        .push({
          name: 'profile',
          params: { username: this.review.username },
        })
        .catch(() => {})
    },
  },
}
</script>

<style scoped>
.username:hover {
  cursor: pointer;
  background-color: lightgrey;
}
</style>
