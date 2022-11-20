<template>
  <div>
    <span>{{ recomment.username }} : {{ recomment.content }}</span>
    <button
      v-if="recomment.user === user.id"
      type="button"
      class="btn btn-danger"
      @click="deleteComment">
      X
    </button>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'RecommentItem',
  props: {
    recomment: Object,
  },
  computed: {
    user() {
      return this.$store.state.user
    },
  },
  methods: {
    deleteComment() {
      axios({
        method: 'delete',
        url: `${API_URL}/community/posts/${this.$route.params.postId}/comments/${this.recomment.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          this.$emit('get_comments')
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
