<template>
  <div class="register-current-user-skin">
    <form @submit.prevent.stop="AddSkinEvent">
      <div>
        <label>Name:</label>
        <select v-model="skin.name">
          <option value="Gragas_camorrista">Camorrista_G</option>
          <option value="gragas_shrek">Shrek_G</option>
          <option value="cosmico">Cosmico_J</option>
          <option value="virtuoso">virtuoso_J</option>
          <option value="Shen_Surgeon">Surgeon_S</option>
          <option value="Warlord_shen">Warlord_S</option>
        </select>
      </div>
      <div>
        <label>Champion Name:</label>
        <select v-model="skin.champion_name">
          <option value="Gragas">Gragas</option>
          <option value="jhin">Jhin</option>
          <option value="Shen">Shen</option>
        </select>
      </div>
      <div>
        <label>Rarity:</label>
        <select v-model="skin.rarity">
          <option value="Pro">Legendary</option>
          <option value="Normal">Epic</option>
          <option value="Pobre">Normal</option>
        </select>
      </div>

      <button class="submit-button" type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import { registerSkin } from "@/services/userskins.api";
import jwtDecode from "jwt-decode";
export default {
  name: "RegisterUserSkin",
  computed: {
    token() {
      // Lee el token del local storage y lo devuelve
      let tokenized = localStorage.getItem("token");
      return jwtDecode(tokenized).user_created_id;
    },
  },
  data() {
    return {
      skin: {
        name: "",
        champion_name: "",
        rarity: "",
        user_id: null, // Aquí se asignará el ID del usuario registrado
      },
    };
  },
  methods: {
    async AddSkinEvent() {
      this.skin.user_id = this.token;
      await registerSkin(this.skin);
    },
  },
};
</script>

<style></style>
