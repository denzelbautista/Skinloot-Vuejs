<template>
  <div class="page-container">
    <navbar-market />
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-md-8">
          <h1 class="text-center">Search Skins</h1>
          <div class="input-group mb-3">
            <input
              type="text"
              class="form-control custom-input-group"
              placeholder="Search..."
            />
            <button class="btn btn-outline-danger" type="button">Search</button>
          </div>
          <div class="filter-box">
            <div class="row">
              <!-- Modified part -->
              <!-- Add a new column for the price order filter -->
              <div class="col-md-4">
                <label for="price-order-filter" class="form-label"
                  >Price Order:</label
                >
                <select
                  class="form-select custom-input-group"
                  id="price-order-filter"
                  @change="sortSkins"
                >
                  <!-- Add two options for the price order filter -->
                  <option value="">None</option>
                  <option value="desc">Most Expensive to Cheapest</option>
                  <option value="asc">Cheapest to Most Expensive</option>
                </select>
              </div>
              <!-- End of modified part -->
              <div class="col-md-4">
                <label for="rarity-filter" class="form-label">Rarity:</label>
                <select
                  class="form-select custom-input-group"
                  id="rarity-filter"
                >
                  <option value="">All</option>
                  <option value="common">Common</option>
                  <option value="rare">Rare</option>
                  <option value="epic">Epic</option>
                  <option value="legendary">Legendary</option>
                </select>
              </div>
              <div class="col-md-4">
                <label for="game-filter" class="form-label">Game:</label>
                <select class="form-select custom-input-group" id="game-filter">
                  <option value="">All</option>
                  <option value="game1">Game 1</option>
                  <option value="game2">Game 2</option>
                  <option value="game3">Game 3</option>
                </select>
              </div>
            </div>
          </div>

          <!-- Create a div with id "skins-container" to hold the skin boxes -->
          <div id="skins-container"></div>
        </div>
      </div>
      <asistente></asistente>
    </div>
    <post-skins></post-skins>
  </div>
</template>

<script scooped>
import NavbarMarket from "@/components/NavbarMarket.vue";
import PostSkins from "@/components/ShowPosts.vue";
import Asistente from "@/components/TestOpen.vue";

export default {
  name: "MarketView",
  components: {
    NavbarMarket,
    PostSkins,
    Asistente,
  },
  data() {
    return {};
  },
  methods: {
    sortSkins() {
      // Lógica para ordenar las skins
    },
  },
};
</script>

<style>
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
