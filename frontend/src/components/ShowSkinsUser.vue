<template>
  <div class="user-skins">
    <h1>Mis skins</h1>
    <div v-if="skins.length > 0">
      <!-- Usar un div con la clase row para envolver las skins -->
      <div class="row">
        <!-- Usar un div con la clase col-md-4 para cada skin -->
        <div v-for="skin in skins" :key="skin.id" class="col-md-4">
          <!-- Usar la clase skin-box para darle estilo a la skin -->
          <div class="skin-box">
            <img :src="skin.skin_image" alt="Skin image" />
            <h3>{{ skin.name }}</h3>
            <p>{{ skin.champion }}</p>
            <p>{{ skin.rarity }}</p>
            <!-- Añadir un botón para comprar la skin -->
            <button class="buy-button">Buy</button>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <p>No tienes ninguna skin</p>
    </div>
  </div>
</template>

<script scooped>
import { getSkinsUser } from "@/services/userskins.api";
export default {
  name: "UserSkins",
  data() {
    return {
      skins: [],
    };
  },
  methods: {
    async loadSkins() {
      const { serialize } = await getSkinsUser();
      this.skins = serialize;
    },
  },
  created() {
    this.loadSkins();
  },
};
</script>

<style>
/* Usar el css que me has dado */
.skin-box {
  background-color: #1f1d1d;
  border-radius: 10px;
  margin-bottom: 50px;
  padding: 20px;
  text-align: center;
}

.skin-box img {
  max-width: 100%;
  height: 200px;
  object-fit: contain;
}

.skin-box h3 {
  font-size: 24px;
  margin-top: 20px;
  margin-bottom: 10px;
}

.skin-box p {
  font-size: 18px;
  margin-bottom: 20px;
}

.buy-button {
  background-color: #1e1818;
  border: none;
  color: #ffffff;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 18px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.buy-button:hover {
  background-color: #330f0f;
}

/* Añadir un media query para pantallas pequeñas */
@media (max-width: 768px) {
  .col-md-4 {
    flex-basis: 100%;
    max-width: 100%;
    margin-left: auto;
    margin-right: auto;
  }
}
</style>
