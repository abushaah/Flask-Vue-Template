<template>
  <div>
    <h1>Items</h1>
    <ul>
      <li v-for="item in items" :key="item.id">{{ item.name }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      items: []
    };
  },
  mounted() {
    axios.get('http://localhost:5000/api/items')
      .then(response => {
        this.items = response.data;
      });
  }
};
</script>