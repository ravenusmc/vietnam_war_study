<template>
  <div>

    <div>
      <GChart
        type="LineChart"
        :data="chartData"
        :options="chartOptions"
      />
    </div>
    
  </div>
</template>

<script>
import * as d3 from 'd3';
import { GChart } from 'vue-google-charts'
import { mapActions } from 'vuex';
import { mapGetters } from 'vuex';

export default {
  name: 'GraphOne',
  data() {
    return {
      height: 600,
      width: 600,
      vBarChartData: [],
      chartOptions: {
        title: 'Vietnam War Deaths',
        curveType: 'function',
        legend: { position: 'bottom' }
      },
    }
  },
  computed: {
    ...mapGetters([
      'graphOneData',
    ]),
    chartData() {
      return this.graphOneData
    },
    buildGraph() {
      return this.lineGraphData = {
        chartType: "lineGraph",
        selector: "lineGraph",
        label: true,
        // fill: 'green',
        title: "Vietnam War Deaths",
        width: 500,
        height: 500,
        metric: ["Deaths"],
        dim: "Deaths",
        data: this.graphOneData,
        grid: {
          enabled: true,
          gridTicks: 25,
        },
        // overrides: {
        //   palette: {
        //     fill: ['#A91DEB', '#4fc08d'],
        //     stroke: '#41B883'
        //   },
        //   x: {
        //     ticks: 20
        //   },
        //   y: {
        //     axisWidth: 40,
        //   },
        // },
        // legends: {
        //   enabled: true,
        //   height: 5,
        //   width: 50,
        // },
      }
    }
  },
  methods: {
    ...mapActions([
      'fetchGraphOneData',
    ]),
  },
  mounted() {
    this.fetchGraphOneData()
  },
}
</script>

<style scoped>
</style>
