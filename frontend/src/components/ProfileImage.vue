<template>
  <div class="d-flex flex-column align-items-center">
    <div class="d-flex">
      <div id="profile-box">
        <img :src="profileUrl" style="width: 100%" />
      </div>
      <div
        v-if="person?.id === user?.id"
        class="delete align-self-end"
        @click="deleteProfile"
      >
        <img :src="require('@/assets/trashcan.png')" alt="" />
      </div>
    </div>
    <div class="mt-3">
      <input
        v-if="person?.id === user?.id"
        style="width: 200px"
        type="file"
        accept="image/*"
        @change="uploadProfile"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'

// const API_URL = "https://boogiee.site"

export default {
  name: 'ProfileImage',
  props: {
    person: Object,
  },
  computed: {
    API_URL() {
      return this.$store.state.API_URL
    },
    user() {
      return this.$store.state.user
    },
    profileUrl() {
      return `${this.$store.state.API_URL}${this.person.profile_image}`
    },
  },
  methods: {
    uploadProfile(event) {
      if (!event.target.files.length) {
        return
      }
      const files = new FormData()
      files.append('profile_image', event.target.files[0])

      axios({
        method: 'put',
        url: `${this.API_URL}/users/${this.person.id}/profile/`,
        data: files,
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          const profileImage = res.data.profile_image
          this.$emit('change_profile', profileImage)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteProfile() {
      axios({
        method: 'delete',
        url: `${this.API_URL}/users/${this.person.id}/profile/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          const profileImage = res.data.profile_image
          this.$emit('change_profile', profileImage)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style scoped>
#profile-box {
  width: 200px;
  height: 200px;
  border-radius: 70%;
  overflow: hidden;
}
.delete {
  cursor: pointer;
  width: 20px;
  height: 20px;
}

.delete img {
  width: 100%;
  filter: opacity(0.6) drop-shadow(0 0 0 white);
}
</style>
