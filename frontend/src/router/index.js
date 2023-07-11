import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";
import MarketView from "../views/MarketView.vue";

const routes = [
  {
    path: "/register",
    name: "register",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "register" */ "../views/RegisterView.vue"),
  },
  {
    path: "/login",
    name: "login",
    component: () =>
      import(/* webpackChunkName: "login" */ "../views/LoginView.vue"),
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
