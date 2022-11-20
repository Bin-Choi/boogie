<template>
  <div>
    <h1>Search</h1>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'SearchView',
  created() {},
  methods: {
    getRecommends() {
      axios({
        method: 'get',
        url: `${API_URL}/`,
        // headers: {
        //   Authorization: `Token ${this.$store.state.token}`,
        // },
        data: {
          판타지: 1,
        },
      })
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
