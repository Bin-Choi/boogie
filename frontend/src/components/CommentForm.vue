<template>
  <div>
    <form
      @submit.prevent="createComment"
      class="d-flex justify-content-center align-items-center">
      <textarea
        id="content"
        class="comment-form mt-3"
        v-model="content"
        @keyup.enter="createComment"></textarea>
      <input class="btn submit-btn mt-3 ms-3" type="submit" id="submit" />
    </form>
  </div>
</template>

<script>
import axios from 'axios'

// const API_URL = "https://boogiee.site"

export default {
  name: 'CommentForm',
  data() {
    return {
      content: null,
    }
  },
  computed: {
    API_URL() {
      return this.$store.state.API_URL
    },
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  methods: {
    createComment() {
      if (!this.isLogin) {
        alert('로그인을 해주세요')
        this.$store.commit('TOGGLE_LOGIN_MODAL', true)
        return
      }
      const content = this.content
      if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${this.API_URL}/community/posts/${this.$route.params.postId}/comments/`,
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

<style scoped>
.comment-form {
  width: 300px;
  height: 50px;
  border: none;
  outline: none;
  border-radius: 5px;
  padding-left: 10px;
  box-shadow: inset 0 0 5px rgb(186, 186, 186);
}

form {
  /* padding: 10px 0px 10px 0px;
  background-color: rgba(219, 219, 219, 0.459); */
}

.submit-btn {
  color: white;
  background-color: rgb(135, 96, 167);
}

.submit-btn:hover {
  color: white;
  background-color: rgb(91, 53, 123);
}
</style>
