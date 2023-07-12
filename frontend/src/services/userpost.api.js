import axios from "axios";
import jwtDecode from "jwt-decode";

let token = localStorage.getItem("token");
let decodedToken = jwtDecode(token).user_created_id;

const user_path = "http://127.0.0.1:5002/posts/" + decodedToken;

let encabezado = {
  "Content-Type": "application/json",
  "X-ACCESS-TOKEN": token,
};

export const registerPost = async (postskin) => {
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
