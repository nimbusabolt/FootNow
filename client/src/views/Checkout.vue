<template>
    <div class="container">
      <form @submit.prevent="submitForm">
        <div class="row">
          <div class="col">
            <h3 class="title">billing address</h3>
            <div class="inputBox">
              <span>full name :</span>
              <input type="text" v-model="billing.fullName" placeholder="john deo">
            </div>
            <div class="inputBox">
              <span>email :</span>
              <input type="email" v-model="billing.email" placeholder="example@example.com">
            </div>
            <div class="inputBox">
              <span>address :</span>
              <input type="text" v-model="billing.address" placeholder="room - street - locality">
            </div>
            <div class="inputBox">
              <span>city :</span>
              <input type="text" v-model="billing.city" placeholder="mumbai">
            </div>
            <div class="flex">
              <div class="inputBox">
                <span>state :</span>
                <input type="text" v-model="billing.state" placeholder="india">
              </div>
              <div class="inputBox">
                <span>zip code :</span>
                <input type="text" v-model="billing.zipCode" placeholder="123 456">
              </div>
            </div>
          </div>
          <div class="col">
            <h3 class="title">payment</h3>
            <div class="inputBox image-div">
              <span>cards accepted :</span>
              <img src="../assets/cards.jpg" alt="cards">
            </div>
            <div class="inputBox">
              <span>name on card :</span>
              <input type="text" v-model="payment.nameOnCard" placeholder="mr. john deo">
            </div>
            <div class="inputBox">
              <span>credit card number :</span>
              <input type="number" v-model="payment.cardNumber" placeholder="1111-2222-3333-4444">
            </div>
            <div class="inputBox">
              <span>exp month :</span>
              <input type="text" v-model="payment.expMonth" placeholder="january">
            </div>
            <div class="flex">
              <div class="inputBox">
                <span>exp year :</span>
                <input type="number" v-model="payment.expYear" placeholder="2022">
              </div>
              <div class="inputBox">
                <span>CVV :</span>
                <input type="text" v-model="payment.cvv" placeholder="1234">
              </div>
            </div>
          </div>
        </div>
        <input type="submit" value="proceed to checkout" class="submit-btn">
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Checkout',
    data() {
      return {
        billing: {
          fullName: '',
          email: '',
          address: '',
          city: '',
          state: '',
          zipCode: ''
        },
        payment: {
          nameOnCard: '',
          cardNumber: '',
          expMonth: '',
          expYear: '',
          cvv: ''
        }
      };
    },
    methods: {
      submitForm() {
        // Handle form submission logic here
        console.log('Billing Info:', this.billing);
        console.log('Payment Info:', this.payment);
        alert('Form submitted!');
      }
    }
  };
  </script>
  <style scoped>
  .container {
    width:100%;
    margin: 0 50px;
    padding: 20px;
    background: #000000;
    color:white;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  .row {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }
  .col {
    flex: 1;
    min-width: 300px;
    margin: 10px;
    font-size:16pt
  }
  .title {
    font-size: 24px;
    margin-bottom: 20px;
    color: #ffffff;
    text-transform: capitalize;
  }
  .inputBox {
    margin-bottom: 15px;
  }
  .inputBox label {
    display: block;
    margin-bottom: 5px;
    font-weight: 500;
    color: #ffffff;
  }
  .inputBox input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    background: #fff;
    font-size: 16px;
    color: #333;
  }
  .inputBox img {
    max-width: 100%;
    margin-top: 10px;
  }
  .flex {
    display: flex;
    gap: 10px;
  }
  .submit-btn {
    position:relative;
    width: 20%;
    left:40%;
    border: 3px solid white;
    padding: 15px;
    background: #000000;
    color: #fff;
    border: none;
    border-radius: 4px;
    font-size: 18px;
    cursor: pointer;
    text-transform: uppercase;
    transition: background 0.3s ease;
  }
  .submit-btn:hover {
    background: #f10d0d;
  }

  .image-div {
    display: flex; /* Enables Flexbox layout */
    align-items: center; /* Vertically centers the items */
    /* Optionally centers the items horizontally */
  /* Optional: for visual reference */
    padding: 5px; /* Optional: adds padding to the container */
    
  }
  </style>
  
  