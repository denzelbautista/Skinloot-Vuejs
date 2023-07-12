<template>
  <div>
    <h1>Preguntale a nuestro asistente</h1>
    <form @submit.prevent.stop="submitMessage">
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
      <button type="submit">Enviar</button>
    </form>
    <div v-if="response">
      <p>
        Esta es la corrección de GPT-3 y el comentario sobre
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
