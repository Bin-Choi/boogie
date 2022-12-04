<template>
  <span class="ms-1 me-1">
    <iframe
      id="player"
      width="100%"
      style="max-width: 250px"
      :src="videoURL"
      frameborder="0"
      allowfullscreen></iframe>
  </span>
</template>

<script>
// import $ from 'jequery';

export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },

  methods: {
    play() {
      this.$emit('play', this.video)
    },
    openlayer() {
      let path = this.attr('href')
      this.cont.append(this.embed)
      path.show()
      this.dim.show()
    },
  },
  computed: {
    videoURL() {
      return 'https://www.youtube.com/embed/' + this.video.id.videoId
    },
  },
}
</script>

<style></style>
