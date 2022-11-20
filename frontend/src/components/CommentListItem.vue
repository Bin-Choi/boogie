<template>
  <div @mouseenter="hover = !hover" @mouseleave="hover = !hover">
    <span>{{ comment.username }} : {{ comment.content }}</span>
    <button v-if="hover" @click="selectComment">대댓글 작성</button>
    <button
      v-if="comment.user === user.id"
      type="button"
      class="btn btn-danger"
      @click="deleteComment">
      X
    </button>
    <div v-if="comment.id === selectedComment">
      <input type="text" v-model="content" @keyup.enter="createRecomment" />
      <button @click="createRecomment">작성</button>
    </div>
    <RecommentItem
      v-for="recomment in recomments"
      :key="recomment.id"
      :recomment="recomment"
      @get_comments="$emit('get_comments')"
      class="ms-3" />
  </div>
</template>

<script>
import RecommentItem from '@/components/RecommentItem.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentListItem',
  components: {
    RecommentItem,
  },
  props: {
    comments: Array,
    selectedComment: Number,
  },
  data() {
    return {
      hover: false,
      content: '',
    }
  },
  computed: {
    comment() {
      return this.comments[0]
    },
    recomments() {
      return this.comments.slice(1)
    },
    user() {
      return this.$store.state.user
    },
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  methods: {
    createRecomment() {
      if (!this.isLogin) {
        alert('로그인을 해주세요')
        return
      }
      const content = this.content
      if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/community/posts/${this.$route.params.postId}/comments/${this.comment.id}/`,
        data: {
          content: content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          this.content = ''
          this.$emit('select_comment', null)
          // 댓글목록 다시 가져오기
          this.$emit('get_comments')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteComment() {
      axios({
        method: 'delete',
        url: `${API_URL}/community/posts/${this.$route.params.postId}/comments/${this.comment.id}/`,
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
    selectComment() {
      const commentId = this.comment.id
      this.$emit('select_comment', commentId)
    },
  },
}
</script>

<style></style>
