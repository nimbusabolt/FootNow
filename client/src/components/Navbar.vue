<template>
  <header class="header">
    <a class="logo">
      <router-link to="/">
        <img src="../assets/Logo.png" alt="" />
      </router-link>
    </a>

    <nav class="navbar" :class="{ open: isMenuOpen }">
      <a><router-link to="/">Home</router-link></a>
      <a><router-link to="/about">About</router-link></a>
      <a><router-link to="/products">Products</router-link></a>
      <a><router-link to="/review">Review</router-link></a>
      <a><router-link to="/contact">Contact</router-link></a>
      <a><router-link to="/blogs">Blogs</router-link></a>
    </nav>

    <nav class="navbar auth-links" :class="{ open: isMenuOpen }">
      <template v-if="isLoggedIn">
        <a @click="logout" class="logout_button">Logout</a>
      </template>
      <template v-else>
        <a> <router-link to="/signin">Sign in</router-link></a>
        <a><router-link to="/signup">Sign up</router-link></a>
      </template>
    </nav>

    <div class="icons">
      <div class="fas fa-search" id="search-btn" @click="toggleSearch"></div>
      <div class="fas fa-shopping-cart" id="cart-btn" @click="toggleCart"></div>
      <div class="fas fa-bars" id="menu-btn" @click="toggleMenu"></div>
    </div>

    <form v-show="showSearchForm" class="search">
      <input type="search" id="search-box" placeholder="search here..." />
      <label for="search-box" class="fas fa-search search-icon"></label>
    </form>
  </header>
</template>
<script>
import SearchBar from "@/components/SearchBar.vue";
import axios from "../router/axios.js";
import { mapState } from "vuex";

export default {
  computed: {
    ...mapState(["isLoggedIn"]),
  },

  data() {
    return {
      showSearchForm: false,
      isMenuOpen:false
    };
  },
  mounted() {
    this.checkToken();
  },
  name: "Navbar",
  components: {
    SearchBar,
  },
  methods: {
    checkToken() {
      const token = localStorage.getItem("token");
      if (token) {
        // Token exists, user is logged in
        this.$store.commit("setLoggedIn", true);
      } else {
        // No token, user is not logged in
        this.$store.commit("setLoggedIn", false);
      }
    },
    logout() {
      localStorage.removeItem("token");
      this.$store.commit("setLoggedIn", false);
      this.$router.push({ name: "Home" });
    },

    toggleCart() {
      const token = localStorage.getItem("token");
      if (token) {
        this.$store.commit("toggleCart");
      } else {
        alert("You have to sign in to see your cart items.")
        this.$router.push({ name: "Signin" });
      }
    },
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },

    toggleSearch() {
      this.showSearchForm = !this.showSearchForm;
    },
  },
};
</script>
<style>
.header {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.navbar a { 
  text-decoration: none;
  color: var(--black);
}

.navbar {
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.navbar.auth-links {
  margin-left: auto;
}

.navbar.open {
  display: block;
}

.icons {
  display: flex;
  justify-content: space-around;
  align-items: center;
}

#menu-btn {
  cursor: pointer;
  display:none;
}

@media (max-width: 768px) {

  #menu-btn {
    display: inline-block; /* Show the menu button on small screens */
  }

  .navbar {
    display: none; /* Hide navbar by default on small screens */
    flex-direction: column; /* Stack the links vertically */
    background-color: #000000; /* Background color for the navbar */
    position: absolute;
    top: 100%;
    left: 70%;
    width: 30%;
    z-index: 1000;
    
  }

  .navbar a {
    display:block;
    padding: 1rem;
    text-align: center;
    font-size: 1.5rem;
    color: var(--black);
  }

  .navbar.open {
    display: flex; /* Show navbar when menu is open */
  }

  .icons {
    margin-left: auto; /* Push icons to the right on small screens */
  }
}

.logout_button {
  background-color: black;
  color: white;
  border: none;
  text-decoration: none;
  padding: 5px 10px;
  transition: font-size 0.1s, border-bottom 0.1s;
  font-size: 1.1em;
}

.logout_button:hover {
  font-size: 1.2em; /* Increase font size on hover */
  color: red; /* Add red underline on hover */
}

.search {
  position: absolute;
  top: 100%; /* Position the search form below the header */
  left: 77%;
  z-index: 999; /* Ensure the search form appears above other content */
  padding: 10px;
  background-color: #fff; /* Background color for the search form */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Add a subtle box shadow */
  border-radius: 4px; /* Add rounded corners */
  width: 250px; /* Set the width of the search form */
}

#search-box {
  width: 100%; /* Make the search input fill the width of the form */
  padding: 8px;
  border: 1px solid #ccc; /* Add a border to the input */
  border-radius: 4px; /* Add rounded corners */
  outline: none; /* Remove the default focus outline */
}

.search-icon {
  position: absolute;
  top: 50%; /* Vertically center the search icon */
  right: 30px;
  transform: translateY(-50%); /* Adjust for vertical centering */
  color: #888; /* Color for the search icon */
  font-size:1.5rem
}
.search-icon:hover {
  cursor:pointer
}
</style>
