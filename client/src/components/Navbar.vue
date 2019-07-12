<template>
  <nav>

    <v-toolbar app>

      <v-toolbar-title class="text-uppercase grey--text">
        <span class='font-weight-light'>Vietnam</span>
        <span>Study</span>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn color='grey'>
        <span>Home</span>
      </v-btn>

    </v-toolbar>

    <v-navigation-drawer app v-model='drawer' class='primary'>
      <v-list>
        <v-list-tile v-for="link in links" :key="link.text" router :to="link.route">
          <v-list-tile-action>
            <v-icon class='white--text'>{{ link.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title class='white--text'>{{ link.text }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>

  </nav>
</template>

<script>
export default {
  data() {
    return {
      drawer: false,
      links: [
        {icon: 'dashboard', text: 'Dashboard', route: '/'},
        {icon: 'folder', text: 'My Projects', route: '/projects'},
        {icon: 'person', text: 'Team', route: '/team'},
      ]
    }
  }
}
</script>

<style>
</style>
