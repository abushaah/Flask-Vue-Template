<template>
  <div>
    <nav class="navbar">
      <router-link to="/">Home</router-link>
      <!-- Add more links here -->
    </nav>

    <main class="main-content">
      <router-view />
    </main>
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style scoped>
.navbar {
  background-color:rgb(58, 83, 72);
  padding: 10px;
  display: flex;
  gap: 10px;
}

.navbar a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

.main-content {
  padding: 20px;
}
</style>
