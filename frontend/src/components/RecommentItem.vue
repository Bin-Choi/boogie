<template>
  <div class="ms-5 d-flex justify-content-between py-2">
    <div>
      <span>↳ </span><span class="fw-bold"> {{ recomment.username }}</span>
      <span class="ms-3">{{ recomment.content }}</span>
    </div>
    <div
      v-if="recomment.user === user?.id"
      class="delete d-inline-block ms-4 me-3"
      @click="deleteComment">
      <img :src="require('@/assets/trashcan.png')" alt="" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'

// const API_URL = "https://boogiee.site"

export default {
  name: 'RecommentItem',
  props: {
    recomment: Object,
  },
  computed: {
    API_URL() {
      return this.$store.state.API_URL
    },
    user() {
      return this.$store.state.user
    },
  },
  methods: {
    deleteComment() {
      axios({
        method: 'delete',
        url: `${this.API_URL}/community/posts/${this.$route.params.postId}/comments/${this.recomment.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          this.$emit('get_comments')
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style scoped>
.delete {
  cursor: pointer;
  width: 20px;
  height: 20px;
}

.delete img {
  width: 100%;
  filter: opacity(0.85) drop-shadow(0 0 0 white);
}
</style>
