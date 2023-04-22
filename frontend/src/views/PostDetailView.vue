<template>
  <div
    class="col-11 col-lg-8 mx-auto mt-3 p-3"
    :class="darkMode ? 'box-dark' : 'box-light'"
    style="max-width: 1200px">
    <div class="d-flex justify-content-between align-items-center">
      <h2 class="title ms-5 mt-4">{{ post?.title }}</h2>
      <div v-if="post?.user === user?.id">
        <div
          class="write d-inline-block"
          @click="
            $router.push({ name: 'updatePost', params: { postId: post?.id } })
          ">
          <img :src="require('@/assets/write.png')" alt="" />
        </div>
        <div class="delete d-inline-block ms-4 me-3" @click="deletePost">
          <img :src="require('@/assets/trashcan.png')" alt="" />
        </div>
      </div>
    </div>
    <div class="header d-flex justify-content-end">
      <p>{{ postCreatedAt.slice(0, 21) }}</p>
      <p class="ms-3 px-2" @click.stop="toProfile" style="cursor: pointer">
        {{ post?.username }}
      </p>
    </div>
    <hr />
    <div class="content d-flex mx-3">
      <div class="ms-4 mt-4" v-html="post?.content"></div>
    </div>
    <div>
      <img
        class="thumb-btn my-3"
        :src="post?.is_liked ? likeBluePath : likeGrayPath"
        style="width: 40px"
        @click="likePost" />
      {{ post?.like_users_count }}
    </div>
    <hr />
    <hr />
    <CommentList class="mx-5" />
  </div>
</template>

<script>
import axios from 'axios'
import CommentList from '../components/CommentList'

// const API_URL = "https://boogiee.site"

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
    }
  },
  computed: {
    API_URL() {
      return this.$store.state.API_URL
    },
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
    darkMode() {
      return this.$store.state.darkMode
    },
  },
  created() {
    this.getPost()
  },
  methods: {
    getPost() {
      if (this.isLogin) {
        axios({
          method: 'get',
          url: `${this.API_URL}/community/posts/${this.$route.params.postId}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
          .then((res) => {
            const post = res.data
            this.post = post
          })
          .catch((err) => {
            console.log(err)
          })
      } else {
        axios({
          method: 'get',
          url: `${this.API_URL}/community/posts/${this.$route.params.postId}/unlogin/`,
        })
          .then((res) => {
            const post = res.data
            this.post = post
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
    deletePost() {
      axios({
        method: 'delete',
        url: `${this.API_URL}/community/posts/${this.$route.params.postId}/`,
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
    likePost() {
      if (!this.isLogin) {
        alert('로그인을 해주세요')
        this.$store.commit('TOGGLE_LOGIN_MODAL', true)
        return
      }
      axios({
        method: 'post',
        url: `${this.API_URL}/community/posts/${this.$route.params.postId}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          const isLiked = res.data.is_liked
          this.post.is_liked = isLiked
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
    toProfile() {
      this.$router
        .push({
          name: 'profile',
          params: { username: this.post.username },
        })
        .catch(() => {})
    },
  },
}
</script>

<style scoped>
.content {
  text-align: left;
  min-height: 400px;
  overflow-x: auto;
}

.content::-webkit-scrollbar {
  height: 15px; /*스크롤바의 너비*/
}

.content::-webkit-scrollbar-thumb {
  background-color: rgb(171, 149, 192); /*스크롤바의 색상*/
  border-radius: 10px; /*스크롤바 라운드*/
}

.content::-webkit-scrollbar-track {
  background-color: rgb(234, 215, 235); /*스크롤바 트랙 색상*/
  border-radius: 10px; /*스크롤바 트랙 라운드*/
  /* box-shadow: inset 0px 0px 5px rgba(0, 0, 0, 0.2); */
}

.title {
  color: rgb(35, 19, 76);
  text-align: left;
}
.thumb-btn {
  transition: transform 0.2s linear;
}

.thumb-btn:hover {
  cursor: pointer;
}

.thumb-btn:active {
  transform: scale(1.2);
}
.header {
  color: gray;
  height: 25px;
}

p {
  text-align: center;
  margin-bottom: 0.02rem;
}

hr {
  margin: 0.04rem 0.04rem;
}

.write {
  cursor: pointer;
  width: 25px;
  height: 25px;
}

.write img {
  width: 100%;
  filter: opacity(0.8) drop-shadow(0 0 0 white);
}

.delete {
  cursor: pointer;
  width: 20px;
  height: 20px;
}

.delete img {
  width: 100%;
  filter: opacity(0.85) drop-shadow(0 0 0 white);
}
</style>
