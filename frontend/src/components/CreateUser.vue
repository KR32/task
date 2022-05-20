<template>
  <div>
    <form autocomplete="off" @submit.prevent="submit()">
      <h2 class="mb-3">Welcome Guest</h2>
      <p>
        <label for="Name" class="ml-5 floatLabel">Name</label>
        <input
          v-model="user_data.name"
          id="Name"
          name="Name"
          type="text"
          required
        />
      </p>
      <p>
        <label for="Email" class="floatLabel">Email</label>
        <input
          v-model="user_data.email"
          id="Email"
          name="Email"
          type="email"
          required
        />
      </p>

      <p>
        <CButton color="primary" type="submit" id="submit">Submit</CButton>
      </p>
    </form>
    <CToaster placement="bottom-end">
      <CToast v-for="(toast, index) in toasts" :key="index">
        <CToastHeader closeButton>
          <span class="me-auto fw-bold">{{ toast.title }}</span>
        </CToastHeader>
        <CToastBody>
          {{ toast.content }}
        </CToastBody>
      </CToast>
    </CToaster>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CreateUser",
  data: function () {
    return {
      user_data: {
        name: "",
        email: "",
      },
      toasts: [],
    };
  },
  methods: {
    submit() {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/v1/create",
        data: this.user_data,
      })
        .then((response) => {
          this.$router.push({
            name: "list",
            params: {
              id: response.data.user_id,
            },
          });
        })
        .catch((error) => {
          if (Array.isArray(error.response.data.detail)) {
            this.showToast(error.response.data.detail[0].msg, "Error");
          } else {
            this.showToast(error.response.data.detail, "Error");
          }

          console.log(error);
        });
    },
    showToast(message, header) {
      this.toasts.push({
        title: header,
        content: message,
      });
    },
  },
};
</script>

<style lang="scss" scoped>
form {
  background: #fff;
  padding: 4em 4em 2em;
  max-width: 400px;
  margin: 50px auto 0;
  box-shadow: 0 0 1em #222;
  border-radius: 2px;
}
label {
  margin-right: 10px;
}
</style>
