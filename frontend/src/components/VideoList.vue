<template>
  <div id="video-list" class="p-3">
    <h4 class="fw-bold">예고편</h4>
    <VideoListItem
      v-for="(video, index) in videoList"
      :key="index"
      :video="video"
    />
  </div>
</template>

<script>
import VideoListItem from './VideoListItem.vue'
// import axios from 'axios'

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
    movie() {
      return this.$store.state.movie
    },
  },
  methods: {
    getVideoList() {
      // const params = {
      //   key: 'AIzaSyAf1G4zWkG8KhIs062j2OEModwcv_O_PZg',
      //   part: 'snippet',
      //   type: 'video',
      //   q: this.movie.title + '예고편',
      // }
      // axios({
      //   method: 'get',
      //   url: 'https://www.googleapis.com/youtube/v3/search',
      //   params,
      // })
      //   .then((res) => {
      //     this.videoList = res.data.items.slice(0, 3)
      //     // this.videoList = res.data.items
      //   })
      //   .catch((err) => {
      //     console.log(err)
      //   })
    },
  },
  created() {
    this.getVideoList()
  },
}
</script>

<style>
#video-list {
  background-color: white;
}
</style>
