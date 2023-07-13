import axios from "axios";

const BASE_URL = "http://127.0.0.1:5002/process_message";

let token = localStorage.getItem("token");
let encabezado = {
  "Content-Type": "application/json",
  "X-ACCESS-TOKEN": token,
};

export const ReceiveMessage = async (message) => {
  try {
    // Agrega la propiedad headers al objeto del tercer argumento
    const response = await axios.post(BASE_URL, message, {
      headers: encabezado,
    });
    const data = response.data;
    console.log("data: ", data);
    return data;
  } catch (error) {
    console.log("error: ", error);
    throw error;
  }
};
