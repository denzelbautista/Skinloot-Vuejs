import axios from "axios";

const BASE_URL = "http://127.0.0.1:5002/skins";

// const token = localstorage.getItem("token");

export const registerSkin = async (skin, token) => {
  try {
    const response = await axios.post(BASE_URL, skin, {
      headers: {
        "Content-Type": "application/json",
        "X-ACCESS-TOKEN": token, // Agrega el token en el encabezado de la solicitud
      },
    });
    const data = response.data;
    console.log("data: ", data);
    return data;
  } catch (error) {
    console.log("error: ", error);
    throw error;
  }
};
