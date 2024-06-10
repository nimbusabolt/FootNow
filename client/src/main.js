import "./style/main.css";

import { createApp } from "vue";

import App from "./App.vue";
import router from "./router";
import axios from "./router/axios.js";
import store from './store.js'
import 'vue-toastify/index.css';

const app = createApp(App);

app.use(router);
app.use(store)
app.config.productionTip = false;

app.mount("#app");

app.config.globalProperties.$http = axios;
