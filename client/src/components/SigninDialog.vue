<template>
  <div class="dialog-container" v-if="isDialogVisible">
    <div class="dialog">
      <h2>Sign In</h2>
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" id="email" v-model="email" required />
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <button type="submit">Sign In</button>
        <p>
          If you are new to the site, please
          <a><router-link to="/signup" class="link">sign up</router-link></a
          >.
        </p>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "../router/axios.js";
import store from '../store'

export default {
  name: "SigninDialog",
  data() {
    return {
      email: "",
      password: "",
      isDialogVisible: true, // You can control this via props or other state management
    };
  },
  methods: {
    handleSubmit() {
      axios
        .post("http://127.0.0.1:5000/signin", {
          email: this.email,
          password: this.password,
        })
        .then((response) => {          
          alert(response.data.message);
          if ((response.data.message = "You are successfully signed in.")) {
            const token = response.data.access_token;            
            localStorage.setItem("token", token);
            store.commit("setLoggedIn", true)
            this.$router.push({ name: "Home" });
          }
        })
        .catch((error) => {
          alert("Error");
        });
    },
 
  },
};
</script>

<style scoped>
.dialog-container {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1000; /* Ensure it's above other elements */
}

.dialog {
  background: rgb(37, 36, 36);
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 300px;
  text-align: center;
  color: white;
  font-size: 17px;
}

.dialog p {
  text-transform: none;
}

.dialog h2 {
  font-size: 25px;
}

.link {
  color: chartreuse;
}
.link:hover {
  color: red;
}
.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
}

.form-group input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}

button {
  padding: 10px 15px;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background: #0056b3;
}
</style>
