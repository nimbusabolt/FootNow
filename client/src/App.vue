<template>
  <Navbar />
  <RouterView />
  <CartItemView v-if="showCart"  :cartItems="cartItems" @item-deleted="handleItemDeleted(item)" />
  <Footer />
</template>

<script>
import { RouterLink, RouterView } from "vue-router";
import Navbar from "./components/Navbar.vue";
import Footer from "./components/Footer.vue";
import CartItemView from "./components/CartItemView.vue";
import { mapState } from "vuex";
import axios from "./router/axios.js";

export default {
  data(){
    return{
      cartItems:[]
    }
  },

  methods: {
    async fetchCartItems() {
      // Fetch cart items from the backend
      try {
        const response = await axios.get('http://127.0.0.1:5000/cartitems');
        this.cartItems = response.data;
      } catch (error) {
        console.error('Error fetching cart items', error);
      }
    },
    async handleItemDeleted(deletedItem) {
      // Remove deleted item from cartItems array
      this.cartItems = this.cartItems.filter(item => item.id !== deletedItem.id);
    }
  },
  components: {
    Navbar,
    Footer,
    CartItemView,
  },

  computed: {
    ...mapState(["showCart"]),
  },
};
</script>
