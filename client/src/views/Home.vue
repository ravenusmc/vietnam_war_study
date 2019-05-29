<template>
  <div class="home">
    <Header/>
    <Main/>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from '@/components/home/Header.vue';
import Main from '@/components/home/Main.vue';

export default {
  name: 'home',
  components: {
    Header,
    Main,
  },
};
</script>
