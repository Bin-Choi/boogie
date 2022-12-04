<template>
  <div
    class="d-flex justify-content-between p-2 review_item"
    @click.stop="toMovieDetail"
    style="cursor: pointer">
    <div class="col-2 fw-bold" style="text-align: left">
      {{ review.movie_title }}
    </div>
    <div class="col-2" style="text-align: left">
      <img :src="starsPath" style="width: 100%" />
    </div>
    <div class="col-5" style="text-align: left">
      {{ review.content }}
    </div>
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
  },
}
</script>

<style scoped>
.review_item:hover {
  transition: transform 0.2s linear;
}

.review_item:hover {
  transform: scale(1.05);
  background-color: rgba(219, 219, 219, 0.459);
  border-radius: 10px;
}
.username:hover {
  background-color: rgb(194, 194, 194);
  border-radius: 3px;
}
</style>
