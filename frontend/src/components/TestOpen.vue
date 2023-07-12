<template>
  <div class="Asistente">
    <h1>Preguntale a nuestro asistente</h1>
    <form @submit.prevent.stop="submitMessage" class="skin-box">
      <label for="message">Quieres saber algo de un campeon?:</label>
      <input id="message" v-model="ups.message" />
      <div>
        <label>Champion Name:</label>
        <select v-model="ups.champion_name">
          <option value="Gragas">Gragas</option>
          <option value="jhin">Jhin</option>
          <option value="Shen">Shen</option>
        </select>
      </div>
      <button type="submit" class="buy-button">Enviar</button>
    </form>
    <div v-if="response" class="skin-box">
      <p>
        Respuesta de nuestro asistente
        {{ champion_name }}:
      </p>
      <p>{{ response }}</p>
    </div>
  </div>
</template>

<script>
import { ReceiveMessage } from "@/services/openai.api";

export default {
  data() {
    return {
      ups: {
        message: "",
        champion_name: "",
      },
      response: "",
    };
  },
  methods: {
    async submitMessage() {
      // send the message to the flask app route
      const data = await ReceiveMessage(this.ups);
      // get the response from the json object
      this.response = data.response;
    },
  },
};
</script>

<style scoped>
.Asistente {
  margin: 0 auto;
  max-width: 800px;
  padding: 20px;
}
.skin-box {
  background-color: #7f2626;
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
</style>
