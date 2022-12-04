<template>
  <div>
    <div v-if="person">
      <!-- <ProfileBackdrop :person="person" @change_backdrop="changeBackdrop" /> -->
      <div
        class="profile-header d-flex align-items-end justify-content-center"
        :style="{
          backgroundImage: `url(${backdropUrl})`,
        }">
        <div class="container profile-info mb-3 py-4 mx-2">
          <div class="row">
            <ProfileImage
              class="col-6 ps-4"
              :person="person"
              @change_profile="changeProfile" />
            <div class="col-6">
              <h4 class="fw-bold mt-3">{{ person?.username }}님의 프로필</h4>
              <p class="mt-4">가입일: {{ dateJoined }}</p>
              <p>점수: {{ person?.score }}점</p>
              <p>
                <span v-if="this.person?.genre_preference.length >= 1"
                  >{{ this.person?.genre_preference[0]['genre'] }}
                </span>
                <span v-if="this.person?.genre_preference.length >= 2">
                  | {{ this.person?.genre_preference[1]['genre'] }}
                </span>
                <span v-if="this.person?.genre_preference.length >= 3">
                  | {{ this.person?.genre_preference[2]['genre'] }}</span
                >
              </p>
              <p
                class="fw-bold"
                style="cursor: pointer"
                @click="$store.commit('TOGGLE_USERS_MODAL', true)">
                <span @click="$store.commit('SAVE_USERS', person?.followings)"
                  >팔로잉: {{ person?.followings.length }}명 /
                </span>
                <span @click="$store.commit('SAVE_USERS', person?.followers)"
                  >팔로워: {{ person?.followers.length }}명</span
                >
              </p>
              <div v-if="person?.id == user?.id" @click="withdraw">
                <button type="button" class="btn btn-outline-danger">
                  회원탈퇴
                </button>
              </div>
              <div v-if="person?.id !== user?.id" @click="follow">
                <button
                  type="button"
                  :class="{
                    btn: true,
                    'btn-outline-primary': !person.is_followed,
                    'btn-outline-secondary': person.is_followed,
                  }">
                  {{ person?.is_followed ? 'Unfollow' : 'Follow' }}
                </button>
              </div>
            </div>
          </div>
          <div v-if="person?.id === user?.id" class="backdrop-input-delete">
            <input
              style="width: 200px"
              type="file"
              accept="image/*"
              @change="uploadBackdrop" />
            <div class="delete d-inline-block ms-3" @click="deleteBackdrop">
              <img :src="require('@/assets/trashcan.png')" alt="" />
            </div>
          </div>
        </div>
      </div>
      <div class="container" style="max-width: 1200px">
        <div class="row col-12 col-lg-9 justify-content-center mx-auto">
          <ProfileMovieList class="mt-3" :likeMovies="person.like_movies" />
          <ProfileLikePostList class="mt-3" :posts="person.like_posts" />
          <ProfileReviewList class="mt-3" :myReviews="person.my_reviews" />
          <ProfilePostList class="mt-3" :posts="person.my_posts" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import ProfileBackdrop from '@/components/ProfileBackdrop.vue'
import ProfileImage from '@/components/ProfileImage.vue'
import ProfileMovieList from '@/components/ProfileMovieList.vue'
import ProfileReviewList from '@/components/ProfileReviewList.vue'
import ProfileLikePostList from '@/components/ProfileLikePostList.vue'
import ProfilePostList from '@/components/ProfilePostList.vue'
import axios from 'axios'

// const API_URL = 'https://boogiee.site'

export default {
  name: 'ProfileView',
  components: {
    ProfileImage,
    // ProfileBackdrop,
    ProfileMovieList,
    ProfileReviewList,
    ProfilePostList,
    ProfileLikePostList,
  },
  data() {
    return {
      person: null,
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
    dateJoined() {
      return new Date(this.person?.date_joined).toLocaleDateString()
    },
    backdropUrl() {
      return `${this.$store.state.API_URL}${this.person.backdrop_image}`
    },
  },
  created() {
    this.getPerson(this.$route.params.username)
  },
  methods: {
    getPerson(username) {
      axios({
        method: 'get',
        url: `${this.API_URL}/users/${username}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          const person = res.data
          this.person = person
        })
        .catch((err) => {
          console.log(err)
        })
    },
    follow() {
      if (!this.isLogin) {
        alert('로그인이 필요합니다')
        return
      }
      axios({
        method: 'post',
        url: `${this.API_URL}/users/${this.person.id}/follow/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          const isFollowed = res.data.is_followed
          this.person.is_followed = isFollowed
          if (isFollowed) {
            this.person.followers.length += 1
          } else {
            this.person.followers.length -= 1
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    changeProfile(profileImage) {
      this.person.profile_image = profileImage
    },
    uploadBackdrop(event) {
      if (!event.target.files.length) {
        return
      }
      const files = new FormData()
      files.append('backdrop_image', event.target.files[0])

      axios({
        method: 'put',
        url: `${this.API_URL}/users/${this.person.id}/backdrop/`,
        data: files,
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          this.person.backdrop_image = res.data.backdrop_image
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteBackdrop() {
      axios({
        method: 'delete',
        url: `${this.API_URL}/users/${this.person.id}/backdrop/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          this.person.backdrop_image = res.data.backdrop_image
        })
        .catch((err) => {
          console.log(err)
        })
    },
    withdraw() {
      axios({
        method: 'delete',
        url: `${this.API_URL}/users/${this.user.id}/withdraw/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          this.$store.commit('WITHDRAW')
          this.$router.push({ name: 'index' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  beforeRouteUpdate(to, from, next) {
    this.getPerson(to.params.username)
    next()
  },
}
</script>

<style scoped>
.profile-header {
  position: relative;
  height: 500px;
  background-size: cover;
}

.profile-info {
  max-width: 500px;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.61);
}

.delete {
  cursor: pointer;
  width: 20px;
  height: 20px;
}

.delete img {
  width: 100%;
  filter: opacity(0.8) drop-shadow(0 0 0 white);
}

.backdrop-input-delete {
  position: absolute;
  right: 10px;
  bottom: 10px;
}
</style>
