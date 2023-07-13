import axios from "axios";
import jwtDecode from "jwt-decode";

let token = localStorage.getItem("token");

const BASE_URL = "http://127.0.0.1:5002//users/<user_id>/skins";

const user_path =
  "http://127.0.0.1:5002/users/" + jwtDecode(token).user_created_id + "/skins";

let encabezado = {
  "Content-Type": "application/json",
  "X-ACCESS-TOKEN": token,
};

export const buyPost = async (postskin) => {
  try {
    // Agrega la propiedad headers al objeto del tercer argumento
    const response = await axios.post(user_path, postskin, {
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
