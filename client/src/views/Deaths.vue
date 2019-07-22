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
        <Talk/>
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

      <div>
        <GraphFour/>
      </div>

      <div>
        <GraphCard
          :typeOne='typeOne'
          :data='graphFiveData'
          :options='chartOptionsFive'>
        </GraphCard>
      </div>

      <div>
        <GraphCard
          :typeOne='typeOne'
          :data='graphSevenData'
          :options='chartOptionsSeven'>
        </GraphCard>
      </div>

      <div>
        <GraphCard
          :typeOne='typeOne'
          :data='graphSixData'
          :options='chartOptionsSix'>
        </GraphCard>
      </div>

      <div>
        <GraphCard
          :typeOne='typeOne'
          :data='graphEightData'
          :options='chartOptionsEight'>
        </GraphCard>
      </div>

      <div>
        <GraphCard
          :typeOne='typeTwo'
          :data='graphNineData'
          :options='chartOptionsNine'>
        </GraphCard>
      </div>

    </section>

  </div>
</template>

<script>
import Form from '@/components/deaths/Form.vue';
import Card from '@/components/deaths/Card.vue';
import Talk from '@/components/deaths/Talk.vue';
import GraphOne from '@/components/deaths/GraphOne.vue';
import GraphTwo from '@/components/deaths/GraphTwo.vue';
import GraphThree from '@/components/deaths/GraphThree.vue';
import GraphFour from '@/components/deaths/GraphFour.vue';
import GraphCard from '@/components/deaths/GraphCard.vue';

import { eventBus } from '../main';
import { mapActions } from 'vuex';
import { mapGetters } from 'vuex';

export default {
  components: {
    Form,
    Card,
    Talk,
    GraphOne,
    GraphTwo,
    GraphThree,
    GraphFour,
    GraphCard,
  },
  data() {
    return {
      deaths: 0,
      yearOne: 1960,
      yearTwo: 1975,
      typeOne: "BarChart",
      typeTwo: "PieChart",
      chartOptionsFive: {
        title: 'Vietnam War Deaths By Enlisted Rank',
        legend: { position: 'bottom' },
        'height':300,
        vAxis: { viewWindow: {
          min:0
        }}
      },
      chartOptionsSix: {
        title: 'Vietnam War Deaths By Officer Rank',
        legend: { position: 'bottom' },
        'height':300,
        vAxis: { viewWindow: {
          min:0
        }}
      },
      chartOptionsSeven: {
        title: 'Vietnam War Deaths By Warrant Officer Rank',
        legend: { position: 'bottom' },
        'height':300,
        vAxis: { viewWindow: {
          min:0
        }}
      },
      chartOptionsEight: {
        title: 'Vietnam War Deaths By Combat MOS',
        legend: { position: 'bottom' },
        'height':300,
        vAxis: { viewWindow: {
          min:0
        }}
      },
      chartOptionsNine: {
        title: 'Vietnam War Deaths By Marital Status',
        legend: { position: 'bottom' },
        'height':300,
        vAxis: { viewWindow: {
          min:0
        }}
      },
    }
  },
  computed: {
    ...mapGetters([
        'deathData',
        'graphOneData',
        'graphFiveData',
        'graphSixData',
        'graphSevenData',
        'graphEightData',
        'graphNineData',
    ]),
    getDeaths(){
      this.deaths = this.deathData
    }
  },
  methods: {
  ...mapActions([
      'fireActions',
      'fireActionsTwo',
    ]),
  },
  created() {
    eventBus.$on('dateData', (queryData) =>  {
      this.yearOne = queryData.yearOne
      this.yearTwo = queryData.yearTwo
      this.fireActions(queryData)
    })
  },
  mounted() {
    const payload = {
      'yearOne': '1960',
      'yearTwo': '1975'
    }
    this.fireActionsTwo({payload})
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
}

#cardArea {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

@media only all and (max-width: 950px){

  #infoArea {
    grid-template-columns: 1fr;
  }

}
</style>
