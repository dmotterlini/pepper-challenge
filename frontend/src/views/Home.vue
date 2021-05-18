<template>
  <div class="home">
    <img alt="Logo" src="@/assets/logo.png" width="400" />
    <LoginForm />
  </div>
</template>

<script>
// @ is an alias to /src
import LoginForm from "@/components/LoginForm.vue";

export default {
  name: "Home",
  components: {
    LoginForm,
  },
};
</script>
