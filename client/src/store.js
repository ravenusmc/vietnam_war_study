import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import jsonp from 'jsonp';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
     deathData: {},
  },

  getters: {
    deathData: state => state.graphOneData,
  },

  mutations: {

  },

  actions: {

    fireActions: ({ commit, dispatch}, payload) => {
      dispatch('fetchDeathData', { payload})
    },

    fetchDeathData: ({ commit }, {payload}) => {
      const path = 'http://localhost:5000/one';
      axios.post(path, payload)
      .then((res) => {

        // commit('setGraphOneData', res.data);
      })
    }
  },

});
