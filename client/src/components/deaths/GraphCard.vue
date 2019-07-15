<template>
  <div>
    
    <div>
      <GChart
        :type="typeOne"
        :data="data"
        :options="options"
      />
    </div>

  </div>
</template>

<script>
import { GChart } from 'vue-google-charts'

export default {
  name: 'GraphCard',
  props: ['typeOne', 'data', 'options'],
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
