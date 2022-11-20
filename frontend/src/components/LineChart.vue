// 공용 사용 가능성이 있어서 components/Charts 에 컴포넌트 형태로 저장하여 사용
// data = chartData 외부에서 가져옴 // chartData = {labels: ['전체 범주'], data:
{ label: '그래프 범주', data: []}
<script>
import { Line } from "vue-chartjs"

export default {
  name: "LineChart",
  extends: Line,
  props: ["chartData"],
  data: () => ({
    colorSets: [
      // 여러 그래프 사용을 위해서 색상표 예약
      { fore: "#EF9A9A", back: "#B71C1C" },
      { fore: "#F48FB1", back: "#880E4F" },
      { fore: "#CE93D8", back: "#4A148C" },
      { fore: "#B39DDB", back: "#311B92" },
      { fore: "#9FA8DA", back: "#1A237E" },
      { fore: "#64B5F6", back: "#0D47A1" },
      { fore: "#4FC3F7", back: "#01579B" },
      { fore: "#0097A7", back: "#006064" },
      { fore: "#00897B", back: "#004D40" },
      { fore: "#81C784", back: "#1B5E20" },
    ],
    datacollection: {
      // 데이터 샘플
      // 전체 범주
      // labels: ["월", "화", "수", "목", "금", "토", "일"],
      labels: [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
      ],
      datasets: [
        {
          // 그래프별 범주
          label: "Data One",
          backgroundColor: "#f87979",
          pointBackgroundColor: "white",
          borderWidth: 1,
          pointBorderColor: "#249EBF",
          // 실제 데이터. labels와 배열 순서가 맞아야 함. 빈곳은 0으로 보정이 필요
          data: [40, 20, 30, 50, 90, 10, 20, 40, 50, 70, 90, 100],
        },
      ],
    },
    options: {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
            },
            gridLines: {
              display: true,
            },
          },
        ],
        xAxes: [
          {
            gridLines: {
              display: false,
            },
          },
        ],
      },
      legend: {
        display: true,
      },
      responsive: true,
      maintainAspectRatio: false,
    },
  }),
  mounted() {
    this.init()
  },
  methods: {
    init() {
      let data = this.chartData.chartData

      let datasets = []
      let pos = 0
      data.forEach((site) => {
        let colors = this.colorSets[pos]

        datasets.push({
          label: site.label,
          borderWidth: 2,
          borderColor: colors.back,
          backgroundColor: colors.back,
          pointBorderColor: colors.fore,
          pointBackgroundColor: colors.fore,
          fill: false,
          data: site.data,
        })

        pos++
      })

      this.datacollection = {
        labels: this.chartData.labels,
        datasets: datasets,
      }

      this.render()
    },
    render() {
      this.renderChart(this.datacollection, this.options)
    },
  },
}
</script>

<style scoped></style>
