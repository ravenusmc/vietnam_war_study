<template>
  <div>
    <h1>Graph One Area</h1>
  </div>
</template>

<script>
import * as d3 from 'd3';
import { mapActions } from 'vuex';
import { mapGetters } from 'vuex';

export default {
  name: 'GraphOne',
  computed: {
    buildGraph() {
      return this.vBarChartData = {
        chartType: "vBarChart",
        label: true,
        fill: 'green',
        selector: "vChart",
        title: "Roman Victories",
        subtitle: "By 75 Year Intervals",
        width: 500,
        height: 500,
        metric: ["Roman Victories", 'Total Battles'],
        dim: "Interval",
        data: this.graphOneData,
        grid: {
          enabled: true,
          gridTicks: 25,
        },
        overrides: {
          palette: {
            fill: ['#A91DEB', '#4fc08d'],
            stroke: '#41B883'
          },
          x: {
            ticks: 20
          },
          y: {
            axisWidth: 40,
          },
        },
        legends: {
          enabled: true,
          height: 5,
          width: 50,
        },
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
