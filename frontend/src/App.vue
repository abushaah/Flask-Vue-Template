<template>
  <div>
    <h1>Home</h1>

    <h2>Items</h2>
    <ul>
      <!-- loop through items defined in setup() -->
      <li v-for="item in items" :key="item.id">{{ item.name }}</li>
    </ul>

    <h2>Items Count Chart</h2>
    <BarChartWrapper
      :data="chartData"
      :options="chartOptions"
    />
  </div>
</template>

<script>
import axios from 'axios';
import { ref, defineComponent } from 'vue';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js';

import BarChartWrapper from './components/BarChartWrapper.vue';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

export default defineComponent({
  name: 'App',
  components: {
    BarChartWrapper
  },
  setup() {
    const items = ref([]);
    const chartData = ref({
      labels: [],
      datasets: [
        {
          label: 'Items',
          backgroundColor: '#42b983',
          data: []
        }
      ]
    });

    const chartOptions = {
      responsive: true,
      maintainAspectRatio: false
    };

    axios.get('http://localhost:5000/api/items')
      .then(response => {
        items.value = response.data;
        chartData.value.labels = items.value.map(item => item.name);
        chartData.value.datasets[0].data = items.value.map(() => 1);
      })
      .catch(err => {
        console.error('Failed to fetch items:', err);
      });

      console.log(chartData);
      console.log(chartOptions);
    return { items, chartData, chartOptions };
  }
});
</script>