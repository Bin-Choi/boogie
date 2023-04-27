<template>
  <div class="now-showing px-5 py-3">
    <h1 class="fw-bold my-4" style="color: #ffffffde; font-size: 50px">
      NOW SHOWING
    </h1>
    <carousel
      :autoplay="true"
      :autoplay-timeout="2300"
      :autoplay-hover-pause="true"
      :center-mode="true"
      :loop="true"
      :per-page="1"
      :per-page-custom="[
        [425, 2],
        [768, 3],
        [1024, 5],
      ]"
      :pagination-active-color="`#ffffff`"
      :pagination-color="`#545454`"
      :pagination-position="`bottom-overlay`"
      ref="carousel">
      <slide v-for="(movie, i) in nowMovies" :index="i" :key="movie.id">
        <NowMovieListItem :movie="movie" />
      </slide>
    </carousel>
  </div>
</template>

<script>
// import { Carousel3d, Slide } from 'vue-carousel-3d'
import { Carousel, Slide } from 'vue-carousel'
import NowMovieListItem from '@/components/NowMovieListItem.vue'
import axios from 'axios'

// const API_URL = "https://boogiee.site"

export default {
  name: 'NowMovieList',
  components: {
    NowMovieListItem,
    // Carousel3d,
    // Slide,
    Carousel,
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
