<template>
  <nav>

    <v-toolbar app absolute class="red accent-4">

      <v-toolbar-title class="text-uppercase grey--text">
        <span class='font-weight-light yellow--text'>Vietnam </span>
        <span class='yellow--text'>Study</span>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn color='yellow red--text' v-for="link in links" :key="link.text" router :to="link.route">
        {{ link.text }}
      </v-btn>

    </v-toolbar>

  </nav>
</template>

<script>
export default {
  data() {
    return {
      drawer: false,
      links: [
        {icon: 'dashboard', text: 'Home', route: '/'},
        {icon: 'person', text: 'Graphs', route: '/deaths'},
        {icon: 'folder', text: 'About Me', route: '/about'},
      ]
    }
  }
}
</script>

<style>
</style>
