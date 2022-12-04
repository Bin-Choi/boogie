<template>
  <div
    :class="darkMode ? 'box-dark' : 'box-light'"
    class="col-8 mx-auto mt-3 p-3">
    <h4 class="fw-bold">게시글 수정</h4>
    <form @submit.prevent="updatePost">
      <input
        class="title-input"
        type="text"
        id="title"
        v-model.trim="title"
        placeholder="제목" />
      <!-- <textarea id="content" cols="30" rows="10" v-model="content"></textarea> -->
      <ckeditor
        class="mt-3"
        v-model="content"
        :config="editorConfig"></ckeditor>
      <br />
      <input class="btn submit-btn" type="submit" id="submit" />
    </form>
  </div>
</template>

<script>
import axios from 'axios'

// const API_URL = 'https://boogiee.site'

export default {
  name: 'PostUpdateView',
  data() {
    return {
      title: null,
      content: null,
      editorConfig: {
        // The configuration of the editor.
        height: '400px',
      },
    }
  },
  computed: {
    API_URL() {
      return this.$store.state.API_URL
    },
    darkMode() {
      return this.$store.state.darkMode
    },
  },
  created() {
    this.getPost()
  },
  methods: {
    getPost() {
      axios({
        method: 'get',
        url: `${this.API_URL}/community/posts/${this.$route.params.postId}/`,
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
        url: `${this.API_URL}/community/posts/${this.$route.params.postId}/`,
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

<style scoped>
.title-input {
  color: black;
  font-size: 20px;
  width: 80%;
  height: 45px;
  border: none;
  outline: none;
  border-radius: 5px;
  padding-left: 10px;
  box-shadow: inset 0 0 5px rgb(186, 186, 186);
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
