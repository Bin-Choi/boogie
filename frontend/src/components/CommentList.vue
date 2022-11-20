<template>
  <div class="comment-list">
    <h3>comment List</h3>
    <hr />
    <CommentListItem
      v-for="comments in orderedComments"
      :key="comments[0].id"
      :comments="comments"
      :selectedComment="selectedComment"
      @get_comments="getComments"
      @select_comment="selectComment"
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
      orderedComments: null,
      selectedComment: null,
    }
  },
  created() {
    this.getComments()
  },
  methods: {
    getComments() {
      axios({
        method: 'get',
        url: `${API_URL}/community/posts/${this.$route.params.postId}/comments/`,
      })
        .then((res) => {
          const comments = res.data
          // 댓글 정렬
          let i = 0
          let commentsRef = {}
          let orderedComments = []
          comments.forEach((comment) => {
            if (comment.original_comment === null) {
              commentsRef[comment.id] = i
              orderedComments.push([comment])
              i += 1
            } else {
              orderedComments[commentsRef[comment.original_comment]].push(
                comment
              )
            }
          })
          this.orderedComments = orderedComments
        })
        .catch((err) => {
          console.log(err)
        })
    },
    selectComment(commentId) {
      this.selectedComment = commentId
    },
  },
}
</script>

<style></style>
