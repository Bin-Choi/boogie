<template>
  <div>
    <div
      class="comment d-flex justify-content-between align-itmes-center py-2"
      @mouseenter="hover = true"
      @mouseleave="hover = false">
      <div class="ms-4">
        <span class="fw-bold">{{ comment.username }}</span>
        <span class="ms-3">{{ comment.content }}</span>
        <button class="recomment-btn ms-3" v-if="hover" @click="selectComment">
          대댓글
        </button>
      </div>
      <div
        v-if="comment.user === user?.id"
        class="delete d-inline-block ms-4 me-3"
        @click="deleteComment">
        <img :src="require('@/assets/trashcan.png')" alt="" />
      </div>
    </div>
    <div class="ms-4" v-if="comment.id === selectedComment">
      <input
        class="recomment-form"
        type="text"
        v-model="content"
        @keyup.enter="createRecomment" />
      <button
        class="ms-3"
        style="border: none; border-radius: 3px"
        @click="createRecomment">
        작성
      </button>
    </div>

    <RecommentItem
      v-for="recomment in recomments"
      :key="recomment.id"
      :recomment="recomment"
      @get_comments="$emit('get_comments')"
      class="ms-4" />
  </div>
</template>

<script>
import RecommentItem from '@/components/RecommentItem.vue'
import axios from 'axios'

// const API_URL = "https://boogiee.site"

export default {
  name: 'CommentListItem',
  components: {
    RecommentItem,
  },
  props: {
    comments: Array,
    selectedComment: Number,
  },
  data() {
    return {
      hover: false,
      content: '',
    }
  },
  computed: {
    API_URL() {
      return this.$store.state.API_URL
    },
    comment() {
      return this.comments[0]
    },
    recomments() {
      return this.comments.slice(1)
    },
    user() {
      return this.$store.state.user
    },
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  methods: {
    createRecomment() {
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
        url: `${this.API_URL}/community/posts/${this.$route.params.postId}/comments/${this.comment.id}/`,
        data: {
          content: content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          this.content = ''
          this.$emit('select_comment', null)
          // 댓글목록 다시 가져오기
          this.$emit('get_comments')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteComment() {
      axios({
        method: 'delete',
        url: `${this.API_URL}/community/posts/${this.$route.params.postId}/comments/${this.comment.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          this.$emit('get_comments')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    selectComment() {
      const commentId = this.comment.id
      this.$emit('select_comment', commentId)
    },
  },
}
</script>

<style scoped>
hr {
  margin-left: 7px;
  margin-right: 7px;
  margin-top: 0.1rem;
  margin-bottom: 0.05rem;
}
.comment:hover {
  background-color: rgba(239, 239, 239, 0.436);
  border-radius: 5px;
}
.comment {
  transition: transform 0.2s;
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

.recomment-btn {
  border: none;
  outline: none;
  border-radius: 5px;
}
.recomment-btn:hover {
  background-color: rgb(224, 224, 224);
}

.recomment-form {
  width: 250px;
  height: 27px;
  border: none;
  outline: none;
  border-radius: 5px;
  padding-left: 10px;
  box-shadow: inset 0 0 3px rgb(186, 186, 186);
}
</style>
