<template>
  <div @mouseenter="hover = !hover" @mouseleave="hover = !hover">
    <span>{{ comment.username }} : {{ comment.content }}</span>
    <button v-if="hover" @click="clicked = !clicked">대댓글 작성</button>
    <div v-if="clicked">
      <input type="text" v-model="content" @keyup.enter="createRecomment" />
      <button @click="createRecomment">작성</button>
    </div>
    <RecommentItem
      v-for="recomment in recomments"
      :key="recomment.id"
      :recomment="recomment"
      class="ms-3" />
  </div>
</template>

<script>
import RecommentItem from '@/components/RecommentItem.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentListItem',
  components: {
    RecommentItem,
  },
  props: {
    comment: Object,
  },
  data() {
    return {
      hover: false,
      clicked: false,
      content: '',
      recomments: null,
    }
  },
  created() {
    this.getRecomments()
  },
  methods: {
    createRecomment() {
      const content = this.content
      if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/community/comments/post/${this.$route.params.post_pk}/comment/${this.comment.id}/`,
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
    getRecomments() {
      axios({
        method: 'get',
        url: `${API_URL}/community/comments/post/${this.$route.params.post_pk}/comment/${this.comment.id}/`,
        // headers: {
        //   Authorization: `Token ${context.state.token}`
        // }
      })
        .then((res) => {
          this.recomments = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
