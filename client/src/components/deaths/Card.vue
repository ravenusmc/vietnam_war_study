<template>
  <div>

    <div class='card'>
      <h3>Vietnam Deaths between {{ yearOne }} and {{ yearTwo }}</h3>
      <p>{{deathData}}</p>
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
.card {
  border: 2px solid black;
  margin: 10px;
  border-radius: 12px;
}
</style>
