<template>
  <div>
    <div v-if="!myReview" id="review_form">
      <div id="stars" class="pt-1 me-3 mb-2">
        <img
          :src="grayStarPath"
          @mouseenter="colorStars(1, $event)"
          @mouseleave="uncolorStar(1, $event)"
          @click="saveScore(1, $event)"
          style="width: 40px" />
        <img
          :src="grayStarPath"
          @mouseenter="colorStars(2, $event)"
          @mouseleave="uncolorStar(2, $event)"
          @click="saveScore(2, $event)"
          style="width: 40px" />
        <img
          :src="grayStarPath"
          @mouseenter="colorStars(3, $event)"
          @mouseleave="uncolorStar(3, $event)"
          @click="saveScore(3, $event)"
          style="width: 40px" />
        <img
          :src="grayStarPath"
          @mouseenter="colorStars(4, $event)"
          @mouseleave="uncolorStar(4, $event)"
          @click="saveScore(4, $event)"
          style="width: 40px" />
        <img
          :src="grayStarPath"
          @mouseenter="colorStars(5, $event)"
          @mouseleave="uncolorStar(5, $event)"
          @click="saveScore(5, $event)"
          style="width: 40px" />
      </div>
      <div class="d-flex mb-2">
        <input
          id="review_text_form"
          type="text"
          v-model.trim="content"
          @keyup.enter="createReview" />
        <div class="write d-inline-block ms-3" @click="createReview">
          <img :src="require('@/assets/write.png')" alt="" />
        </div>
      </div>
    </div>
    <div v-if="myReview" class="d-flex justify-content-between">
      <div class="d-flex flex-wrap align-items-center mb-3">
        <div style="width: 180px" class="me-3">
          <img :src="myReviewStarPath" style="width: 100%" />
        </div>
        <div class="fs-5 fw-bold mt-1">
          {{ myReview.content }}
        </div>
        <div class="delete d-inline-block ms-3 me-1" @click="deleteReview">
          <img :src="require('@/assets/trashcan.png')" alt="" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

// const API_URL = "https://boogiee.site"

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
    API_URL() {
      return this.$store.state.API_URL
    },
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
  watch: {
    $route() {
      this.getMyReview()
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
        url: `${this.API_URL}/movies/${this.$route.params.movieId}/myreview/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.myReview = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    createReview() {
      if (!this.isLogin) {
        alert('로그인을 해주세요')
        this.$store.commit('TOGGLE_LOGIN_MODAL', true)
        return
      }
      const vote = this.vote
      const content = this.content
      axios({
        method: 'post',
        url: `${this.API_URL}/movies/${this.$route.params.movieId}/reviews/`,
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
        url: `${this.API_URL}/movies/${this.$route.params.movieId}/reviews/${this.myReview.id}/`,
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

<style scoped>
#review_form {
  display: flex;
  flex-wrap: wrap;
}

#review_text_form {
  width: 280px;
  height: 40px;
  border: none;
  border-radius: 5px;
  padding-left: 5px;
  background-color: rgb(229, 227, 230);
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
  filter: opacity(0.7) drop-shadow(0 0 0 white);
}
</style>
