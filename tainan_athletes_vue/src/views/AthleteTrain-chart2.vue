<template>
  <div>
    <h2 id="dataRecord">總覽</h2>
        <table class="dataframe table table-striped">
          <thead>
            <tr style="text-align: right;">
              <th class="title-button">基本資料</th>
              <th class="title-button">體能測試</th>
              <th class="title-button">傷病紀錄</th>
              <th class="title-button">營養紀錄</th>
            </tr>
          </thead>
          <!-- <tbody>
            <tr>
              <td><time>2024-10-13</time></td>
              <td>跑步訓練狀態指數來源</td>
              <td></td>
              <td>否</td>
            </tr>
          </tbody> -->
        </table>
    <LineChart :api-url="'http://127.0.0.1:8000/user_data/api/data/'" />
  </div>
</template>

<script>
import LineChart from '@/components/LineChart.vue';

export default {
  components: {
    LineChart,
  },
};
</script>
