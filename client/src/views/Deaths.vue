<template>
  <div>

    <router-view/>
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/deaths">Examining Deaths</router-link> |
      <router-link to="/about">About</router-link>
    </div>

    <Form/>

    <section id='infoArea'>

      <div>
        <Card
          :deathData='deathData'
          :yearOne='yearOne'
          :yearTwo='yearTwo'
          ></Card>
      </div>

      <div>
      </div>

    </section>
    
  </div>
</template>

<script>
import Form from '@/components/deaths/Form.vue';
import Card from '@/components/deaths/Card.vue';
import { eventBus } from '../main';
import { mapActions } from 'vuex';
import { mapGetters } from 'vuex';

export default {
  components: {
    Form,
    Card,
  },
  data() {
    return {
      deaths: 0,
      yearOne: 0,
      yearTwo: 0,
    }
  },
  computed: {
    ...mapGetters([
        'deathData',
    ]),
    getDeaths(){
      console.log(this.deathData)
      this.deaths = this.deathData
    }
  },
  methods: {
  ...mapActions([
      'fireActions',
      'fetchDeathData',
    ]),
  },
  created() {
    eventBus.$on('dateData', (queryData) =>  {
      this.yearOne = queryData.yearOne
      this.yearTwo = queryData.yearTwo
      console.log(queryData.yearOne)

      this.fireActions(queryData)
    })
  },
}
</script>

<style scoped>
#infoArea {
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin-top: 100px;
  margin-left: 5%;
  margin-right: 5%;
  border: 2px solid red;
}

</style>
