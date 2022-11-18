<template>
  <div class="comment-list">
    <h3>comment List</h3>
    <hr />
    <CommentListItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
      @get_comments="getComments"
      class="text-start" />
    <CommentForm @get_comments="getComments" />
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'
import CommentForm from '@/components/CommentForm.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  components: { CommentListItem, CommentForm },
  name: 'CommentList',
  data() {
    return {
      comments: null,
    }
  },
  created() {
    this.getComments()
  },
  methods: {
    getComments() {
      axios({
        method: 'get',
        url: `${API_URL}/community/comments/post/${this.$route.params.post_pk}/`,
        // headers: {
        //   Authorization: `Token ${context.state.token}`
        // }
      })
        .then((res) => {
          this.comments = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
