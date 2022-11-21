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
      colors: ['#CC0000', '#3366FF', '#33CC33', '#FF6600', '#FFFF66'],
    }
  },
  methods: {},
  mounted() {
    const ctx = document.getElementById('myChart')

    axios({
      method: 'get',
      url: `${API}/movies/boxoffice/`,
    })
      .then((res) => {
        const datasets = res.data
        // for datasets:
        // , "borderWidth":'3', "fill": 'false', "tension": "0.3"}
        let i = 0

        datasets.forEach((dataset) => {
          dataset['borderWidth'] = 3
          dataset['fill'] = false
          dataset['tension'] = 0.3
          dataset['borderColor'] = this.colors[i]
          i += 1
        })

        this.datasets = datasets

        const myChart = new Chart(ctx, {
          type: 'line',
          data: {
            labels: ['월', '화', '수', '목', '금', '토', '일'],
            datasets: this.datasets,
          },
          options: {
            responsive: true,
            title: {
              display: true,
              text: '주간 인기 영화',
            },
            tooltips: {
              mode: 'index',
              intersect: false,
            },
            hover: {
              mode: 'nearest',
              intersect: true,
            },
            scales: {
              y: {
                type: 'linear',
                suggestedMin: 0,
                suggestedMax: 1000000,
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
