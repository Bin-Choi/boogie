<template>
  <div>
    <canvas id="myChart" width="500" height="400"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js'
import axios from 'axios'

const API = 'http://127.0.0.1:8000'

export default {
  name: 'BoxOffice',
  data() {
    return {
      datasets: null,
    }
  },
  mounted() {
    const ctx = document.getElementById('myChart')

    axios({
      method: 'get',
      url: `${API}/movies/boxoffice/`,
    })
      .then((res) => {
        this.datasets = res.data

        const myChart = new Chart(ctx, {
          type: 'line',
          data: {
            labels: ['월', '화', '수', '목', '금', '토', '일'],
            datasets: this.datasets,
          },
          options: {
            scales: {
              y: {
                beginAtZero: true,
              },
            },
          },
        })
        myChart
      })
      .catch((err) => {
        console.log(err)
      })
  },
}
</script>

<style></style>
