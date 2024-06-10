// store.js
import {createApp} from 'vue';
import Vuex from 'vuex';

const app=createApp({})
app.use(Vuex);

export default new Vuex.Store({
  state: {
    showCart: false,
    isLoggedIn:false
  },
  mutations: {
    toggleCart(state) {
      state.showCart = !state.showCart;
    },

    setLoggedIn(state, isLoggedIn) {
      state.isLoggedIn=isLoggedIn
    }
  },

  getters:{
    showCart(state) {
        return state.showCart
    }
  }
});
