import axios from "axios";
//import jwtDecode from "jwt-decode";

const BASE_URL = "http://127.0.0.1:5002/skins";

let token = localStorage.getItem("token");
//let decodedToken = jwtDecode(token).user_created_id;
let encabezado = {
  "Content-Type": "application/json",
  "X-ACCESS-TOKEN": token,
};
export const registerSkin = async (skin) => {
  try {
    // Agrega la propiedad headers al objeto del tercer argumento
    const response = await axios.post(BASE_URL, skin, { headers: encabezado });
    const data = response.data;
    console.log("data: ", data);
    return data;
  } catch (error) {
    console.log("error: ", error);
    throw error;
  }
};
