<template>
  <div>

    <router-view/>
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/deaths">Graphs</router-link> |
      <router-link to="/about">About</router-link>
    </div>

    <section class='title_section'>

      <h2>Vietnam Study</h2>
      <p>
        The Vietnam War was a great tragedy for our country. And it is now far
        enough away so that one can study without using the slogans to what's
        really happened.
        <b>-Henry Kissinger</b>
      </p>

      <div>
        <h2>Purpose</h2>
        <p>
          The purpose of this project is to examine data about the Vietnam War.
          Most of my life I've been very interested in Vietnam - it could have
          been because my father as a Vietnam Veteran. To me, the war holds so many
          lessons that really need to be drilled into not only politicians but the
          general public as well. In many ways, this project is me taking the next
          step in learning about Vietnam.
        </p>
      </div>

      <div>
        <h2>Sections</h2>

        <div id='sectionArea'>

          <v-card>
            <v-img
              src="https://images.unsplash.com/photo-1543286386-713bdd548da4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60"
              aspect-ratio="1.0"></v-img>

            <v-card-title primary-title>
              <div>
                <h3 class="headline mb-0">Graphs</h3>
              </div>
            </v-card-title>

            <v-card-actions>
              <v-btn flat color="orange"><router-link to="/deaths">Explore</router-link></v-btn>
            </v-card-actions>
          </v-card>

          <v-card>
            <v-img
              src="https://images.unsplash.com/photo-1531737212413-667205e1cda7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60"
              aspect-ratio="1.0"></v-img>

            <v-card-title primary-title>
              <div>
                <h3 class="headline mb-0">About</h3>
              </div>
            </v-card-title>

            <v-card-actions>
              <v-btn flat color="orange"><router-link to="/about">About Me</router-link></v-btn>
            </v-card-actions>
          </v-card>

        </div>

      </div>

      <div class='gif_div'>
        <img class='gif_image' src='@/assets/img/gif_one.gif'>
      </div>

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
  margin-left: 10%;
  margin-right: 10%;
  margin-top: 15px;
  font-size: 2rem;
  font-weight: 100;
  line-height: normal;
  font-family: Benton Sans,Helvetica Neue,Helvetica,Arial,sans-serif;
}

.gif_image {
  height: 400px;
  width: 80%;
}

#sectionArea {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 2em;
  margin-top: 50px;
  margin-bottom: 100px;
}

@media only all and (max-width: 950px){

  #sectionArea {
    grid-template-columns: 1fr;
  }

}


</style>
