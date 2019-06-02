<template>
  <div>

    <router-view/>
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/deaths">Examining Deaths</router-link> |
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
      <hr>

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
      <hr>

      <div>
        <h2>Sections</h2>
      </div>
      <hr>

      <div>
        <img src='@/assets/img/gif_one.gif'>
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

hr {
  width: 10%;
  border-color: red;
}

</style>
