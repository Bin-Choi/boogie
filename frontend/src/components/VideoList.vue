<template>
  <div :class="darkMode ? 'box-dark' : 'box-light'" class="p-3">
    <h5 class="fw-bold">예고편</h5>
    <div class="video-list">
      <VideoListItem
        v-for="(video, index) in videoList"
        :key="index"
        :video="video" />
    </div>
  </div>
</template>

<script>
import VideoListItem from './VideoListItem.vue'
import axios from 'axios'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  data() {
    return {
      videoList: [],
    }
  },
  computed: {
    API_URL() {
      return this.$store.state.API_URL
    },
    movie() {
      return this.$store.state.movie
    },
    darkMode() {
      return this.$store.state.darkMode
    },
  },
  watch: {
    movie() {
      this.getVideoList()
    },
  },
  created() {
    this.getVideoList()
  },
  methods: {
    getVideoList() {
      axios({
        method: 'get',
        url: `${this.API_URL}/movies/${this.movie.title}/videos/`,
      })
        .then((res) => {
          this.videoList = res.data.items
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
