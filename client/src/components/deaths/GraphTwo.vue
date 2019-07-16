<template>
  <div>

    <div class='cardDiv'>
      <v-card>
        <GChart
          type="BarChart"
          :data="chartDataTwo"
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
    name: 'GraphTwo',
    data() {
      return {
        chartOptions: {
          title: 'Vietnam War Deaths By Branch',
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
        'graphTwoData',
      ]),
      chartDataTwo() {
        return this.graphTwoData
      },
    },
    methods: {
      ...mapActions([
        'fetchGraphTwoData',
      ]),
    },
    mounted() {
      const payload = {
        'yearOne': '1960',
        'yearTwo': '1975'
      }
      this.fetchGraphTwoData({payload})
    },
  }
</script>

<style scoped>
.cardDiv {
  margin: 10px;
}
</style>
