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
    dataKey: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      chart: null,
      // isRendering: false, // 新增：鎖機制標誌
    };
  },
  watch: {
    // 監聽 dataKey 的變化，當欄位改變時重繪圖表
    dataKey: {
      immediate: true,
      handler() {
        this.fetchAndRenderChart();
      },
    },
  },
  methods: {
    async fetchAndRenderChart() {
      // if (this.isRendering) return; // 如果正在渲染，直接返回
      // this.isRendering = true; // 設置渲染鎖
      try {
        const response = await fetch(this.apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // 根據選擇的欄位準備數據
        const labels = data.map(item => item['日期']); // X 軸為日期
        const values = data.map(item => item[this.dataKey]); // Y 軸為選定的欄位

        // 如果圖表已存在，先銷毀
        if (this.chart) {
          this.chart.destroy();
        }

        // 繪製圖表
        const ctx = document.getElementById('lineChart').getContext('2d');
        this.chart = new Chart(ctx, {
          type: 'line',
          data: {
            labels,
            datasets: [
              {
                label: this.dataKey,
                data: values,
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
  },
  beforeDestroy() {
    if (this.chart) {
      this.chart.destroy();
    }
  },
};
</script>
