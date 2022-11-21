<template>
  <div style="width: 100px">
    <img :src="profileUrl" style="width: 100%" />
    <input type="file" accept="image/*" v-model="profileImage" />
    <button @click="uploadProfile">변경</button>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileImage',
  props: {
    person: Object,
  },
  computed: {
    profileUrl() {
      return `${API_URL}${this.person.profile_image.profile_image}`
    },
  },
  methods: {
    uploadProfile(event) {
      const files = new FormData()
      files.append('profile_image', event.target.files[0])

      axios({
        method: 'put',
        url: `${API_URL}/users/${this.person.id}/profile/`,
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
  },
}
</script>

<style></style>
