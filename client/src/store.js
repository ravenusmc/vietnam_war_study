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
     graphThreeData: {},
     graphFourData: {},
     graphFiveData: {},
     graphSixData: {},
     graphSevenData: {},
  },

  getters: {
    deathData: state => state.deathData,
    graphOneData: state => state.graphOneData,
    graphTwoData: state => state.graphTwoData,
    graphThreeData: state => state.graphThreeData,
    graphFourData: state => state.graphFourData,
    graphFiveData: state => state.graphFiveData,
    graphSixData: state => state.graphSixData,
    graphSevenData: state => state.graphSevenData,
  },

  actions: {

    //This is the main action that will fire that rest of the actions when the
    //user hits the submit button.
    fireActions: ({ commit, dispatch }, payload) => {
      dispatch('fetchDeathData', { payload })
      dispatch('fetchGraphOneData')
      dispatch('fetchGraphTwoData', { payload })
      dispatch('fetchGraphThreeData', { payload })
      dispatch('fetchGraphFourData', { payload })
      dispatch('fetchGraphFiveData', { payload })
      dispatch('fetchGraphSixData', { payload })
      dispatch('fetchGraphSevenData', {payload})
    },

    fireActionsTwo: ({ dispatch }, payload) => {
      dispatch('fetchGraphFiveData', payload)
      dispatch('fetchGraphSixData', payload)
      dispatch('fetchGraphSevenData', payload)
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
        commit('setGraphOneData', res.data)
      })
    },

    //This action will get the data for the second chart.
    fetchGraphTwoData: ({ commit }, { payload }) => {
        const path = 'http://localhost:5000/secondGraph';
        axios.post(path, payload)
        .then((res) => {
          commit('setGraphTwoData', res.data)
        })
    },

    //This action will get the data for the third chart.
    fetchGraphThreeData: ({ commit }, { payload }) => {
      const path = 'http://localhost:5000/thirdGraph';
      axios.post(path, payload)
      .then((res) => {
        commit('setGraphThreeData', res.data)
      })
    },

    //This action will get the data for the fourth chart.
    fetchGraphFourData: ({ commit }, { payload }) => {
      const path = 'http://localhost:5000/fourthGraph';
      axios.post(path, payload)
      .then((res) => {
        commit('setGraphFourData', res.data)
      })
    },

    //This action will get the data for the fifth chart
    fetchGraphFiveData: ({ commit }, {payload }) => {
      const path = 'http://localhost:5000/fifthGraph';
      axios.post(path, payload)
      .then((res) => {
        commit('setGraphFiveData', res.data)
      })
    },

    //This action will get the data for six chart
    fetchGraphSixData: ({ commit }, {payload}) => {
      const path = 'http://localhost:5000/sixthGraph';
      axios.post(path, payload)
      .then((res) => {
        commit('setGraphSixData', res.data)
      })
    },

    //This action will get the data for the seventh chart
    fetchGraphSevenData: ({ commit }, { payload }) => {
      const path = 'http://localhost:5000/seventhGraph';
      axios.post(path, payload)
      .then((res) => {
        commit('setGraphSevenData', res.data)
      })
    },

  },

  mutations: {
    setDeathData(state, data) {
      state.deathData = data;
    },
    setGraphOneData(state, data){
      state.graphOneData = data;
    },
    setGraphTwoData(state, data){
      state.graphTwoData = data;
    },
    setGraphThreeData(state, data){
      state.graphThreeData = data;
    },
    setGraphFourData(state, data){
      state.graphFourData = data;
    },
    setGraphFiveData(state, data){
      state.graphFiveData = data;
    },
    setGraphSixData(state, data){
      state.graphSixData = data
    },
    setGraphSevenData(state, data){
      state.graphSevenData = data
    }
  },

});
