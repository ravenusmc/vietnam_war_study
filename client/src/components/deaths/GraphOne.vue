<template>
  <div>

    <div class='cardDiv'>
      <v-card>
        <GChart
          type="LineChart"
          :data="chartData"
          :options="chartOptions"
        />
      </v-card>
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
      chartOptions: {
        title: 'Vietnam War Deaths',
        curveType: 'function',
        legend: { position: 'bottom' },
        'height':300,
        vAxis: { viewWindow: {
          min:0
        }}
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
.cardDiv {
  margin: 10px;
}
</style>
