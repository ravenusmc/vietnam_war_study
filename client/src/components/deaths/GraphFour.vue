<template>
  <div>

    <div>
      <GChart
        type="PieChart"
        :data="chartDataThree"
        :options="chartOptions"
      />
    </div>


  </div>
</template>

<script>
import { GChart } from 'vue-google-charts'
import { mapActions } from 'vuex';
import { mapGetters } from 'vuex';

export default {
  name: 'GraphFour',
  data() {
    return {
      chartOptions: {
        title: 'Vietnam War Deaths By Race',
        legend: { position: 'bottom' },
        'height':300,
        pieHole: 0.4,
      },
    }
  },
  computed: {
    ...mapGetters([
      'graphFourData',
    ]),
    chartDataThree() {
      return this.graphFourData
    },
  },
}
</script>

<style scoped>
</style>
