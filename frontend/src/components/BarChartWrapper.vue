<template>
  <div class="chart-container">
    <Bar :data="unwrappedData" :options="options" v-if="unwrappedData && unwrappedData.labels?.length" />
  </div>
</template>

<script>
import { defineComponent, computed, isRef } from 'vue';
import { Bar } from 'vue-chartjs';

export default defineComponent({
  name: 'BarChartWrapper',
  components: { Bar },
  props: {
    data: { type: Object, required: true },
    options: { type: Object, required: true }
  },
  setup(props) {
    const unwrappedData = isRef(props.data) ? props.data.value : props.data;
    console.log(unwrappedData);
    return { unwrappedData };
  }
});
</script>

<style scoped>
.chart-container {
  height: 300px;
  max-width: 600px;
  position: relative;
}
</style>
