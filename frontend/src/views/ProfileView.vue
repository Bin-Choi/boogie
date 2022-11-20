<template>
  <div>
    <h1>Profile</h1>
    <p>{{ person?.username }}</p>
    <p>가입일: {{ dateJoined }}</p>
    <p>점수: {{ person?.score }}점</p>
    <p>팔로잉: {{ person?.followings.length }}명</p>
    <p>팔로워: {{ person?.followers.length }}명</p>
    <div v-if="person?.id !== user?.id" @click="follow">
      <button
        type="button"
        :class="{
          btn: true,
          'btn-outline-primary': !isFollowed,
          'btn-outline-secondary': isFollowed,
        }">
        {{ isFollowed ? '팔로잉 취소' : '팔로우' }}
      </button>
    </div>
    <p>
      선호장르{{
        genrePreference[0][0] + genrePreference[1][0] + genrePreference[2][0]
      }}
    </p>
    <p>영화 &#10084;</p>
    <ProfileMovieListItem
      v-for="movie in person?.like_movies"
      :key="`movie-${movie.id}`"
      :movie="movie" />
    <p>내 리뷰</p>
    <ProfileReviewListItem
      v-for="review in person?.my_reviews"
      :key="`review-${review.id}`"
      :review="review" />
    <p>내가 작성한 글</p>
    <PostListItem
      v-for="post in person?.my_posts"
      :key="`my-${post.id}`"
      :post="post" />
    <p>글 &#128077;</p>
    <PostListItem
      v-for="post in person?.like_posts"
      :key="`like-${post.id}`"
      :post="post" />
  </div>
</template>

<script>
import ProfileMovieListItem from '@/components/ProfileMovieListItem.vue'
import ProfileReviewListItem from '@/components/ProfileReviewListItem.vue'
import PostListItem from '@/components/PostListItem.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  components: {
    ProfileMovieListItem,
    PostListItem,
    ProfileReviewListItem,
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
      return Object.entries(this.person?.genre_preference).sort(
        (a, b) => b[1] - a[1]
      )
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
  },
  beforeRouteUpdate(to, from, next) {
    this.getPerson(to.params.username)
    next()
  },
}
</script>

<style></style>
