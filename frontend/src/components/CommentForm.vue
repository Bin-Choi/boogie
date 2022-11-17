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

<script></script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentForm',
  data() {
    return {
      content: null,
    }
  },
  methods: {
    createComment() {
      const content = this.content
      if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/community/comments/post/${this.$route.params.post_pk}/`,
        data: {
          content: content,
        },
        //   headers: {
        //     Authorization: `Token ${this.$store.state.token}`
        //   }
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
