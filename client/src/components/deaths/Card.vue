<template>
  <div>

    <v-card>
      <v-card-title primary-title>
        <div>
          <h3 class="headline mb-0">Vietnam War Deaths</h3>
          <div> {{ yearOne }} - {{ yearTwo }} </div>
          <p class="card-text">{{deathData}}</p>
        </div>
      </v-card-title>
    </v-card>

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
