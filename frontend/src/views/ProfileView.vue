<template>
  <div>
    <h1>Profile</h1>
    <div v-if="person">
      <ProfileBackdrop :person="person" @change_backdrop="changeBackdrop" />
      <ProfileImage :person="person" @change_profile="changeProfile" />
      <div>
        <p>{{ person?.username }}</p>
        <p>가입일: {{ dateJoined }}</p>
        <p>점수: {{ person?.score }}점</p>
        <!-- <p>팔로잉: {{ person?.followings.length }}명</p> -->
        <!-- <p>팔로워: {{ person?.followers.length }}명</p> -->
        <div v-if="person?.id !== user?.id" @click="follow">
          <button
            type="button"
            :class="{
              btn: true,
              'btn-outline-primary': !isFollowed,
              'btn-outline-secondary': isFollowed,
            }"
          >
            {{ isFollowed ? '팔로잉 취소' : '팔로우' }}
          </button>
          <p>
            선호장르
            <span v-if="genrePreference?.length >= 1">{{
              genrePreference[0][0]
            }}</span>
            <span v-if="genrePreference?.length >= 2">{{
              genrePreference[1][0]
            }}</span>
            <span v-if="genrePreference?.length >= 3">{{
              genrePreference[2][0]
            }}</span>
          </p>
        </div>
      </div>
      <ProfileMovieList :likeMovies="person.like_movies" />
      <ProfileReviewList :myReviews="person.my_reviews" />
      <ProfilePostList :postTitle="'내가 작성한 글'" :post="person.my_posts" />
      <ProfilePostList :postTitle="'글'" :post="person.like_posts" />
    </div>
  </div>
</template>

<script>
import ProfileBackdrop from '@/components/ProfileBackdrop.vue'
import ProfileImage from '@/components/ProfileImage.vue'
import ProfileMovieList from '@/components/ProfileMovieList.vue'
import ProfileReviewList from '@/components/ProfileReviewList.vue'
import ProfilePostList from '@/components/ProfilePostList.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  components: {
    ProfileImage,
    ProfileBackdrop,
    ProfileMovieList,
    ProfileReviewList,
    ProfilePostList,
  },
  data() {
    return {
      person: null,
      isFollowed: false,
    }
  },
  computed: {
    user() {
      return this.$store.state.user
    },
    isLogin() {
      return this.$store.getters.isLogin
    },
    dateJoined() {
      return new Date(this.person?.date_joined).toLocaleDateString()
    },
    genrePreference() {
      if (this.person?.genre_preference) {
        return Object.entries(this.person?.genre_preference).sort(
          (a, b) => b[1] - a[1]
        )
      } else {
        return []
      }
    },
  },
  created() {
    this.getPerson(this.$route.params.username)
  },
  methods: {
    getPerson(username) {
      axios({
        method: 'get',
        url: `${API_URL}/users/${username}/`,
        // headers: {
        //   Authorization: `Token ${this.$store.state.token}`,
        // },
      })
        .then((res) => {
          console.log(res)
          const person = res.data
          this.person = person
          if (person.followers.includes(this.user?.id)) {
            this.isFollowed = true
          } else {
            this.isFollowed = false
          }
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
        url: `${API_URL}/users/${this.person.id}/follow/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          const isFollowed = res.data.is_followed
          this.isFollowed = isFollowed
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
      this.person.profile_image.profile_image = profileImage
    },
    changeBackdrop(backdropImage) {
      console.log(backdropImage)
      this.person.backdrop_image.backdrop_image = backdropImage
    },
  },
  beforeRouteUpdate(to, from, next) {
    this.getPerson(to.params.username)
    next()
  },
}
</script>

<style></style>
