<template>
  <div>
    <form @submit="submitYears">
      <h5>Select the Date:</h5>
      <label>Year One:</label>
       <input type="number" v-model='yearOne' name="yearOne" placeholder="Enter First Year">
       <label>Year Two:</label>
       <input type="number" v-model="yearTwo" name="yearTwo" placeholder="Enter Second Year">
       <div>
         <button class="btn btn-primary font" type="submit">Submit</button>
       </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'name',
  data() {
    return {
      yearOne: 0,
      yearTwo: 0,
    };
  },
  methods: {
    submitYears(evt) {
      evt.preventDefault();
      alert('Mike')
    }
  }
}
</script>

<style scoped>
</style>
