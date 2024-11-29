<!-- <template>
  <div>
    <canvas :id="chartId"></canvas>
  </div>
</template>

<script>
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

export default {
  props: {
    basicInfo: {
      type: Array,
      required: false, // 本地 JSON 數據，非必須
    },
    dataKey: {
      type: String,
      required: true, // 必須提供要繪製的欄位
    },
    fieldMappings: {
      type: Object,
      required: true, // 必須提供字段映射，用於顯示中文
    },
  },
  data() {
    return {
      chart: null, // Chart.js 實例
      chartId: `lineChart-${Math.random().toString(36).substr(2, 9)}`, // 動態生成唯一 ID
    };
  },
  watch: {
    // 當 dataKey 發生變化時，重新繪製圖表
    dataKey: {
      immediate: true,
      handler() {
        this.renderChart();
      },
    },
    // 當 basicInfo 發生變化時，重新繪製圖表
    basicInfo: {
      deep: true,
      handler() {
        this.renderChart();
      },
    },
    fieldMappings: {
      type: Object,
      required: true, // 必須提供字段映射，用於顯示中文
    },
  },
  methods: {
    async renderChart() {
      try {
        let data = [];
        // 如果有提供 basic_info，優先使用本地數據
        if (this.basicInfo && this.basicInfo.length > 0) {
          data = this.basicInfo;
        } else {
          console.warn("No data available for rendering chart");
          return;
        }

        // 準備圖表數據
        const labels = data.map((item) => item.test_date); // X 軸為測試日期
        const values = data.map((item) => item[this.dataKey] || 0); // Y 軸為選定的欄位值

        // 如果圖表已存在，銷毀舊圖表
        if (this.chart) {
          this.chart.destroy();
        }

        // 繪製圖表
        const ctx = document.getElementById(this.chartId).getContext("2d");
        this.chart = new Chart(ctx, {
          type: "line",
          data: {
            labels,
            datasets: [
              {
                label: this.fieldMappings[this.dataKey],
                data: values,
                borderColor: "rgba(75, 192, 192, 1)",
                borderWidth: 2,
              },
            ],
          },
        });
      } catch (error) {
        console.error("數據加載錯誤:", error);
      }
    },
  },
  mounted() {
    this.renderChart(); // 組件掛載時初始化圖表
  },
  beforeDestroy() {
    // 組件銷毀時清理圖表實例
    if (this.chart) {
      this.chart.destroy();
    }
  },
};
</script>

<style scoped>
canvas {
  max-width: 100%;
}
</style> -->

<template>
  <div>
    <canvas :id="chartId"></canvas>
  </div>
</template>

<script>
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

export default {
  props: {
    info: {
      type: Array,
      required: false, // 本地 JSON 數據，非必須
    },
    dataKey: {
      type: String,
      required: true, // 必須提供要繪製的欄位
    },
    fieldMappings: {
      type: Object,
      required: true, // 必須提供字段映射，用於顯示中文
    },
  },
  data() {
    return {
      chart: null, // Chart.js 實例
      chartId: `lineChart-${Math.random().toString(36).substr(2, 9)}`, // 動態生成唯一 ID
    };
  },
  watch: {
    // 當 dataKey 發生變化時，重新繪製圖表
    dataKey: {
      immediate: true,
      handler() {
        this.renderChart();
      },
    },
    // 當 info 發生變化時，重新繪製圖表
    info: {
      deep: true,
      handler() {
        this.renderChart();
      },
    },
    fieldMappings: {
      type: Object,
      required: true, // 必須提供字段映射，用於顯示中文
    },
  },
  methods: {
    async renderChart() {
      try {
        let data = [];
        // 如果有提供 basic_info，優先使用本地數據
        if (this.info && this.info.length > 0) {
          data = this.info;
        } else {
          console.warn("No data available for rendering chart");
          return;
        }

        // 準備圖表數據
        const labels = data.map((item) => item.test_date); // X 軸為測試日期
        const values = data.map((item) => item[this.dataKey] || 0); // Y 軸為選定的欄位值

        // 如果圖表已存在，銷毀舊圖表
        if (this.chart) {
          this.chart.destroy();
        }

        // 繪製圖表
        const ctx = document.getElementById(this.chartId).getContext("2d");
        this.chart = new Chart(ctx, {
          type: "line",
          data: {
            labels,
            datasets: [
              {
                label: this.fieldMappings[this.dataKey],
                data: values,
                borderColor: "rgba(75, 192, 192, 1)",
                borderWidth: 2,
              },
            ],
          },
        });
      } catch (error) {
        console.error("數據加載錯誤:", error);
      }
    },
  },
  mounted() {
    this.renderChart(); // 組件掛載時初始化圖表
  },
  beforeDestroy() {
    // 組件銷毀時清理圖表實例
    if (this.chart) {
      this.chart.destroy();
    }
  },
};
</script>

<style scoped>
canvas {
  max-width: 100%;
}
</style>
