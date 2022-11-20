<template>
  <div>
    <h1>Search</h1>
    <canvas id="myChart"></canvas>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<script>
import axios from 'axios'
import Chart from 'chart.js'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'SearchView',
  created() {
    const ctx = document.getElementById('myChart')

    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [
          {
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    })
  },
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
