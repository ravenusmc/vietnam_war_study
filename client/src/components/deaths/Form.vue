<template>
  <div>

    <section>

      <form @submit="submitYears">
        <h5>Select the Date by Year:</h5>
        <label>Year One:</label>
         <input type="number" v-model='yearOne' name="yearOne" placeholder="Enter First Year">&nbsp;
         <label>Year Two:</label>
         <input type="number" v-model="yearTwo" name="yearTwo" placeholder="Enter Second Year">
         <div class='button_div'>
           <button class="btn btn-primary font" type="submit">Submit</button>
         </div>
      </form>

    </section>

  </div>
</template>

<script>
import { eventBus } from '../../main';

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
      const queryData = {
        yearOne: this.yearOne,
        yearTwo: this.yearTwo,
      };
      eventBus.$emit('dateData', queryData);
    }
  }
}
</script>

<style scoped>

section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

form {
  border: 2px solid black;
  padding: 15px;
  box-shadow: 5px 8px #888888;
  border-radius: 10px;
}

.button_div {
  margin-top: 10px;
}
</style>
