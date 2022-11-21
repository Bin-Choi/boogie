<template>
  <div>
    <h1>제목: {{ post?.title }}</h1>
    <p>작성자: {{ post?.username }}</p>
    <p>좋아요: {{ post?.like_users_count }}</p>
    <p>작성: {{ postCreatedAt }}</p>
    <p>수정: {{ postUpdatedAt }}</p>
    <button
      v-if="post?.user === user.id"
      type="button"
      class="btn btn-primary"
      @click="
        $router.push({ name: 'updatePost', params: { postId: post?.id } })
      "
    >
      수정
    </button>
    <button
      v-if="post?.user === user.id"
      type="button"
      class="btn btn-danger"
      @click="deletePost"
    >
      삭제
    </button>
    <hr />
    <p>내용: {{ post?.content }}</p>
    <div @click="likePost">
      <img
        class="thumb-btn"
        :src="isLiked ? likeBluePath : likeGrayPath"
        style="width: 50px"
      />
      {{ post?.like_users_count }}
    </div>
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
      likeBluePath: require('@/assets/like_blue.png'),
      likeGrayPath: require('@/assets/like_gray.png'),
      isLiked: false,
    }
  },
  computed: {
    user() {
      return this.$store.state.user
    },
    isLogin() {
      return this.$store.getters.isLogin
    },
    postCreatedAt() {
      return new Date(this.post?.created_at).toLocaleString()
    },
    postUpdatedAt() {
      return new Date(this.post?.updated_at).toLocaleString()
    },
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
          this.post = post
          // isLiked
          this.isLiked = post.like_users.includes(this.user.id) ? true : false
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deletePost() {
      axios({
        method: 'delete',
        url: `${API_URL}/community/posts/${this.$route.params.postId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          this.$route.push({ name: 'community' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    likePost() {
      if (!this.isLogin) {
        alert('로그인이 필요합니다')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/community/posts/${this.$route.params.postId}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          const isLiked = res.data.is_liked
          this.isLiked = isLiked
          if (isLiked) {
            this.post.like_users_count += 1
          } else {
            this.post.like_users_count -= 1
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style scoped>
.thumb-btn {
  transition: transform 0.2s linear;
}

.thumb-btn:hover {
  cursor: pointer;
}

.thumb-btn:active {
  transform: scale(1.5);
}
</style>
