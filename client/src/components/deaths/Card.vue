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
export default {
  name: 'Card',
  props: ['deathData', 'yearOne', 'yearTwo'],
  data() {
    return {

    }
  }
}
</script>

<style scoped>
/* .card {
  border: 2px solid black;
  margin: 10px;
  border-radius: 12px;
} */
</style>
