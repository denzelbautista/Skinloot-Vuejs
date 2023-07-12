<template>
  <div class="all-posts">
    <h1>Todos los posts</h1>
    <div v-if="posts.length > 0">
      <!-- Usar un div con la clase row para envolver los posts -->
      <div class="row">
        <!-- Usar un div con la clase col-md-4 para cada post -->
        <div v-for="post in posts" :key="post.id" class="col-md-4">
          <!-- Usar la clase post-box para darle estilo al post -->
          <div class="post-box">
            <img :src="post.image" alt="Post image" />
            <h3>{{ post.title }}</h3>
            <p>{{ post.nombre }}</p>
            <p>{{ post.precio }}</p>
            <p>{{ post.campeon }}</p>
            <!-- Añadir un botón para ver el post -->
            <button class="view-button">View</button>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <p>No hay ningún post</p>
    </div>
  </div>
</template>

<script>
import { getPosts } from "@/services/userpost.api";
export default {
  name: "AllPosts",
  data() {
    return {
      posts: [],
    };
  },
  methods: {
    async loadPosts() {
      const { serialize } = await getPosts();
      this.posts = serialize;
    },
  },
  created() {
    this.loadPosts();
  },
};
</script>

<style>
/* Usar un css similar al de las skins, pero con otros colores */
.post-box {
  background-color: #1d1f1f;
  border-radius: 10px;
  margin-bottom: 50px;
  padding: 20px;
  text-align: center;
}

.post-box img {
  max-width: 100%;
  height: 200px;
  object-fit: contain;
}

.post-box h3 {
  font-size: 24px;
  margin-top: 20px;
  margin-bottom: 10px;
}

.post-box p {
  font-size: 18px;
  margin-bottom: 20px;
}

.view-button {
  background-color: #181e1e;
  border: none;
  color: #ffffff;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 18px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.view-button:hover {
  background-color: #0f3333;
}

/* Añadir un media query para pantallas pequeñas */
@media (max-width: 768px) {
  .col-md-4 {
    flex-basis: 100%;
    max-width: 100%;
    margin-left: auto;
    margin-right: auto;
  }
}
</style>
