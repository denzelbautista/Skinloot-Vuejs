<template>
  <div class="post-creation-form">
    <h1>Registrar Post</h1>
    <div>
      <form @submit.prevent.stop="registerPostEvent">
        <div>
          <label>Skin:</label>
          <select v-model="post.skin_id">
            <option v-for="skin in skins" :key="skin.id" :value="skin.id">
              {{ skin.name }}
            </option>
          </select>
        </div>
        <div>
          <label>Title:</label>
          <input type="text" v-model="post.title" />
        </div>
        <div>
          <label>Name:</label>
          <input type="text" v-model="post.name" />
        </div>
        <div>
          <label>Price:</label>
          <input type="number" v-model="post.price" />
        </div>
        <div>
          <label>Champion:</label>
          <input type="text" v-model="post.champion" />
        </div>
        <button class="submit-button" type="submit">Submit</button>
      </form>
    </div>
    <user-skins></user-skins>
  </div>
</template>

<script>
import { registerPost } from "@/services/userpost.api";
import { getSkinsUser } from "@/services/userskins.api";
import UserSkins from "@/components/ShowSkinsUser.vue";
export default {
  name: "RegisterUserPost",
  mounted() {
    this.loadSkins();
  },
  data() {
    return {
      post: {
        title: "",
        skin_id: "",
        name: "",
        price: "",
        champion: "",
      },
      skins: [],
    };
  },
  methods: {
    async loadSkins() {
      const { serialize } = await getSkinsUser();
      this.skins = serialize;
    },

    async registerPostEvent() {
      await registerPost(this.post, this.token);
    },
  },
  components: { UserSkins },
};
</script>

<style>
.post-creation-form {
  width: 80%;
  margin: 0 auto;
  font-family: Arial, sans-serif;
}

h1 {
  text-align: center;
  color: #333;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
}

label {
  font-weight: bold;
  color: #555;
}

input,
select {
  width: 300px;
  height: 30px;
  padding: 5px;
  border: 1px solid #aaa;
  border-radius: 5px;
}

.submit-button {
  width: 200px;
  height: 40px;
  background-color: #28a745;
  color: white;
  font-size: 18px;
  border: none;
  border-radius: 10px;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #218838;
}
</style>
