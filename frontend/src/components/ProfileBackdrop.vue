<template>
  <div>
    <div id="profile_backdrop">
      <img :src="backdropUrl" />
    </div>
    <input type="file" accept="image/*" @change="uploadBackdrop" />
    <button @click="deleteBackdrop">삭제</button>
  </div>
</template>

<script>
import axios from 'axios'

// const API_URL = "https://boogiee.site"

export default {
  name: 'ProfileBackdrop',
  props: {
    person: Object,
  },
  computed: {
    API_URL() {
      return this.$store.state.API_URL
    },
    backdropUrl() {
      return `${this.$store.state.API_URL}${this.person.backdrop_image}`
    },
  },
  methods: {
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
          const backdropImage = res.data.backdrop_image
          this.$emit('change_backdrop', backdropImage)
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
          const backdropImage = res.data.backdrop_image
          this.$emit('change_backdrop', backdropImage)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style>
#profile_backdrop {
  width: 100%;
  height: 300px;
  overflow: hidden;
}

#profile_backdrop img {
  width: 100%;
  height: 500px;
  object-fit: cover;
}
</style>
