<template>
  <div>
    <div v-if="!myReview" id="review_form" class="d-flex">
      <div id="stars">
        <img
          :src="grayStarPath"
          @mouseenter="colorStars(1, $event)"
          @mouseleave="uncolorStar(1, $event)"
          @click="saveScore(1, $event)"
          style="width: 50px" />
        <img
          :src="grayStarPath"
          @mouseenter="colorStars(2, $event)"
          @mouseleave="uncolorStar(2, $event)"
          @click="saveScore(2, $event)"
          style="width: 50px" />
        <img
          :src="grayStarPath"
          @mouseenter="colorStars(3, $event)"
          @mouseleave="uncolorStar(3, $event)"
          @click="saveScore(3, $event)"
          style="width: 50px" />
        <img
          :src="grayStarPath"
          @mouseenter="colorStars(4, $event)"
          @mouseleave="uncolorStar(4, $event)"
          @click="saveScore(4, $event)"
          style="width: 50px" />
        <img
          :src="grayStarPath"
          @mouseenter="colorStars(5, $event)"
          @mouseleave="uncolorStar(5, $event)"
          @click="saveScore(5, $event)"
          style="width: 50px" />
      </div>
      <div id="review_text_form" class="ms-5">
        <input type="text" v-model.trim="content" />
        <button
          type="button"
          class="btn btn-outline-primary ms-2"
          @click="createReview">
          작성
        </button>
      </div>
    </div>
    <div v-if="myReview">
      <img :src="myReviewStarPath" style="width: 200px" />
      <span class="fs-4 fw-bold" style="margin-left: 20px">{{
        myReview.content
      }}</span>
      <button type="button" class="btn btn-danger" @click="deleteReview">
        삭제
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewForm',
  data() {
    return {
      myReview: null,
      yellowStarPath: require('@/assets/star_yellow.png'),
      grayStarPath: require('@/assets/star_gray.png'),
      vote: null,
      content: '',
    }
  },
  computed: {
    myReviewStarPath() {
      if (this.myReview) {
        return require(`@/assets/stars_${this.myReview.vote}.png`)
      }
      return ''
    },
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  created() {
    this.getMyReview()
  },
  methods: {
    colorStars(order) {
      if (!this.voted) {
        const stars = document.querySelectorAll('#stars img')
        for (let i = 0; i < order; i++) {
          stars[i].setAttribute('src', this.yellowStarPath)
        }
      }
    },
    uncolorStar(order) {
      if (!this.voted) {
        const stars = document.querySelectorAll('#stars img')
        for (let i = 0; i < order; i++) {
          stars[i].setAttribute('src', this.grayStarPath)
        }
      }
    },
    saveScore(order) {
      this.vote = order
      this.voted = true
      const stars = document.querySelectorAll('#stars img')
      for (let i = 0; i < order; i++) {
        stars[i].setAttribute('src', this.yellowStarPath)
      }
      for (let i = order; i < 5; i++) {
        stars[i].setAttribute('src', this.grayStarPath)
      }
    },
    getMyReview() {
      if (!this.isLogin) {
        return
      }
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.movieId}/myreview/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          if (res.status === 204) return
          this.myReview = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    createReview() {
      if (!this.isLogin) {
        alert('로그인 해주세요')
        return
      }
      const vote = this.vote
      const content = this.content
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.$route.params.movieId}/reviews/`,
        data: {
          vote,
          content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          const stars = document.querySelectorAll('#stars img')
          for (let i = 0; i < 5; i++) {
            stars[i].setAttribute('src', this.grayStarPath)
          }
          this.content = ''
          this.myReview = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteReview() {
      axios({
        method: 'delete',
        url: `${API_URL}/movies/reviews/${this.myReview.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          this.myReview = null
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style>
#review_form {
  display: flex;
  flex-wrap: wrap;
}
</style>
