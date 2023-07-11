import axios from "axios";

const BASE_URL = "http://127.0.0.1:5002/skins";

export const registerSkin = async (skin) => {
  try {
    const { data } = await axios.post(BASE_URL, skin, {
      headers: {
        "content-type": "application/json",
        // Agrega el token en el encabezado Authorization
      },
    });

    console.log("data: ", data);

    return data;
  } catch (error) {
    console.log("error here: ", error);
  }
};
