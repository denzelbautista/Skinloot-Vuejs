<template>
  <div id="app">
    <router-link to="/market">Market</router-link> |
    <router-link to="/register">Register</router-link> |
    <router-link to="/userconfig">Config</router-link> |
    <router-link to="/about">registerskin</router-link> |

    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
#app {
  background-color: white;
}
</style>
