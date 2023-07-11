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
    } else {
      throw new Error("Token not found in the response.");
    }
  } catch (error) {
    console.log("error here: ", error);
    throw error;
  }
};

export const getUserData = async (userId, token) => {
  try {
    const response = await axios.get(`${BASE_URL}/${userId}`, {
      headers: {
        "Content-Type": "application/json",
        "X-ACCESS-TOKEN": token,
      },
    });

    return response.data;
  } catch (error) {
    console.log("Error:", error);
    throw error;
  }
};
