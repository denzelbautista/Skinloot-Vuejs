// vue file
<template>
  <div>
    <h1>Preguntale a nuestro asistente</h1>
    <form @submit.prevent="submitMessage">
      <label for="message">Escribe una oración en inglés incorrecto:</label>
      <input id="message" v-model="message" />
      <button type="submit">Enviar</button>
    </form>
    <div v-if="response">
      <p>Esta es la corrección de GPT-3:</p>
      <p>{{ response }}</p>
    </div>
  </div>
</template>

<script>
import { ReceiveMessage } from "@/services/openai.api";

export default {
  data() {
    return {
      message: "",
      response: "",
    };
  },
  methods: {
    async submitMessage() {
      // send the message to the flask app route
      const data = await ReceiveMessage(this.message);
      // get the response from the json object
      this.response = data.response;
    },
  },
};
</script>
