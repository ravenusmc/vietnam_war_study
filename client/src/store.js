import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import jsonp from 'jsonp';

Vue.use(Vuex);

export default new Vuex.Store({

  state: {
     deathData: 0,
     graphOneData: {},
     graphTwoData: {},
  },

  getters: {
    deathData: state => state.deathData,
    graphOneData: state => state.graphOneData,
    graphTwoData: state => state.graphTwoData,
  },

  actions: {

    //This is the main action that will fire that rest of the actions when the
    //user hits the submit button.
    fireActions: ({ commit, dispatch }, payload) => {
      dispatch('fetchDeathData', { payload })
      dispatch('fetchGraphOneData')
      dispatch('fetchGraphTwoData', { payload })
    },

    //This action will get the data for the number of deaths between two years
    //that the user enters.
    fetchDeathData: ({ commit }, {payload}) => {
      const path = 'http://localhost:5000/one';
      axios.post(path, payload)
      .then((res) => {
        commit('setDeathData', res.data);
      })
    },

    //This action will get the data for the first chart that will show total
    //deaths in Vietnam.
    fetchGraphOneData: ({commit}) => {
      const path = 'http://localhost:5000/firstGraph';
      axios.get(path)
      .then((res) => {
        //for (let i = 1; i <= res.data.length; i++){
          //console.log(res.data[i][0])
          //res.data[i][0].toString()
        //}
        commit('setGraphOneData', res.data)
      })
    },

    //This action will get the data for the second chart.
    fetchGraphTwoData: ({ commit }, { payload }) => {
      console.log(payload)
    }

  },

  mutations: {
    setDeathData(state, data) {
      state.deathData = data;
    },
    setGraphOneData(state, data){
      state.graphOneData = data;
    },
  },

});
