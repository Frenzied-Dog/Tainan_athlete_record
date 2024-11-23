<template>
  <div>
    <canvas id="lineChart"></canvas>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

export default {
  data() {
    return {
      chart: null,
    };
  },
  async mounted() {
    // 從 Django API 獲取數據
    const response = await fetch('http://127.0.0.1:8000/myapp/api/data/');
    const data = await response.json();

    // 處理數據
    const labels = data.map((item) => item['日期']);
    const weights = data.map((item) => item['體重 (kg)']); // 或其他你想要的欄位

    // 初始化折線圖
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
            fill: false,
          },
        ],
      },
    });
  },
  beforeDestroy() {
    // 清除圖表實例
    if (this.chart) {
      this.chart.destroy();
    }
  },
};
</script>
