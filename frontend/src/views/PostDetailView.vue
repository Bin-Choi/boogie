<template>
  <div>
    <h1>제목: {{ post?.title }}</h1>

    <!-- <p>{{post.created_at}}</p> -->
    <p>작성자: {{ post?.username }}</p>
    <p>좋아요: {{ post?.like_users_count }}</p>
    <p>작성: {{ post?.created_at }}</p>
    <p>수정: {{ post?.updated_at }}</p>
    <hr />
    <p>내용: {{ post?.content }}</p>

    <hr />
    <CommentList />
  </div>
</template>

<script>
import axios from 'axios'
import CommentList from '../components/CommentList'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'PostDetailView',
  components: {
    CommentList,
  },
  data() {
    return {
      post: null,
    }
  },

  created() {
    this.getPost()
  },
  methods: {
    getPost() {
      axios({
        method: 'get',
        url: `${API_URL}/community/posts/${this.$route.params.post_pk}`,
        // headers: {
        //   Authorization: `Token ${this.$store.state.token}`,
        // },
      })
        .then((res) => {
          this.post = res.data
        })
        .catch(() => {
          this.$router.push({ name: 'index' })
        })
    },
  },
}
</script>

<style></style>
