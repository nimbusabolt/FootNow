<template>
  <section class="contact" id="contact">
    <h1 class="heading"><span>contact</span> us</h1>

    <div class="row">
      <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d20623.574504018754!2d5.707138324721994!3d58.96645728575791!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x463a3549dd29f795%3A0xad7aeb21b80a9259!2sStavanger!5e0!3m2!1sen!2sno!4v1714310703246!5m2!1sen!2sno"
        width="600"
        height="450"
        style="border: 0"
        allowfullscreen=""
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
      ></iframe>
      <form action="https://formspree.io/f/xayrvyby" method="POST">
        <h3>get in touch</h3>
        <div class="inputBox">
          <span class="fas fa-user icon"></span>
          <input type="text" name="name" placeholder="name" required />
        </div>
        <div class="inputBox">
          <span class="fas fa-envelope icon"></span>
          <input type="email" name="_replyto" placeholder="email" required />
        </div>
        <div class="inputBox">
          <span class="fas fa-phone icon"></span>
          <input type="text" name="phone" placeholder="number" required />
        </div>
        <div class="inputBox">
          <span class="fas fa-pen icon"></span>
          <textarea
            name="message"
            placeholder="Your message here..."
            required
            class="message"
          ></textarea>
        </div>
        <button type="submit" class="btn">Send</button>
      </form>
    </div>
  </section>
</template>
<script>
export default {
  name: "ContactView",
};
</script>
<style>
.icon{
  margin-right: 20px;
}
.message {
  width:100%
}
</style>
