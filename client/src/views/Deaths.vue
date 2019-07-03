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
        <GraphOne/>
      </div>

      <div>
        <h1>Talk Here</h1>
      </div>

      <div id='cardArea'>
        <Card
          :deathData='deathData'
          :yearOne='yearOne'
          :yearTwo='yearTwo'
          ></Card>
      </div>

      <div>
        <GraphTwo/>
      </div>

      <div>
        <GraphThree/>
      </div>

    </section>

  </div>
</template>

<script>
import Form from '@/components/deaths/Form.vue';
import Card from '@/components/deaths/Card.vue';
import GraphOne from '@/components/deaths/GraphOne.vue';
import GraphTwo from '@/components/deaths/GraphTwo.vue';
import GraphThree from '@/components/deaths/GraphThree.vue';

import { eventBus } from '../main';
import { mapActions } from 'vuex';
import { mapGetters } from 'vuex';

export default {
  components: {
    Form,
    Card,
    GraphOne,
    GraphTwo,
    GraphThree,
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
        'graphOneData',
    ]),
    getDeaths(){
      console.log(this.deathData)
      this.deaths = this.deathData
    }
  },
  methods: {
  ...mapActions([
      'fireActions',
    ]),
  },
  created() {
    eventBus.$on('dateData', (queryData) =>  {
      this.yearOne = queryData.yearOne
      this.yearTwo = queryData.yearTwo
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

#cardArea {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
