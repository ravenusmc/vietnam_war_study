<template>
  <div>

    <h1>{{ typeOne }}</h1>
    <div>
      <GChart
        type="TypeOne"
        :data="chartDataThree"
        :options="chartOptions"
      />
    </div>

  </div>
</template>

<script>
export default {
  name: 'GraphCard',
  props: ['typeOne'],
}
</script>

<style scoped>
</style>
