<template>
  <div>
    <CRow class="justify-content-center">
      <CCard style="width: 600px" class="m-5">
        <h5 class="text-center">Welcome {{ user_data_name }}</h5>
        <h6>{{ user_data_email }}</h6>
      </CCard>
    </CRow>
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
export default {
  name: "UserCard",
  props: {
    user_data: {
      type: Object,
      required: true,
      default: () => {
        return {};
      },
    },
  },
  data() {
    return {
      toasts: [],
    };
  },
  mounted() {
    this.toasts.push({
      content: "User Saved Successfully",
      title: "Welcome",
    });
  },
  computed: {
    user_data_name() {
      return this.user_data.name;
    },
    user_data_email() {
      return this.user_data.email;
    },
  },
};
</script>

<style scoped>
.card {
  background: #fff;
  padding: 2em 2em 2em 0em;
  max-width: 400px;
  margin: 50px auto 0;
  box-shadow: 0 0 1em #222;
  border-radius: 2px;
}
</style>
