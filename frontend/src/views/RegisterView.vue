<template>
  <div>
    <h1>Sign Up!</h1>
    <div v-if="!isUserSubmitted">
      <form @submit.prevent.stop="registerUserEvent">
        <div>
          <label>Username:</label>
          <input type="text" v-model="user.nickname" />
        </div>
        <div>
          <label>Email:</label>
          <input type="text" v-model="user.e_mail" />
        </div>
        <div>
          <label>Password:</label>
          <input type="password" v-model="user.password" />
        </div>
        <div>
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
      errorLists: [],
      isUserSubmitted: false,
    };
  },
  methods: {
    async registerUserEvent() {
      await registerUser(this.user);
    },
  },
};
</script>
