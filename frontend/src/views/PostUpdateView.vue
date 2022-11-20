<template>
  <div>
    <h1>게시글 수정</h1>
    <form @submit.prevent="updatePost">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title" /><br />
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea
      ><br />
      <input type="submit" value="수정" />
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'PostUpdateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  created() {
    this.getPost()
  },
  methods: {
    getPost() {
      axios({
        method: 'get',
        url: `${API_URL}/community/posts/${this.$route.params.postId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          const post = res.data
          this.title = post.title
          this.content = post.content
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updatePost() {
      axios({
        method: 'put',
        url: `${API_URL}/community/posts/${this.$route.params.postId}/`,
        data: {
          title: this.title,
          content: this.content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          this.$router.push({
            name: 'postDetail',
            params: { postId: this.$route.params.postId },
          })
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
