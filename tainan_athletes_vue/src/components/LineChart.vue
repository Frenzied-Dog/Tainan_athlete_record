<template>
  <div>
    <canvas id="lineChart"></canvas>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

export default {
  props: {
    apiUrl: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      chart: null,
    };
  },
  async mounted() {
    try {
      const response = await fetch(this.apiUrl);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();

      const labels = data.map(item => item['日期']);
      const weights = data.map(item => item['體重 (kg)']);

      const ctx = document.getElementById('lineChart').getContext('2d');
      this.chart = new Chart(ctx, {
        type: 'line',
        data: {
          labels,
          datasets: [
            {
              label: '體重 (kg)',
              data: weights,
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 2,
            },
          ],
        },
      });
    } catch (error) {
      console.error('數據加載錯誤:', error);
    }
  },
  beforeDestroy() {
    if (this.chart) {
      this.chart.destroy();
    }
  },
};
</script>
