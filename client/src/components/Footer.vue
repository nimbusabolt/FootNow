<template>
  <section class="footer">
    <div class="share">
      <a href="#" class="fab fa-facebook-f"></a>
      <a href="#" class="fab fa-twitter"></a>
      <a href="#" class="fab fa-instagram"></a>
      <a href="#" class="fab fa-linkedin"></a>
      <a href="#" class="fab fa-pinterest"></a>
    </div>

    <div class="links">
        <a><router-link to="/">Home</router-link></a>
      <a><router-link to="/about">About</router-link></a>
      <a><router-link to="/products">Products</router-link></a>
      <a><router-link to="/review">Review</router-link></a>
      <a><router-link to="/contact">Contact</router-link></a>
      <a><router-link to="/blogs">Blogs</router-link></a>
    
    </div>

    <div class="credit">
      created by <span> Jehad And Ruhan </span> | all rights reserved
    </div>
  </section>
</template>
<script>
    export default {
        name:"Footer"
    }
</script>