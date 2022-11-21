<template>
  <div
    class="d-flex justify-content-between mt-3"
    @click.stop="toMovieDetail"
    style="cursor: pointer"
  >
    <div>
      <span>{{ review.movie_title }}</span>
      <img :src="starsPath" style="width: 150px" />
      <span class="fs-6 fw-bold" style="margin-left: 20px">{{
        review.content
      }}</span>
    </div>
    <span style="color: gray" @click.stop="toProfile">{{
      review.username
    }}</span>
  </div>
</template>

<script>
export default {
  name: 'RecentReviewListItem',
  props: {
    review: Object,
  },
  computed: {
    starsPath() {
      return require(`@/assets/stars_${this.review.vote}.png`)
    },
  },
  methods: {
    toMovieDetail() {
      this.$router.push({
        name: 'movieDetail',
        params: { movieId: this.review.movie },
      })
    },
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

<style></style>
