<template>

    

  <!-- home section starts  -->
  

  <section class="home" id="home">
    <div class="content">
      <h3>THE LATEST FOOTBALL PRODUCTS</h3>
      <p>
        At FootNow, we are passionate about soccer and committed to providing
        enthusiasts and players alike with the highest quality soccer products.
        From the latest in soccer footwear and apparel to essential gear like
        balls and accessories, we've got everything you need to take your game
        to the next level.
      </p>
      <a class="btn"><router-link to='/products'>Get Yours Now</router-link></a>
    </div>
  </section>

 
  
</template>

<script>
import logo from '../assets/Logo.png'; 

export default {
    name:'Home',
    
    data(){
        return{
          logo,
          
        }
    }
}
</script>
