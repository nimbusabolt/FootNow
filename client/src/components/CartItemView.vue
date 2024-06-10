<template>
  <div class="sidebar" :class="{ active: showCart }">
    <div v-if="cartItems.length > 0" class="cart-items">
      <div v-for="item in cartItems" :key="item.id" class="cart-item">
        <img
          :src="`/src/assets/${item.image}`"
          :alt="item.name"
          class="item-image"
        />
        <div class="item-details">
          <div class="item-name">
            <p>{{ item.name }}</p>
          </div>
          <div class="item-price">
            <p>$ {{ item.price }}</p>
          </div>
        </div>

        <div class="item-quantity">
          <p>{{ item.quantity }}</p>
        </div>
        <div class="item-delete">
          <i class="fa fa-trash" @click="deleteItem(item.name)"></i>
        </div>
      </div>
    </div>
    <a class="check-btn"><router-link to='/Checkout'>Checkout Now</router-link></a>
  </div>
</template>

<script>
import { mapState } from "vuex";
import axios from "../router/axios.js";

export default {
  name: "CartItemView",

  computed: {
    ...mapState(["showCart"]),
  },

  props: ["item"],
  data() {
    return {
      cartItems: [],
    };
  },

  mounted() {
    this.fetchCartItems();
  },

  methods: {
    async fetchCartItems() {
      try {
        const response = await axios.get("http://127.0.0.1:5000/cartitems");
        this.cartItems = response.data;
      } catch (error) {
        console.error("Error fetching cart items", error);
      }
    },

    async deleteItem(item) {
      try {
        const config = {
          headers: {
            "Content-Type": "application/json",
          },
          data: {
            item_name: item, // Assuming item name is accessible via this.item.name
          },
        };

        await axios.delete("http://127.0.0.1:5000/deleteitem", config);        
        this.$store.commit("toggleCart")
        alert("The item has been deleted.")
        this.$emit("item-deleted", item);
      } catch (error) {
        console.error("Error deleting item", error);
      }
    },
  },
};
</script>

<style scoped>
.sidebar {
  position: fixed;
  top: 100px;
  right: -300px; /* Initially off-screen */
  width: 300px;
  height: 100%;
  background-color: #f0f0f0;
  animation: slideOutRight 0.5s ease forwards;/* Animate transition */
}
@keyframes slideOutRight {
  from {
    right: -300px;
  }
  to {
    right: 0;
  }
}

.sidebar.hide {
  right: -300px; /* Slide out to the right */
  animation: slideInRight 1s ease forwards; /* Animate slide out */
}

@keyframes slideInRight {
  from {
    right: 0;
  }
  to {
    right: -300px;
  }
}

.sidebar.active {
  right: 0; /* Slide in from the right */
}

.item-image {
  height: 80px;
  width: 80px;
}
.cart-item {
 display:flex;
 align-items:center;
 padding:10px
}

.item-details{
  flex:1;
  margin-left:10px
}

.item-name{
  font-size:19px;
  font-weight:bold
}

.item-price {
  color:red;
  font-size:16px;
}
.item-quantity {
  font-size:20px;
  margin-right:10px
}

.item-delete {
  cursor:pointer;
  font-size:24px
}

.item-delete:hover {
  color:red
}

.check-btn {
  display:inline-block;
  width:60%;
  margin:10px 20%;
  font-size:23px;
  padding:10px;
  color:white ! important ;
  background-color:black;
  border:2px solid white;
}
.check-btn:hover {
  background-color: red;
}
</style>
