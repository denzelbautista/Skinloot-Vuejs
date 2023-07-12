// import axios from "axios";
// import jwtDecode from "jwt-decode";

// let token = localStorage.getItem("token");

// const BASE_URL = "http://127.0.0.1:5002/posts";

// const user_path =
//   "http://127.0.0.1:5002/posts/" + jwtDecode(token).user_created_id;

// let encabezado = {
//   "Content-Type": "application/json",
//   "X-ACCESS-TOKEN": token,
// };

// export const registerPost = async (postskin) => {
//   try {
//     // Agrega la propiedad headers al objeto del tercer argumento
//     const response = await axios.post(user_path, postskin, {
//       headers: encabezado,
//     });
//     const data = response.data;
//     console.log("data: ", data);
//     return data;
//   } catch (error) {
//     console.log("error: ", error);
//     throw error;
//   }
// };

// export const getPosts = async () => {
//   try {
//     const response = await axios.get(BASE_URL, { headers: encabezado });
//     const data = response.data;
//     console.log("data: ", data);
//     return data;
//   } catch (error) {
//     console.log("error: ", error);
//     throw error;
//   }
// };
