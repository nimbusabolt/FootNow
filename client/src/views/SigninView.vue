<template>
  
  <div class="content signin">
    <SigninDialog />
  </div>
  
</template>
<script>

import SigninDialog from "@/components/SigninDialog.vue";

export default {
  name: "SigninView",
  components: {    
    SigninDialog,
  },
};
</script>
<style scoped>
.content {
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(
    100vh - 100px
  ); /* Adjust according to the height of Navbar and Footer */
  padding-top: 50px; /* Adjust according to the height of Navbar */
  padding-bottom: 50px; /* Adjust according to the height of Footer */
}
</style>
