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

export default {
  components: {
    Form,
  }
}
</script>

<style scoped>
</style>
