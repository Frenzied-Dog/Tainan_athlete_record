<template>
  <div>
    <h2 id="dataOverview">總覽 - 身體數值</h2>
    <table class="overview-table">
      <thead>
        <tr>
          <th>年齡</th>
          <th>身高 (cm)</th>
          <th>體重 (kg)</th>
          <th>BMI</th>
          <th>肌肉量 (kg)</th>
          <th>體脂率 (%)</th>
          <th>測試日期</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in data" :key="item.id">
          <td>{{ item.age }}</td>
          <td>{{ item.height }}</td>
          <td>{{ item.weight }}</td>
          <td>{{ item.BMI }}</td>
          <td>{{ item.musule_mass }}</td>
          <td>{{ item.body_fat }}</td>
          <td>{{ formatDate(item.test_date) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "BasicInfoTable",
  props: {
    // JSON 數據作為組件的 prop 傳入
    data: {
      type: Array,
      required: true,
    },
  },
  methods: {
    // 格式化日期函式
    formatDate(date) {
      const options = { year: "numeric", month: "short", day: "numeric" };
      return new Date(date).toLocaleDateString(undefined, options);
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
