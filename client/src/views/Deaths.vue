<template>
  <div>

    <router-view/>
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/deaths">Examining Deaths</router-link> |
      <router-link to="/about">About</router-link>
    </div>

    <Form/>

    <p>See Me!</p>
    <p>{{ getDeaths }}</p>
    <h1>{{deaths}}</h1>
  </div>
</template>

<script>
import Form from '@/components/deaths/Form.vue';
import { eventBus } from '../main';
import { mapActions } from 'vuex';
import { mapGetters } from 'vuex';

export default {
  components: {
    Form,
  },
  data() {
    return {
      deaths: 0,
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
      this.fireActions(queryData)
    })
  },
}
</script>

<style scoped>
</style>
