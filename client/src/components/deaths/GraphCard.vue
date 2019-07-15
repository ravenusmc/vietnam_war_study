<template>
  <div>

    <!-- <h1>{{ data }}</h1> -->
    <h1>{{ typeOne }}</h1>
    <div>
      <GChart
        :type="typeOne"
        :data="data"
        :options="chartOptions"
      />
    </div>

  </div>
</template>

<script>
import { GChart } from 'vue-google-charts'

export default {
  name: 'GraphCard',
  props: ['typeOne', 'data'],
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
}
</script>

<style scoped>
</style>
