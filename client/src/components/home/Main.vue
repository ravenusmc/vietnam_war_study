<template>
  <div>
    <router-view/>
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <section class='title_section'>
      <h1>Vietnam Study</h1>
    </section>
  </div>
</template>

<script>
export default {
  name: "Main",
}
</script>

<style scoped>

.title_section {
  margin-top: 100px;
}

</style>
