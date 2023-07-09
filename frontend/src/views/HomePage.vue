<template>
  <div>
    <button class="menu"><b>Log In</b></button>
    <div class="jumbotron">
      <div class="container-fluid text-center">
        <h1 class="display-3 text-white fw-bold">Skinloot</h1>
        <p class="lead text-white">
          Welcome to Skinloot, the marketplace for video games skins. Browse our
          selection of skins and find the perfect look for your game character.
        </p>
      </div>
    </div>
    <div id="how-it-works">
      <div class="container">
        <div class="row">
          <div class="col-md-12">
            <h2 class="text-center mb-5">How it works</h2>
          </div>
        </div>
        <div class="row">
          <div class="col-md-4">
            <h3 class="text-center">Step 1</h3>
            <p class="text-center">
              Browse our selection of skins and find the one you like.
            </p>
          </div>
          <div class="col-md-4">
            <h3 class="text-center">Step 2</h3>
            <p class="text-center">
              Add the skin to your cart and proceed to checkout.
            </p>
          </div>
          <div class="col-md-4">
            <h3 class="text-center">Step 3</h3>
            <p class="text-center">
              Receive the skin in your game account and enjoy your new look!
            </p>
          </div>
        </div>
      </div>
    </div>
    <div>
      <button class="Register_now" @click="redirectToRegister">
        Register Now
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomePage",
  methods: {
    redirectToRegister() {
      this.$router.push({ name: "register" });
    },
  },
};
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/css/bootstrap.min.css");

.jumbotron {
  background: url("https://media.giphy.com/media/UtEQ8viTEfCdiAOW4Q/giphy.gif")
    no-repeat center center fixed;
  background-size: cover;
  padding-top: 10%;
  padding-bottom: 10%;
}

#how-it-works {
  background-color: #000000;
  color: #dc3545;
  padding-top: 50px;
  padding-bottom: 50px;
}

#how-it-works h2 {
  font-size: 3rem;
  font-weight: bold;
}

body {
  background-color: black;
}

.Register_now {
  background-color: #dc3545;
  color: black;
  margin-left: 47%;
  border: none;
  padding: 10px 10px;
  display: flex;
}

.menu {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: black;
  color: #dc3545;
  padding: 10px;
  margin-left: 95%;
  border: none;
}
</style>
