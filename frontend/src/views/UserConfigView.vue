<template>
  <div class="page-container">
    <navbar-market />
    <div class="container">
      <h1>Configuración de Usuario</h1>
      <form id="user-settings-form" action="/update-user" method="POST">
        <div class="mb-3">
          <label for="username" class="form-label"
            >Cambiar Nombre de Usuario</label
          >
          <input
            type="text"
            class="form-control"
            id="username"
            name="username"
            placeholder="Nuevo Nombre de Usuario"
          />
        </div>
        <div class="mb-3">
          <label for="profile-picture" class="form-label"
            >Cambiar Foto de Perfil</label
          >
          <input
            type="file"
            class="form-control"
            id="profile-picture"
            name="profile-picture"
          />
        </div>
        <div class="mb-3">
          <label for="balance" class="form-label">Añadir Saldo</label>
          <input
            type="number"
            class="form-control"
            id="balance"
            name="balance"
            placeholder="Cantidad de Saldo"
          />
        </div>
        <button type="submit" class="btn btn-primary button">
          Guardar Cambios
        </button>
        <a href="/logout" id="logout-link" class="button">Cerrar sesión</a>
      </form>
      <button class="btn btn-secondary button" @click="Logout">
        Cerrar Sesión
      </button>
      <button class="btn btn-secondary button">Ver Skins</button>
      <button class="btn btn-secondary button">Agregar Skins</button>
    </div>
  </div>
</template>

<script scooped>
import NavbarMarket from "@/components/NavbarMarket.vue";

export default {
  name: "UserConfigView",
  components: {
    NavbarMarket,
  },
  data() {},
  methods: {
    Logout() {
      localStorage.removeItem("token");
      this.$router.push({ name: "home" });
    },
  },
};
</script>

<style>
.container {
  margin-top: 50px;
}

.button {
  margin-top: 10px;
}

.form-control {
  border-radius: 10px;
}
.button {
  display: inline-block;
  padding: 10px 20px;
  background-color: #007bff; /* Color celeste */
  color: #fff; /* Color del texto blanco */
  border: none;
  border-radius: 5px;
  text-decoration: none;
}

.button:hover {
  opacity: 0.8; /* Cambiar la opacidad al pasar el cursor sobre el botón */
}

.page-container {
  background: linear-gradient(to bottom, #2e0909, #240606, #170000);
  width: 100%;
  height: 96.7vh;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  color: #ffffff;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}

.filter-box {
  margin-top: 30px;
  margin-bottom: 30px;
}

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

.custom-input-group {
  background-color: #333333;
  border-color: #333333;
  color: rgb(101, 91, 91);
}

.custom-button {
  padding: 5px 10px;
  border-radius: 5px;
  margin-right: 10px;
}

.custom-button img {
  width: 30px;
  height: 30px;
  object-fit: contain;
}

.custom-button-container {
  float: right;
}
</style>
