<template>
  <div>

    <router-view/>
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/deaths">Examining Deaths</router-link> |
      <router-link to="/about">About</router-link>
    </div>

    <Form/>
  </div>
</template>

<script>
import Form from '@/components/deaths/Form.vue';
import { eventBus } from '../main';
import { mapActions } from 'vuex';

export default {
  components: {
    Form,
  },
  methods: {
  ...mapActions([
      'fetchGraphOneData',
    ]),
  },
  created() {
    eventBus.$on('dateData', (queryData) =>  {
      console.log(queryData)
      this.fetchGraphOneData(queryData)
    })
  },
}
</script>

<style scoped>
</style>
