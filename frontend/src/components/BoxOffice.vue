<template>
  <div>
    <h1>qkrtm</h1>
    <v-container fluid>
      <v-row>
        <v-col>
          <div
            class="text-lg-center pa-5"
            style="width: 100%"
            v-if="chartLoading"
          >
            <v-progress-circular
              width="7"
              size="70"
              indeterminate
              color="red"
            ></v-progress-circular>
          </div>
          <line-chart :chartData="chartData" v-if="!chartLoading" />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
// '@/components/Charts/LineChart' 사용 가능하면 대체를 해도 된다.
import LineChart from "@/components/LineChart"

export default {
  name: "BoxOffice",
  components: { LineChart },
  data: () => ({
    chartLoading: false, // 데이터를 불러오기 전까지는 progress circle을 사용
    chartData: [],
  }),
  mounted() {
    this.init()
  },
  methods: {
    init() {
      let item =
        '{"labels":["01","02","03","04","05","06","07","08","09","10","11"],"chartData":[{"label":"다음","data":["65","13","22","125","41","142","156","121","24","29","151"]},{"label":"다우존스","data":["1","1","0","6","1","3","6","8","0","0","6"]},{"label":"네이버","data":["65","13","22","119","41","139","150","119","20","28","147"]},{"label":"뉴스원","data":["61","7","17","105","28","128","138","108","10","20","137"]},{"label":"다나와","data":["0","0","0","1","0","0","1","0","0","0","0"]}]}'
      let data = JSON.parse(item)

      this.chartData = {
        labels: data.labels,
        chartData: data.chartData,
      }

      // 차트 보이기
      this.chartLoading = false
    },
  },
}
</script>

<style scoped></style>
