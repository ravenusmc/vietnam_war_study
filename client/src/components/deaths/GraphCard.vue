<template>
  <div>

    <div class='cardDiv'>
      <v-card>
        <GChart
          :type="typeOne"
          :data="data"
          :options="options"
        />
      </v-card>
    </div>

  </div>
</template>

<script>
import { GChart } from 'vue-google-charts'

export default {
  name: 'GraphCard',
  props: ['typeOne', 'data', 'options'],
}
</script>

<style scoped>
.cardDiv {
  margin: 10px;
}

</style>
