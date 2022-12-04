<template>
  <div class="now-showing p-3">
    <h1 class="fw-bold" style="color: #ffffffde; font-size: 50px">
      NOW SHOWING
    </h1>
    <carousel-3d
      :autoplay="true"
      :autoplay-timeout="2300"
      :controls-visible="true"
      :controls-prev-html="'&#10092; '"
      :controls-next-html="'&#10093;'"
      :controls-width="30"
      :controls-height="60"
      :clickable="true"
      :space="300"
      :width="300"
      :height="420">
      <slide v-for="(movie, i) in nowMovies" :index="i" :key="movie.id">
        <NowMovieListItem :movie="movie" style="cursor: pointer" />
      </slide>
    </carousel-3d>
  </div>
</template>

<script>
import { Carousel3d, Slide } from 'vue-carousel-3d'
import NowMovieListItem from '@/components/NowMovieListItem.vue'
import axios from 'axios'

// const API_URL = "https://boogiee.site"

export default {
  name: 'NowMovieList',
  components: {
    NowMovieListItem,
    Carousel3d,
    Slide,
  },
  data() {
    return {
      nowMovies: [],
    }
  },
  computed: {
    API_URL() {
      return this.$store.state.API_URL
    },
  },
  created() {
    this.getNowMovies()
  },
  methods: {
    getNowMovies() {
      axios({
        method: 'get',
        url: `${this.API_URL}/movies/now/`,
      })
        .then((res) => {
          this.nowMovies = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style scoped>
.now-showing {
  background-image: url('../assets/gradation.png');
  background-size: cover;
}
</style>
