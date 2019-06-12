import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import jsonp from 'jsonp';

Vue.use(Vuex);

export default new Vuex.Store({

  state: {
     deathData: 0,
     graphOneData: {},
  },

  getters: {
    deathData: state => state.deathData,
    graphOneData: state => state.graphOneData,
  },

  actions: {

    //This is the main action that will fire that rest of the actions when the
    //user hits the submit button.
    fireActions: ({ commit, dispatch }, payload) => {
      dispatch('fetchDeathData', { payload })
      dispatch('fetchGraphOneData')
    },

    fetchDeathData: ({ commit }, {payload}) => {
      const path = 'http://localhost:5000/one';
      axios.post(path, payload)
      .then((res) => {
        commit('setDeathData', res.data);
      })
    },

    fetchGraphOneData: ({commit}) => {
      console.log('fired')
      const path = 'http://localhost:5000/firstGraph';
      axios.post(path)
      .then((res) => {
        console.log('Mike')
      })
    },

  },

  mutations: {
    setDeathData(state, data) {
      state.deathData = data;
    },
    setGraphOneData(state, data){
      state.graphOneData = data;
    }
  },

});
