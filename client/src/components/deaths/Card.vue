<template>
  <div>

    <div class="card" style="width: 18rem;">
      <div class="card-body">
        <h5 class="card-title">Vietnam Deaths</h5>
        <h6 class="card-subtitle mb-2 text-muted">{{ yearOne }} - {{ yearTwo }}</h6>
        <p class="card-text">{{deathData}}</p>
      </div>
    </div>

  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'Card',
  props: ['deathData', 'yearOne', 'yearTwo'],
  methods: {
    ...mapActions([
      'fetchDeathData',
    ]),
  },
  mounted() {
    const payload = {
      'yearOne': '1960',
      'yearTwo': '1975'
    }
    this.fetchDeathData({payload})
  },
}
</script>

<style scoped>
.card {
  border: 2px solid black;
  margin: 10px;
  border-radius: 12px;
}
</style>
