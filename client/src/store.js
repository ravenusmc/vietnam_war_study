import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import jsonp from 'jsonp';

Vue.use(Vuex);

export default new Vuex.Store({

  state: {
     deathData: 0,
  },

  getters: {
    deathData: state => state.deathData,
  },

  actions: {

    fireActions: ({ commit, dispatch }, payload) => {
      dispatch('fetchDeathData', { payload })
    },

    fetchDeathData: ({ commit }, {payload}) => {
      const path = 'http://localhost:5000/one';
      axios.post(path, payload)
      .then((res) => {
        commit('setDeathData', res.data);
      })
    }

  },

  mutations: {
    setDeathData(state, data) {
      state.deathData = data;
    },
  },

});
