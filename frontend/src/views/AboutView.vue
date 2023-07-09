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
//import { getToken } from "@/services/users.api";

export default {
  name: "RegisterUserSkin",
  data() {
    return {
      skin: {
        name: "",
        champion_name: "",
        rarity: "",
        user_id: "", // Aquí se asignará el ID del usuario registrado
      },
      token: "", // Variable para almacenar el token
    };
  },
  methods: {
    async AddSkinEvent() {
      await registerSkin(this.skin, this.token);
      console.log("data:", this.skin);
    },
  },
};
</script>

<style></style>
