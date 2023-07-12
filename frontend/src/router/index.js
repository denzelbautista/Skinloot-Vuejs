import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";
import RegisterView from "../views/RegisterView.vue";
import LoginView from "../views/LoginView.vue";
import RegisterUserSkin from "../views/AboutView.vue";
import MarketView from "../views/MarketView.vue";

const routes = [
  {
    path: "/register",
    name: "register",
    component: RegisterView,
  },
  {
    path: "/about",
    name: "about",
    component: RegisterUserSkin,
  },

  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/market",
    name: "market",
    component: MarketView,
  },
  {
    path: "/userconfig",
    name: "userconfig",
    component: () =>
      import(
        /* webpackChunkName: "userconfig" */ "../views/UserConfigView.vue"
      ),
  },
  {
    path: "/postskin",
    name: "postskin",
    component: () =>
      import(/* webpackChunkName: "userconfig" */ "../views/PostSkinView.vue"),
  },
  {
    path: "/",
    name: "home",
    component: HomePage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
