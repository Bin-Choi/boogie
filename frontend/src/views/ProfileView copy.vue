<template>
  <div>
    <h1>Profile</h1>
    <p>{{ person?.username }}</p>
    <p>가입일: {{ person?.date_joined }}</p>
    <p>점수: {{ person?.score }}점</p>
    <p>팔로잉: {{ person?.followings.length }}명</p>
    <p>팔로워: {{ person?.followers.length }}명</p>
    <p>영화 &#10084;</p>
    <ProfileMovieListItem
      v-for="movie in person?.like_movies"
      :key="movie.id"
      :movie="movie" />
    <p>내 리뷰</p>
    <ReviewListItem
      v-for="review in person?.my_reivews"
      :key="review.id"
      :review="review" />>
    <p>내 리뷰:{{ person?.my_reviews }}</p>
    <p>내가 작성한 글: {{ person?.my_posts }}</p>
    <p>좋아요한 글:{{ person?.like_posts }}</p>
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
    }
  },
  computed: {
    user() {
      return this.$store.state.user
    },
    personJoinedAt() {
      return new Date(this.person?.joined_at).toLocaleString()
    },
  },
  created() {
    this.getPerson()
  },
  methods: {
    getPerson() {
      axios({
        method: 'get',
        url: `${API_URL}/users/${this.$route.params.username}/`,
        // headers: {
        //   Authorization: `Token ${this.$store.state.token}`,
        // },
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
  },
}
</script>

<style></style>
