<template>
  <div>
    <CRow class="justify-content-center">
      <CCard style="width: 600px" class="m-5">
        <div>
        <label class="mt-5"> Hello: {user_date} </label>
        </div>
      </CCard>
    </CRow>
  </div>
</template>

<script>
export default {
  name: "UserCard",
  props: {
    user_data: Object,
  },
};
</script>
