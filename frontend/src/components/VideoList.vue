<template>
  <div>
    <h3>{{movie?.title}}</h3>
    <ul>
      <VideoListItem v-for="(video, index) in videoList" :key = "index" :video="video" @play="play"/>
    </ul>
  </div>
</template>

<script>
import VideoListItem from './VideoListItem.vue';
import axios from 'axios'

export default {
  name: "VideoList",
  components: {
    VideoListItem,
  },
  props: {
    movie: Object,
  },
  data() {
    return {
      videoList: [],
    }
  },
  methods: {
    getVideoList(){
      const title = this.movie.title
      const params = {
        key: 'AIzaSyAqe-pKnjEB4hsDDn8Cjmge-OVYOb_aZ7w',
        part: 'snippet',
        type: 'video',
        q: title
      }
      axios({
        method: 'get',
        url: 'https://www.googleapis.com/youtube/v3/search',
        params
      })
      .then((res) => {
        this.videoList = res.data.items.slice((0,4))
        // this.videoList = res.data.items
      })
      .catch((err) => {
        console.log(err)
      })
    },
    play(video){
      this.video = video
    }
  },
  created() {
    this.getVideoList()
  },
}
</script>

<style></style>
