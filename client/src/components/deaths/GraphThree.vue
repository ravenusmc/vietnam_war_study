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
  name: 'GraphThree',
  data() {
    return {
      chartOptions: {
        title: 'Vietnam War Deaths By Religion',
        legend: { position: 'bottom' },
        'height':300,
        is3D: true,
      },
    }
  },
  computed: {
    ...mapGetters([
      'graphThreeData',
    ]),
    chartDataThree() {
      return this.graphThreeData
    },
  },
  methods: {
    ...mapActions([
      'fetchGraphThreeData',
    ]),
  },
  mounted() {
    const payload = {
      'yearOne': '1960',
      'yearTwo': '1975'
    }
    this.fetchGraphThreeData({payload})
  },
}
</script>

<style scoped>
</style>
