import axios from "axios";

const BASE_URL = "http://127.0.0.1:5002/users";

export const registerUser = async (user) => {
  try {
    const { data } = await axios.post(BASE_URL, user);
    console.log("data: ", data);

    if (data && data.token) {
      console.log("token: ", data.token);
      console.log("id: ", data.id);
      return data;
    }
  } catch (error) {
    console.log("error here: ", error);
    throw error;
  }
};
