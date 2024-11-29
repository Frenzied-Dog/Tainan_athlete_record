<template>
  <div>
    <h2>總覽 - 物理測試</h2>
    <table class="overview-table">
      <thead>
        <tr>
          <th>垂直跳 (cm)</th>
          <th>敏捷性 (s)</th>
          <th>握力</th>
          <th>30M 衝刺</th>
          <th>背肌力</th>
          <th>有氧適能</th>
          <th>測試日期</th>
        </tr>
      </thead>
      <tbody>
        <!-- 使用 v-for 迴圈動態渲染數據 -->
        <tr v-for="item in data" :key="item.id">
          <td>{{ item.vertical_jump }}</td>
          <td>{{ formatValue(item.agility) }}</td>
          <td>{{ item.grip_strength }}</td>
          <td>{{ item.sprint_30m }}</td>
          <td>{{ item.back_muscle_strength }}</td>
          <td>{{ formatValue(item.aerobic_fitness) }}</td>
          <td>{{ formatDate(item.test_date) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "PhysicalTestTable",
  props: {
    // 接收物理測試數據作為 props
    data: {
      type: Array,
      required: true,
    },
  },
  methods: {
    // 格式化日期函數
    formatDate(date) {
      const options = { year: "numeric", month: "short", day: "numeric" };
      return new Date(date).toLocaleDateString(undefined, options);
    },
    // 格式化數據，處理 null 的情況
    formatValue(value) {
      return value !== null ? value : "N/A";
    },
  },
};
</script>

<style scoped>
/* 表格樣式 */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
  font-size: 16px;
  text-align: left;
}

table th,
table td {
  border: 1px solid #ddd;
  padding: 8px;
}

table th {
  background-color: #f9f9f9;
  text-align: center;
}
</style>
