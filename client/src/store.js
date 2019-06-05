import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import jsonp from 'jsonp';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
     graphOneData: {},
  },

  getters: {
    graphOneData: state => state.graphOneData,
  },

  mutations: {

  },

  actions: {
    fetchGraphOneData: ({ commit }, payload) => {
      const path = 'http://localhost:5000/graphOne';
      axios.post(path, payload)
      .then((res) => {
        console.log("mike")
        // commit('setGraphOneData', res.data);
      })
    }
  },

});
