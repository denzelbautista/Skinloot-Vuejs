<template>
  <div id="app">
    <router-link to="/market">Market</router-link>
    <router-link to="/register">Register</router-link>
    <router-link to="/userconfig">Config</router-link>
    <router-view />
  </div>
</template>

<style>
#app {
  background-color: black;
}
</style>
