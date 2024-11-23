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
    try {
      // 發送請求獲取數據
      const response = await fetch('http://127.0.0.1:8000/user_data/api/data/');
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      // 確保返回的是 JSON 格式
      const data = await response.json();
      console.log('獲取的數據:', data);

      // 處理數據，構建圖表
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
      console.error('數據請求或處理錯誤:', error);
    }
  },
  beforeDestroy() {
    // 清理圖表實例
    if (this.chart) {
      this.chart.destroy();
    }
  },
};
</script>
