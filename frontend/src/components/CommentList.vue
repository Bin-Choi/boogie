<template>
  <div class="comment-list">
    <div class="ms-4 my-2">
      <p class="fw-bold" style="text-align: left; font-size: 17px">댓글 목록</p>
    </div>
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

// const API_URL = "https://boogiee.site"

export default {
  components: { CommentListItem, CommentForm },
  name: 'CommentList',
  data() {
    return {
      orderedComments: null,
      selectedComment: null,
    }
  },
  computed: {
    API_URL() {
      return this.$store.state.API_URL
    },
  },
  created() {
    this.getComments()
  },
  methods: {
    getComments() {
      axios({
        method: 'get',
        url: `${this.API_URL}/community/posts/${this.$route.params.postId}/comments/`,
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

<style scoped>
hr {
  margin-left: 7px;
  margin-right: 7px;
  margin-top: 0.04rem;
  margin-bottom: 0.04rem;
}
</style>
