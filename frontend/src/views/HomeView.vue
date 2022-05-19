<template>
  <div class="home">
    <UserCard user_data="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import UserCard from "@/components/UserCard.vue";

export default {
  name: "HomeView",
  components: {
    UserCard,
  },
};
</script>
