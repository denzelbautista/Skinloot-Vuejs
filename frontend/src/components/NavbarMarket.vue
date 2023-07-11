<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-auto">
          <button class="btn btn-outline-danger custom-button" type="button">
            Post
          </button>
        </div>
        <div class="col-md-auto custom-button-container">
          <button
            class="btn btn-outline-danger custom-button"
            id="user_config"
            type="button"
          >
            <img
              src="@/assets/images/persona.png"
              alt="Perfil"
              class="align-right"
              @click="redirectToUserConfig"
            />
          </button>
        </div>
        <div class="col-md-auto custom-button-container">
          <button
            class="btn btn-outline-danger custom-button"
            id="user_config"
            type="button"
          >
            <img
              src="@/assets/images/home.png"
              alt="Perfil"
              class="align-right"
              @click="redirectToMarket"
            />
          </button>
        </div>
      </div>
      <a class="navbar-brand" href="#">Welcome to Skinloot</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarText"
        aria-controls="navbarText"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarText">
        <!-- contenido adicional del navbar si lo necesitas -->
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavbarMarket",
  methods: {
    redirectToUserConfig() {
      this.$router.push({ name: "userconfig" });
    },
    redirectToMarket() {
      this.$router.push({ name: "market" });
    },
  },
};
</script>

<style>
.navbar {
  background-color: rgb(209, 209, 209);
}
</style>
