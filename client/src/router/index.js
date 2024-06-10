import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AboutView from "../views/AboutView.vue";
import ProductsView from "../views/ProductsView.vue";
import ContactView from "../views/ContactView.vue";
import BlogsView from "../views/BlogsView.vue";
import ReviewView from "../views/ReviewView.vue";
import SigninView from "@/views/SigninView.vue";
import SignupView from "@/views/SignupView.vue";
import Checkout from "@/views/Checkout.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Home",
      component: HomeView,
    },
    {
      path: "/about",
      name: "About",
      component: AboutView,
    },
    {
      path: "/products",
      name: "Products",
      component: ProductsView,
    },
    {
      path: "/contact",
      name: "Contact",
      component: ContactView,
    },
    {
      path: "/blogs",
      name: "Blogs",
      component: BlogsView,
    },
    {
      path: "/review",
      name: "Review",
      component: ReviewView,
    },
    {
      path:"/checkout",
      name:"Checkout",
      component:Checkout
    },
    {
      path: "/signin",
      name: "Signin",
      component: SigninView,
    },
    {
      path: "/signup",
      name: "Signup",
      component: SignupView,
    },
  ],
});
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem("token");

  // Check if the route requires authentication and token is not present
  if (to.name === "Contact") {
    if (!token) {
      // Alert the user
      alert("You have to sign in to go to Contact page");
      // Redirect to signin view
      next({ name: "Signin" });
    } else {
      // Proceed to the next route
      next();
    }
  } else {
    // For other routes, proceed as usual
    next();
  }
});
export default router;
