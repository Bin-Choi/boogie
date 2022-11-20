<template>
  <div>
    <form @submit.prevent="createComment">
      <label for="content">내용 :</label>
      <textarea
        id="content"
        cols="20"
        rows="3"
        v-model="content"
        @keyup.enter="createComment"></textarea>
      <input type="submit" id="submit" />
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentForm',
  data() {
    return {
      content: null,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  methods: {
    createComment() {
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
        url: `${API_URL}/community/posts/${this.$route.params.postId}/comments/`,
        data: {
          content: content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          this.content = ''
          // 댓글목록 다시 가져오기
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
