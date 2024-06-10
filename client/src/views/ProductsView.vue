<template>
  
  <section class="products" id="products">
    <div class="products-container">
      <div class="product-grid">
        <div
          v-for="(product, index) in displayedProducts"
          :key="product.id"
          class="product-block"
        >
          <img
          :src="`/src/assets/${product.image}`"
            alt="Product Image"
            class="product-image"
          />
          <h3 class="product-name">{{ product.name }}</h3>
          <p class="product-price">Price: <span style="color:red; font-size:13pt">${{ product.price }}</span> </p>
          <p class="product-stock">Stock: {{ product.stock }}</p>
          <button @click="addToCart(product)" class="add-to-cart">
            <i class="fas fa-shopping-cart fa-2x"></i>
          </button>
        </div>
      </div>
      <button v-if="!showAll" @click="showAllProducts" class="show-more">
        Show More
      </button>
    </div>
  </section>
 
</template>
<script>
import axios from "../router/axios.js";
import store from '../store.js'

export default {
  data() {
    return {
      products_array: [],
      displayedProducts: [],
      showAll: false,
    };
  },

  mounted() {
    this.fetchProducts();
  },

  methods: {
    fetchProducts() {
      axios
        .get("http://127.0.0.1:5000/products")
        .then((response) => {
          this.products_array = response.data;
          this.displayedProducts = this.products_array.slice(0, 6);
          console.log(this.products_array);
        })
        .catch((error) => {
          console.error("Error fetching products", error);
        });
    },

    showAllProducts() {
      this.showAll = true;
      this.displayedProducts = this.products_array;
    },

    addToCart(product) {
      const token = localStorage.getItem("token");      
      if (!token) {
        alert("You need to sign in to add items to the cart.");
        this.$router.push("/signin");
        return;
      }

      axios
        .post("http://127.0.0.1:5000/additem", { productId: product.id })
        .then((response) => {
          alert("Product added to cart");
          this.$store.commit("toggleCart")
        })
        .catch((error) => {
          console.error("Error adding to cart:", error);
          alert("Failed to add product to cart.");
        });
    },

    getImageSrc(imageName) {
      return `../assets/${imageName}`;
    },
  },

  name: "ProductsView",
  components: {
    
  },
};
</script>

<style scoped>
.products-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 50px;
  background-color: black;
  color: white;
  font-size: 15px;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  width: 100%;
}

.product-block {
  border: 1px solid #ddd;
  padding: 20px;
  text-align: center;
  background-color: #000000;
}

.product-image {
  width: 100%;
  height:60%;
  padding-bottom: 10px; /* 2:3 aspect ratio */
  background-size: cover;
  background-position: center;
}

.product-name {
  margin: 10px 0;
  font-size: 1.2em;
}

.product-price,
.product-stock {
  margin: 5px 0;
}

.add-to-cart {
  margin-top: 10px;
  padding: 10px 20px;
  color: #fff;
  background-color: #000000;
  border: none;
  cursor: pointer;
  border:1px solid white
}

.add-to-cart:hover {
  background-color: red
}

.show-more {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #000000;
  color: #ffffff;
  border: none;
  cursor: pointer;
  font-size: xx-large;
  width: 20%;
}

.show-more:hover {
  background-color: red 
}

@media (max-width: 768px) {
  .product-grid {
    grid-template-columns: 1fr; /* One item per row on small screens */
  }

  .show-more {
    width:50%;
    font-size: large; /* Adjust font size for smaller screens */
  }
}
</style>
