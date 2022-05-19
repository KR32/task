import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach(async (to) => {
  if (
    // ❗️ Avoid an infinite redirect
    to.name !== "home"
  ) {
    // redirect the user to the login page
    return { name: "home" };
  }
});

export default router;
