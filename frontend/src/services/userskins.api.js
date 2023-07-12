import axios from "axios";

const BASE_URL = "http://127.0.0.1:5002/skins";

export const registerSkin = async (skin) => {
  try {
    const response = await axios.post(BASE_URL, skin);
    const data = response.data;
    console.log("data: ", data);
    return data;
  } catch (error) {
    console.log("error: ", error);
    throw error;
  }
};
