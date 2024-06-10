<template>
  <div class="dialog-container">
    <div class="dialog">
      <h2>Sign Up</h2>
      <form @submit.prevent="validateForm">
        <div class="form-group">
          <label for="username">Email</label>
          <input
            type="text"
            id="email"
            v-model="email"
            required
            @input="validateEmail"
          />
          <span v-if="emailError" class="error">{{ emailError }}</span>
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input
            type="password"
            id="password"
            v-model="password"
            required
            @input="validatePassword"
          />
          <span v-if="passwordError" class="error">{{ passwordError }}</span>
        </div>
        <button type="submit">Sign Up</button>
        <div>
          <p>
            If you have already signed up, Please go to
            <a><router-link class="link" to="/signin">log-in </router-link></a
            >dialog
          </p>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "../router/axios.js";
import store from '../store.js'

export default {
  name: "SignupDialog",
  data() {
    return {
      email: "",
      password: "",
      emailError: "",
      passwordError: "",
    };
  },
  methods: {
    validateEmail() {
      const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
      if (!this.email.match(emailPattern)) {
        this.emailError = "Please enter a valid email address.";
      } else {
        this.emailError = "";
      }
    },

    validatePassword() {
      const passwordRegex = /^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$/;
      if (!passwordRegex.test(this.password)) {
        this.passwordError =
          "Password must be at least 8 characters long and contain at least one number and one capital letter";
      } else {
        this.passwordError = "";
      }
    },

    validateForm() {
      this.validateEmail();
      this.validatePassword();
      if (!this.emailError && !this.passwordError) {
        // Proceed with the signup process
        this.handleSubmit();
      }
    },
    handleSubmit(){
      if (!this.emailError && this.email && this.password)
      axios.post('http://127.0.0.1:5000/signup', {
        email:this.email,
        password:this.password
      }).then(response=>{
        alert(response.data.message);
        if (response.data.message="You are successfully signed up."){
          const token=response.data.access_token;
          localStorage.setItem('token', token)
          store.commit("setLoggedIn", true)
          this.$router.push({name:'Home'})
        }
      }).catch(error=>{
        alert("Error:" +error.response.data.message)
      })
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

.error {
  text-transform: none;
}

.dialog h2 {
  font-size: 25px;
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

.link {
  color: chartreuse;
}

.link:hover {
  color: red;
}

.error {
  color: red;
  font-size: 0.8em;
}

button {
  padding: 10px 15px;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 10px;
}

button:hover {
  background: #0056b3;
}
</style>
