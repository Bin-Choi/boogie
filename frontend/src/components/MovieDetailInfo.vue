<template>
  <div>
    <h4>줄거리</h4>
    <p>{{ movie.overview }}</p>
  </div>
</template>

<script>

export default {
  name: "MovieDetailInfo",
  props: {
    movie: Object,
  }

}
</script>

<style>
</style>
