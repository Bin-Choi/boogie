<template>
  <div>
    <h1>댓글 작성</h1>
    <form @submit.prevent="createComment">
      <label for="content">내용 :</label>
      <textarea id="content" cols="20" rows="3" v-model="content"></textarea>
      <input type="submit" id="submit" />
    </form>
  </div>
</template>

<script>
import axios from "axios"

const API_URL = "http://127.0.0.1:8000"

export default {
  name: "CommentForm",
  data() {
    return {
      content: null,
    }
  },
  methods: {
    createComment() {
      const content = this.content
      if (!title) {
        alert("내용을 입력해주세요")
        return
      }
      axios({
        method: "post",
        url: `${API_URL}/`,
        data: {
          content: content,
        },
        //   headers: {
        //     Authorization: `Token ${this.$store.state.token}`
        //   }
      })
        .then((res) => {
          console.log(res)
          this.$router.push({ name: "DetailView" })
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
