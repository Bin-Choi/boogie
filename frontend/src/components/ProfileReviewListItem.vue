<template>
  <div
    class="d-flex justify-content-between mt-3"
    @click="toMovieDetail"
    style="cursor: pointer">
    <div>
      <span>{{ review.movie_title }}</span>
      <img :src="starsPath" style="width: 150px" />
      <span class="fs-6 fw-bold" style="margin-left: 20px">{{
        review.content
      }}</span>
    </div>
    <span style="color: gray">{{ review.username }}</span>
  </div>
</template>

<script>
export default {
  name: 'ProfileReviewListItem',
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
  },
}
</script>

<style></style>
