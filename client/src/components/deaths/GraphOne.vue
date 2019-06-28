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
  mounted() {
    this.fetchGraphOneData()
  },
}
</script>

<style scoped>
</style>
