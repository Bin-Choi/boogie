<template>
  <div id="movie_detail_header">
    <div
      class="d-flex justify-content-center mx-auto"
      style="max-width: 2000px"
    >
      <div id="movie_detail_header_poster" class="col-2">
        <img :src="poster_url" />
      </div>
      <div id="movie_detail_header_info" class="col-6 ps-4 pt-4 text-start">
        <div>
          <h2 class="fw-bolder">{{ movie.title }}</h2>
          <div @click="likeMovie">
            <img
              class="like-btn"
              :src="movie.isLiked ? heartPinkPath : heartGrayPath"
              style="width: 50px"
            />
            {{ movie.like_users_count }}
          </div>
        </div>

        <p class="fs-6" style="color: gray">
          {{ movie.release_date }} · {{ genres }} · {{ movie?.country }}
        </p>
        <hr />
        <p class="fs-6 fw-bold">
          평균⭐ {{ Math.round(movie.vote_average * 5) / 10 }}점 ({{
            movie.vote_count
          }}명)
        </p>
        <hr />
        <ReviewForm />
      </div>
    </div>
  </div>
</template>

<script>
import ReviewForm from '@/components/ReviewForm.vue'

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetailHeader',
  components: {
    ReviewForm,
  },
  data() {
    return {
      heartPinkPath: require('@/assets/heart_pink.png'),
      heartGrayPath: require('@/assets/heart_gray.png'),
    }
  },
  computed: {
    user() {
      return this.$store.state.user
    },
    isLogin() {
      return this.$store.getters.isLogin
    },
    movie() {
      return this.$store.state.movie
    },
    poster_url() {
      if (this.movie.poster_path) {
        return `https://image.tmdb.org/t/p/original${this.movie.poster_path}`
      } else {
        return require('@/assets/movie_default_poster.png')
      }
    },
    genres() {
      let genres = ''
      this.movie.genres.forEach((genre) => {
        genres += genre.name + ' '
      })
      return genres
    },
  },
  methods: {
    likeMovie() {
      if (!this.isLogin) {
        alert('로그인이 필요합니다')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.movie.id}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          const isLiked = res.data.is_liked
          this.movie.isLiked = isLiked
          if (isLiked) {
            this.movie.like_users_count += 1
          } else {
            this.movie.like_users_count -= 1
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style>
#movie_detail_header {
  background-color: white;
}

#movie_detail_header_poster {
  height: 263px;
  width: 186px;
  overflow: hidden;

  position: relative;
  bottom: 40px;

  border: 3px solid white;
  border-radius: 3px;

  box-shadow: 0px 0px 15px #272727;
}

#movie_detail_header_poster img {
  width: 100%;
  object-fit: cover;
}

hr {
  color: #b7b7b7;
}

.like-btn {
  transition: transform 0.2s linear;
}

.like-btn:hover {
  cursor: pointer;
}

.like-btn:active {
  transform: scale(1.5);
}
</style>
