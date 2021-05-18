<template>
  <h1>Login</h1>
  <p>
    Welcome back
  </p>
  <form @submit="onSubmit">
    <p>
      Email*<br />
      <input type="text" placeholder="mail@somedomain.com" v-model="username" />
    </p>
    <p>
      Password*<br />
      <input
        type="password"
        placeholder="Your secret words"
        v-model="password"
      />
    </p>
    <input type="submit" value="Login" />
  </form>
</template>

<script>
export default {
  name: "LoginForm",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    onSubmit(e) {
      e.preventDefault();

      alert(this.username + "\n" + this.password);
    },
  },
};
</script>

<style scoped>
/* TODO style */
</style>
