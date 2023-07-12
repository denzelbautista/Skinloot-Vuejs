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
  </div>
</template>

<script>
import { registerPost } from "@/services/userpost.api";
import { getSkinsUser } from "@/services/userskins.api";
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
};
</script>
