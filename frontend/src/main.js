import { createApp } from "vue";
import HomePage from "./views/HomePage.vue";
import router from "./router";

createApp(HomePage).use(router).mount("#app");
