<template>
  <!-- 主頁面 -->
  <main class="main-content">
    <!-- 總覽 -->
    <!-- BasicInfo -->
    <h2 id="dataOverview">總覽-身體數值</h2>
    <table class="overview-table">
      <thead>
        <tr>
          <th>年齡</th>
          <th>身高</th>
          <th>體重</th>
          <th>BMI</th>
          <th>肌肉量</th>
          <th>體脂率</th>
          <th>測試日期</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>年齡</td>
          <td>身高</td>
          <td>體重</td>
          <td>BMI</td>
          <td>肌肉量</td>
          <td>體脂率</td>
          <td>測試日期</td>
        </tr>
        <tr>
          <td>年齡</td>
          <td>身高</td>
          <td>體重</td>
          <td>BMI</td>
          <td>肌肉量</td>
          <td>體脂率</td>
          <td>測試日期</td>
        </tr>
      </tbody>
    </table>
    <!-- PhysicalTest -->
    <h2>總覽-物理測試</h2>
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
        <tr>
          <td>垂直跳 (cm)</td>
          <td>敏捷性 (s)</td>
          <td>握力</td>
          <td>30M 衝刺</td>
          <td>背肌力</td>
          <td>有氧適能</td>
          <td>測試日期</td>
        </tr>
        <tr>
          <td>垂直跳 (cm)</td>
          <td>敏捷性 (s)</td>
          <td>握力</td>
          <td>30M 衝刺</td>
          <td>背肌力</td>
          <td>有氧適能</td>
          <td>測試日期</td>
        </tr>
      </tbody>
    </table>
    <br>
    <!-- 數據分析 -->
    <!-- BasicInfo -->
    <h2 id="dataAnalyze">數據分析-身體數值</h2>
    <table class="overview-table">
      <thead>
        <th v-for="field in fields" :key="field" class="title-button" @click="changeField(field)">{{ field }}
        </th>
      </thead>
    </table>
    <LineChart :api-url="'http://127.0.0.1:8000/user_data/api/data/'" :data-key="selectedField" />
    <!-- PhysicalTest -->
    <h2>數據分析-物理測試</h2>
    <table class="overview-table">
      <thead>
        <th v-for="field in fields" :key="field" class="title-button" @click="changeField(field)">{{ field }}
        </th>
      </thead>
    </table>
    <LineChart :api-url="'http://127.0.0.1:8000/user_data/api/data/'" :data-key="selectedField" />

    <!-- 詳細數據 -->
    <!-- <table class="dataframe table table-striped">
      <thead>
      <tr style="text-align: right;">
        <th>紀錄日期</th>
        <th>量測項目</th>
        <th>量測單位</th>
        <th>必填</th>
        <th>資料範圍</th>
        <th>數據</th>
      </tr>
      </thead>
      <tbody>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>跑步訓練狀態指數來源</td>
        <td></td>
        <td>否</td>
        <td>App、網站、手錶等</td>
        <td></td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>最大心率</td>
        <td>次數/每分鐘</td>
        <td>否</td>
        <td>0 ~ 999次數/每分鐘</td>
        <td>1</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>起始緯度</td>
        <td>緯度</td>
        <td>否</td>
        <td>0.0 ~ 99.99999緯度</td>
        <td>1.1</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>前腳掌壓力佔比(平均值)</td>
        <td>%</td>
        <td>否</td>
        <td>0.0 ~ 999.99百分比</td>
        <td>70.1</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>平均配速(秒/公里)</td>
        <td>秒/公里</td>
        <td>否</td>
        <td>0 ~ 99999秒/公里</td>
        <td>1</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>路線名稱</td>
        <td></td>
        <td>否</td>
        <td>騎車、跑步、健行等的路線名稱</td>
        <td></td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>狀況指數</td>
        <td>數值</td>
        <td>否</td>
        <td>0.0 ~ 9.9數值</td>
        <td>5.1</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>訓練指數</td>
        <td>數值</td>
        <td>否</td>
        <td>0.0 ~ 999.9數值</td>
        <td>500.1</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>比賽項目</td>
        <td></td>
        <td>否</td>
        <td>比賽項目，例：男子組單人</td>
        <td></td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>70%儲備心率</td>
        <td>次數/每分鐘</td>
        <td>否</td>
        <td>0 ~ 999次數/每分鐘</td>
        <td>160</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>疲勞指數</td>
        <td>數值</td>
        <td>否</td>
        <td>0.0 ~ 99.9數值</td>
        <td>40.1</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>消耗卡路里</td>
        <td>千卡</td>
        <td>否</td>
        <td>0.0 ~ 9999.9千卡</td>
        <td>1.3</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>總下降海拔</td>
        <td>公尺</td>
        <td>否</td>
        <td>0.0 ~ 9999.9公尺</td>
        <td>1.4</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>結束緯度</td>
        <td>緯度</td>
        <td>否</td>
        <td>0.0 ~ 99.99999緯度</td>
        <td>1.3</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>活動tcx檔</td>
        <td></td>
        <td>否</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>體能指數</td>
        <td>數值</td>
        <td>否</td>
        <td>0.0 ~ 99.9數值</td>
        <td>30.1</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>最大速度(公里/小時)</td>
        <td>公里/小時</td>
        <td>否</td>
        <td>0.0 ~ 99.9公里/小時</td>
        <td>1.1</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>結束經度</td>
        <td>經度</td>
        <td>否</td>
        <td>0.0 ~ 999.99999經度</td>
        <td>1.4</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>活動fit檔</td>
        <td></td>
        <td>否</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>比賽名稱</td>
        <td></td>
        <td>否</td>
        <td>比賽名稱</td>
        <td></td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>平均步頻</td>
        <td>步數/每分鐘</td>
        <td>否</td>
        <td>0.0 ~ 999.9步數/每分鐘</td>
        <td>1.1</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>跑步類型</td>
        <td></td>
        <td>否</td>
        <td>慢速長距離、乳酸閾值間歇訓練、5 公里競賽等</td>
        <td></td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>內旋過度</td>
        <td></td>
        <td>否</td>
        <td>0 ~ 9</td>
        <td>0</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>起始經度</td>
        <td>經度</td>
        <td>否</td>
        <td>0.0 ~ 999.99999經度</td>
        <td>1.2</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>最低海拔</td>
        <td>公尺</td>
        <td>否</td>
        <td>0.0 ~ 999.9公尺</td>
        <td>1.7</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>儲備心率</td>
        <td>次數/每分鐘</td>
        <td>否</td>
        <td>0 ~ 999次數/每分鐘</td>
        <td>120</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>平均速度(公里/小時)</td>
        <td>公里/小時</td>
        <td>是</td>
        <td>0.0 ~ 99.9公里/小時</td>
        <td>1.1</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>步數</td>
        <td>步</td>
        <td>否</td>
        <td>0 ~ 99999步</td>
        <td>1</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>最高步頻</td>
        <td>步數/每分鐘</td>
        <td>否</td>
        <td>0.0 ~ 999.9步數/每分鐘</td>
        <td>1.1</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>總爬升海拔</td>
        <td>公尺</td>
        <td>否</td>
        <td>0.0 ~ 9999.9公尺</td>
        <td>1.5</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>鞋子品牌(型號)</td>
        <td></td>
        <td>否</td>
        <td>跑步、健行等鞋子品牌或型號</td>
        <td></td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>跑步目標</td>
        <td></td>
        <td>否</td>
        <td>正式比賽;訓練</td>
        <td></td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>活動gpx檔</td>
        <td></td>
        <td>否</td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>後腳掌壓力佔比(平均值)</td>
        <td>%</td>
        <td>否</td>
        <td>0.0 ~ 999.99百分比</td>
        <td>29.5</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>距離(公里)</td>
        <td>公里</td>
        <td>是</td>
        <td>0.0 ~ 999.99公里</td>
        <td>1.5</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>比賽名次</td>
        <td></td>
        <td>否</td>
        <td>比賽名次</td>
        <td></td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>跑力</td>
        <td>估計值</td>
        <td>否</td>
        <td>0 ~ 99估計值</td>
        <td>80</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>步幅</td>
        <td>公尺</td>
        <td>否</td>
        <td>0.0 ~ 9.99公尺</td>
        <td>2.52</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>內旋不足</td>
        <td></td>
        <td>否</td>
        <td>0 ~ 9</td>
        <td>1</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>移動時間</td>
        <td>秒</td>
        <td>否</td>
        <td>0 ~ 99999秒</td>
        <td>1</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>最高海拔</td>
        <td>公尺</td>
        <td>否</td>
        <td>0.0 ~ 9999.9公尺</td>
        <td>1.6</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>花費時間</td>
        <td>秒</td>
        <td>是</td>
        <td>0 ~ 99999秒</td>
        <td>1</td>
      </tr>
      <tr>
        <td><time>2024-10-13</time></td>
        <td>平均心率</td>
        <td>次數/每分鐘</td>
        <td>否</td>
        <td>0.0 ~ 999.9次數/每分鐘</td>
        <td>1.1</td>
      </tr>
      </tbody>
    </table> -->
  </main>
</template>

<script>
import LineChart from '@/components/LineChart.vue'; // add for chart 

export default {
  name: "TrainingData",
  name: "TrainingDataPage",
  methods: {
    logout() {
      alert('您已登出');
      this.$router.push('/login'); // Vue Router 的導航方法
    },
    changeField(field) {
      this.selectedField = field; // 更新選中的欄位
    },
  },
  components: { // add for chart 
    LineChart,
  },
  data() {
    return {
      // 可選欄位
      fields: [
        '身高',
        '體重',
        'BMI',
        '肌肉量',
        '體脂率',
      ],
      // 預設選擇的欄位
      selectedField: '體重 (kg)',
    };
  },
};
</script>

<style>
/* 主畫面樣式 */
.main-content {
  flex: 1;
  background-color: #ffffff;
  overflow-y: auto;
  padding: 20px;
  box-sizing: border-box;
}

/* 主畫面區 */
.main-div {
  display: flex;
  flex-direction: column;
  flex: 1;
  position: relative;
}

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

.title-button:hover {
  cursor: pointer;
  background-color: #f0f0f0;
}

.title-tr {
  flex-wrap: wrap;
}
</style>