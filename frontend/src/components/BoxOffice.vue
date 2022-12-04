<template>
  <div class="p-3" :class="darkMode ? 'box-dark' : 'box-light'">
    <h5 class="fw-bold">지난주 TOP5 일별 관객수</h5>
    <canvas class="ps-3 pe-3" id="myChart" width="100%"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js'
import axios from 'axios'

// const API_URL = 'https://boogiee.site'

export default {
  name: 'BoxOffice',
  data() {
    return {
      datasets: null,
      colors: ['#141060', '#70558e', '#7173c9', '#df94c2', '#ffbdc1'],
    }
  },
  computed: {
    API_URL() {
      return this.$store.state.API_URL
    },
    darkMode() {
      return this.$store.state.darkMode
    },
  },
  mounted() {
    const ctx = document.getElementById('myChart')

    axios({
      method: 'get',
      url: `${this.API_URL}/movies/boxoffice/`,
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
              display: false,
              text: '지난주 Top5 일별관객수',
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
              yAxes: [
                {
                  ticks: {
                    fontColor: this.darkMode ? '#d4d4d4' : '#353535',
                  },
                },
              ],
              xAxes: [
                {
                  ticks: {
                    fontColor: this.darkMode ? '#d4d4d4' : '#353535',
                  },
                },
              ],
            },
            legend: {
              labels: {
                fontColor: this.darkMode ? '#d4d4d4' : '#535353',
                fontSize: 12,
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
