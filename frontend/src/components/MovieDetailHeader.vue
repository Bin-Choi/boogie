<template>
  <div
    id="movie_detail_header"
    :class="darkMode ? 'header-dark' : 'header-light'">
    <div
      class="d-flex justify-content-center mx-auto"
      style="max-width: 2000px">
      <div id="movie_detail_header_poster" class="col-2">
        <img :src="poster_url" />
      </div>
      <div id="movie_detail_header_info" class="col-6 ps-4 pt-4 text-start">
        <div class="d-flex align-items-center">
          <h2 class="d-inline-block fw-bolder">{{ movie.title }}</h2>
          <span @click="likeMovie">
            <img
              class="like-btn ms-3 mb-2"
              :src="movie.is_liked ? heartPinkPath : heartGrayPath"
              style="width: 30px" />
          </span>
          <span
            class="mb-2 ms-2 like-number"
            :class="{
              'font-pink': movie.is_liked,
              'font-gray': !movie.is_liked,
            }">
            {{ movie.like_users_count }}
          </span>
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

// const API_URL = "https://boogiee.site"

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
    API_URL() {
      return this.$store.state.API_URL
    },
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
    darkMode() {
      return this.$store.state.darkMode
    },
  },
  methods: {
    likeMovie() {
      if (!this.isLogin) {
        alert('로그인을 해주세요')
        this.$store.commit('TOGGLE_LOGIN_MODAL', true)
        return
      }
      axios({
        method: 'post',
        url: `${this.API_URL}/movies/${this.movie.id}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          const isLiked = res.data.is_liked
          this.movie.is_liked = isLiked
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

<style scoped>
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
  transform: scale(1.3);
}

.like-number {
  font-weight: bold;
  font-size: 15px;
}
.font-pink {
  color: rgb(221, 67, 67);
}
.font-gray {
  color: gray;
}

.header-dark {
  color: white;
  background-color: rgba(255, 255, 255, 0.137);
}

.header-light {
  background-color: white;
}
</style>
