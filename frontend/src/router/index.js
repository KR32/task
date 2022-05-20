import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import UserRegistration from "../views/UserRegistration.vue";

const routes = [
  {
    path: "/",
    name: "create",
    component: UserRegistration,
  },
  {
    path: "/list-view/:id",
    name: "list",
    component: HomeView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// router.beforeEach(async (to) => {
//   if (
//     // ❗️ Avoid an infinite redirect
//     to.name !== "list-view"
//   ) {
//     // redirect the user to the registration pageF
//     return { name: "home" };
//   }
// });

export default router;
