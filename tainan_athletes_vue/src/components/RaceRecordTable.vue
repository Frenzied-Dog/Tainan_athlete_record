<template>
  <div>
    <h3 id="dataOverview">{{ record.race_name }}</h3>
    <table class="overview-table">
      <tbody>
        <tr>
          <th class="th-title">比賽名稱</th>
          <td>{{ record.race_name }}</td>
        </tr>
        <tr>
          <th class="th-title">比賽日期</th>
          <td>{{ record.date }}</td>
        </tr>
        <tr>
          <th class="th-title">比賽描述</th>
          <td>{{ record.description }}</td>
        </tr>
        <tr>
          <th class="th-title">縮略圖</th>
          <td>
            <img
              v-if="record.thumbnail"
              :src="record.thumbnail"
              alt="比賽縮略圖"
              class="thumbnail-image"
            />
            <span v-else>無縮略圖</span>
          </td>
        </tr>
        <tr>
          <th class="th-title">證明文件</th>
          <td>
            <a
              v-if="record.proof"
              :href="record.proof"
              target="_blank"
              rel="noopener noreferrer"
            >
              點擊查看證明文件
            </a>
            <span v-else>無證明文件</span>
          </td>
        </tr>
        <tr>
          <th class="th-title">創建時間</th>
          <td>{{ formatDate(record.created_at) }}</td>
        </tr>
        <tr>
          <th class="th-title">最後更新時間</th>
          <td>{{ formatDate(record.updated_at) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "RaceRecordTable",
  props: {
    record: {
      type: Object,
      required: true,
    },
  },
  methods: {
    formatDate(datetime) {
      const date = new Date(datetime);
      return date.toLocaleString(); // 格式化日期時間為可讀形式
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

.th-title {
  width: 20%;
}

.thumbnail-image {
  max-width: 100px;
  max-height: 100px;
  display: block;
}
</style>
