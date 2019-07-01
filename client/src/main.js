import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import VueMaterial from 'vue-material';
import 'vue-material/dist/vue-material.min.css';
import Chart from 'v-chart-plugin'
import VueGoogleCharts from 'vue-google-charts'

Vue.config.productionTip = false;

//Material design
Vue.use(VueMaterial)
//V-chart plugin
Vue.use(Chart);
//Google charts plugin
Vue.use(VueGoogleCharts)

//Vue bus
export const eventBus = new Vue();

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
