<template>
  <div class="home">
    <UserCard :user_data="user_data" />
    <CButton @click="goBack()" color="primary">Back</CButton>
  </div>
</template>

<script>
// @ is an alias to /src
import UserCard from "@/components/UserCard.vue";
import axios from "axios";

export default {
  name: "HomeView",
  components: {
    UserCard,
  },
  data() {
    return {
      user_data: {},
    };
  },
  mounted() {
    let { id } = this.$route.params;

    axios({
      method: "get",
      url: "http://127.0.0.1:8000/v1/search",
      params: {
        user_id: id,
      },
    })
      .then((response) => {
        this.user_data = response.data[0];
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    goBack() {
      this.$router.push({
        name: "create",
      });
    },
  },
};
</script>
