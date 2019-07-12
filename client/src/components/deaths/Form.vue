<template>
  <div>

    <header>
      <h1>Examining Deaths</h1>
      <p>
        The goal here is to see how deaths change through out a given time period.<br/>
        The initial years are set from 1960 to 1975.
      </p>
    </header>

    <section>

      <form @submit="submitYears">
        <h5>Select the Date by Year:</h5>
        <label>Year One:</label>
         <input type="number" v-model='yearOne' name="yearOne" placeholder="Enter First Year">&nbsp;
         <label>Year Two:</label>
         <input type="number" v-model="yearTwo" name="yearTwo" placeholder="Enter Second Year">
         <v-btn type="submit" color='yellow red--text'>
           Submit
         </v-btn>
         <!-- <div class='button_div'>
           <button class="btn btn-primary font" type="submit">Submit</button>
         </div> -->
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
      if (this.yearOne <= 1955){
        alert('The first year must be greater than 1955!')
      }else if (this.yearTwo >= 1976){
        alert('The second year must not be greater than 1975!')
      }else if (this.yearOne >= this.yearTwo){
        alert('The first year must be less than the second year!')
      }else if (this.yearTwo <= this.yearOne){
        alert('The second year must be greater than the first year!')
      }else {
        const queryData = {
          yearOne: this.yearOne,
          yearTwo: this.yearTwo,
        };
        eventBus.$emit('dateData', queryData);
      }
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

button {
  background-color: #F90303;
  border-color: #F90303;
  padding: 12px;
  border-radius: 12px;
}

button:hover {
  color: #F90303;
  border-color: #EEF903;
  background-color: #EEF903;
}

</style>
