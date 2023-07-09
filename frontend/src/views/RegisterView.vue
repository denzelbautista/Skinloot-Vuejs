<template>
  <div class="registerview">
    <h1 class="skinloot">Register</h1>
    <div class="form-container">
      <form class="registration-form" @submit.prevent.stop="registerUserEvent">
        <div class="form-group">
          <label>Username:</label>
          <input type="text" v-model="user.nickname" />
        </div>
        <div class="form-group">
          <label>Email:</label>
          <input type="text" v-model="user.e_mail" />
        </div>
        <div class="form-group">
          <label>Password:</label>
          <input type="password" v-model="user.password" />
        </div>
        <div class="form-group">
          <label>Confirmation Password:</label>
          <input type="password" v-model="user.confirmationPassword" />
        </div>
        <button class="submit-button" type="submit">Submit</button>
      </form>
    </div>
  </div>
</template>

<script>
import { registerUser } from "@/services/users.api";
export default {
  name: "RegisterUser",
  data() {
    return {
      user: {
        nickname: "",
        e_mail: "",
        password: "",
        confirmationPassword: "",
      },
    };
  },
  methods: {
    async registerUserEvent() {
      await registerUser(this.user);
    },
  },
};
</script>

<style>
.registerview {
  background: url("https://media.giphy.com/media/U8VG8SfKICqkPjq4Sl/giphy.gif")
      no-repeat 90% center fixed,
    url("https://media.giphy.com/media/U8VG8SfKICqkPjq4Sl/giphy.gif") no-repeat
      10% center fixed;
  background-size: auto 40%;
  background-color: rgb(0, 0, 0);
  color: rgb(207, 0, 0);
}

.skinloot {
  font-weight: none;
  font-size: 100px;
  font-family: "Times New Roman", Times, serif;
  color: #ff0000;
}

.form-container {
  /*background-color: #000000; /* es el contrno*/
  padding: 20px;
  border-radius: 8px;
}

.registration-form label {
  display: block;
  margin-bottom: 10px;
  color: rgb(207, 0, 0); /* los nicks y eso*/
  font-weight: bold;
}

.registration-form input[type="text"],
.registration-form input[type="email"],
.registration-form input[type="password"] {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  background-color: #2c2c2c;
  color: rgb(0, 0, 0);
  border: none;
  border-radius: 4px; /* los inputs*/
  color: white;
}

.skinloot {
  text-align: center;
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}

.registration-form input[type="submit"] {
  width: 100%;
  padding: 10px;
  background-color: rgb(207, 0, 0);
  color: #000000; /* el submit*/
  border: #383838;
  border-radius: 9px;
  cursor: pointer;
  font-weight: bold;
}

.registration-form input[type="submit"]:hover {
  background-color: darkred;
}

.logo {
  width: 100%;
  max-width: 1000px; /* Ajusta el tamaño máximo de la imagen según tus preferencias */
  display: block;
  margin: 0 auto; /* Centra la imagen horizontalmente */
  border-radius: 10000px;
  border: #ff0303;
}
</style>
