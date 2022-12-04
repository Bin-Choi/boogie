<template>
  <div
    class="container justify-content-between p-2 review_item"
    @click.stop="toMovieDetail"
    style="cursor: pointer; height: 40px">
    <div class="row">
      <div class="col-4 fw-bold" style="text-align: left; white-space: nowrap">
        {{ review.movie_title }}
      </div>
      <div class="col-3" style="text-align: left">
        <img :src="starsPath" style="width: 100%" />
      </div>
      <div
        class="col-4"
        style="text-align: left; white-space: nowrap; overflow: hidden">
        {{ review.content }}
      </div>
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
