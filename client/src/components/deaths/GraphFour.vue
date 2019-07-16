<template>
  <div>

    <div class='cardDiv'>
      <v-card>
        <GChart
          type="PieChart"
          :data="chartDataThree"
          :options="chartOptions"
        />
      </v-card>
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
  methods: {
    ...mapActions([
      'fetchGraphFourData',
    ]),
  },
  mounted() {
    const payload = {
      'yearOne': '1960',
      'yearTwo': '1975'
    }
    this.fetchGraphFourData({payload})
  },
}
</script>

<style scoped>
.cardDiv {
  margin: 10px;
}
</style>
