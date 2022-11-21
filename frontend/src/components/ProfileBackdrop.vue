<template>
  <div>
    <img :src="backdropUrl" />
    <input type="file" accept="image/*" @change="uploadBackdrop" />
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileBackdrop',
  props: {
    person: Object,
  },
  computed: {
    backdropUrl() {
      return `${API_URL}${this.person.backdrop_image.backdrop_image}`
    },
  },
  methods: {
    uploadBackdrop(event) {
      const files = new FormData()
      files.append('backdrop_image', event.target.files[0])

      axios({
        method: 'put',
        url: `${API_URL}/users/${this.person.id}/backdrop/`,
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
  },
}
</script>

<style></style>
