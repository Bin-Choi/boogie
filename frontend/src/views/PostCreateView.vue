<template>
  <div
    :class="darkMode ? 'box-dark' : 'box-light'"
    class="col-11 col-lg-8 mx-auto mt-3 p-3">
    <h4 class="fw-bold">게시글 작성</h4>
    <form @submit.prevent="createPost">
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

// const API_URL = "https://boogiee.site"

export default {
  name: 'PostCreateView',
  data() {
    return {
      title: null,
      content: null,
      editorConfig: {
        // The configuration of the editor.
        height: '400px',
        removeButtons: 'Maximize, ShowBlocks',
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
  methods: {
    createPost() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${this.API_URL}/community/posts/`,
        data: {
          title: title,
          content: content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          this.$router.push({ name: 'community' })
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
