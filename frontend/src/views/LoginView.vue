<template>
  <div class="login-view">
    <h1 class="title">Login</h1>
    <div class="form-container">
      <form class="login-form" @submit.prevent.stop="loginUserEvent">
        <div class="form-group">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="user.nickname" />
        </div>
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="text" id="email" v-model="user.e_mail" />
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="user.password" />
        </div>
        <button class="submit-button" type="submit">Submit</button>
      </form>
    </div>
  </div>
</template>

<script>
import { loginUser } from "@/services/loginuser.api";
export default {
  name: "LoginView",
  data() {
    return {
      user: {
        nickname: "",
        e_mail: "",
        password: "",
      },
    };
  },
  methods: {
    async loginUserEvent() {
      await loginUser(this.user);
      this.$router.push({ name: "market" });
    },
  },
};
</script>

<style scoped>
.login-view {
  background: url("https://media.giphy.com/media/U8VG8SfKICqkPjq4Sl/giphy.gif")
      no-repeat 90% center fixed,
    url("https://media.giphy.com/media/U8VG8SfKICqkPjq4Sl/giphy.gif") no-repeat
      10% center fixed;
  background-size: auto 40%;
  background-color: rgb(0, 0, 0);
  color: rgb(207, 0, 0);
  height: 96.7vh; /* Ajusta la altura al 100% de la ventana */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.title {
  font-weight: none;
  font-size: 100px;
  font-family: "Times New Roman", Times, serif;
  color: #ff0000;
  margin-bottom: 20px;
}

.form-container {
  padding: 20px;
  border-radius: 8px;
  width: 30%; /* Ajusta el ancho del formulario según tus preferencias */
}

.login-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 20px;
}
.login-form label {
  margin-bottom: 10px;
  color: rgb(207, 0, 0); /* los nicks y eso*/
  font-weight: bold;
}

input[type="text"],
input[type="email"],
input[type="password"] {
  padding: 10px;
  background-color: #333333;
  color: white;
  border: none;
  border-radius: 4px;
  box-sizing: 100%;
}

.submit-button {
  padding: 10px;
  background-color: rgb(207, 0, 0);
  color: #000000;
  border: none;
  border-radius: 9px;
  cursor: pointer;
  font-weight: bold;
}

.submit-button:hover {
  background-color: darkred;
}
</style>
