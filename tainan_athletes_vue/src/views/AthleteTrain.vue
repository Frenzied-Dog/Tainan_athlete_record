<template>
  <div class="app-layout">
    <!-- 側欄 -->
    <aside class="sidebar">
      <div class="logo">
        <img src="@/assets/logo.png" alt="Logo" />
        <h2>台南優秀運動員<br />健康管理系統</h2>
      </div>
      <div class="user-info">
        <img class="user-avatar" src="@/assets/user-avatar.png" alt="User Avatar" />
        <p>王小明</p>
      </div>
      <nav>
        <ul>
          <li>
            <span class="menu-title"><router-link to="/athlete-basic">>> 使用者基本資料</router-link></span>
            <ul class="submenu">
              <li><a href="#basicData">> 基本資料</a></li>
              <li><a href="#coachData">> 教練資料</a></li>
            </ul>
          </li>
          <li>
            <span class="menu-title"><router-link to="/athlete-train">>> 運動訓練數據紀錄</router-link></span>
            <ul class="submenu">
              <li><a href="#dataRecord">> 總覽</a></li>
              <li><a href="#dataAnalyze">> 數據分析</a></li>
            </ul>
          </li>
          <li>
            <span class="menu-title"><router-link to="/athlete-competition">>> 競賽紀錄</router-link></span>
            <ul class="submenu">
              <li><a href="#">> 總覽</a></li>
              <li><a href="#">> 數據紀錄</a></li>
              <li><a href="#">> 特殊紀錄</a></li>
            </ul>
          </li>
          <li><span class="menu-title"><router-link to="/athlete-health">>> 健康紀錄</router-link></span></li>
          <li><span class="menu-title"><router-link to="/athlete-nutrition">>> 營養紀錄</router-link></span></li>
          <li><span class="menu-title"><router-link to="/athlete-hurt">>> 受傷紀錄</router-link></span></li>
        </ul>
      </nav>
    </aside>
    <!-- 主畫面 -->
    <div class="main-div">
      <!-- 上方列 -->
      <div class="upsidebar">
        <h1>運動訓練數據紀錄</h1>
        <button type="button" class="logout" @click="logout">登出</button> <!-- 觸發 js -->
      </div>
      <!-- 主頁面 -->
      <main class="main-content">
        <h2 id="dataRecord">總覽</h2>
        <table class="dataframe table table-striped">
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
        </table>
        <h2 id="dataAnalyze">數據分析</h2>
      </main>
      <!-- 頁尾 -->
      <footer>
        <p>台南優秀運動員健康管理系統</p>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  name: "TrainingDataPage",
  methods: {
    logout() {
      alert('您已登出');
      this.$router.push('/login'); // Vue Router 的導航方法
    },
  },
};
</script>

<style scoped>
/* App 布局樣式 */
.app-layout {
  display: flex;
  height: 100vh;
  overflow: hidden;
  background-color: #ffffff;
}

/* 側欄樣式 */
.sidebar {
  background-color: #1a2b47;
  color: #ffffff;
  width: 250px;
  display: flex;
  flex-direction: column; /* 垂直排列內容 */
  padding: 20px;
  box-sizing: border-box;
}

nav {
  overflow-y: auto; /* 垂直滾動 */
}

/* Logo 區域樣式 */
.logo {
  margin-bottom: 20px;
  text-align: center;
}

.logo img {
  max-width: 80px;
  height: auto;
  margin: 0 auto 10px;
}

.logo h2 {
  font-size: 16px;
  font-weight: bold;
  margin: 0;
  line-height: 1.2;
  position: relative;
  top: -5px; /* 向上微調文字 */
}

/* 使用者資訊樣式 */
.user-info {
  margin-bottom: 20px;
  text-align: center;
}

.user-avatar {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  margin-bottom: 10px;
}

.user-info p {
  font-size: 16px;
  margin: 0;
}

/* 列表樣式 */
ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  text-align: left;
}

li {
  margin-bottom: 15px;
}

.menu-title {
  font-size: 14px;
  font-weight: bold;
  padding-left: 30px;
  color: #ffffff;
  text-decoration: none;
  cursor: pointer;
}

.menu-title a {
  color: #ffffff;
  text-decoration: none;
}

.menu-title:hover {
  color: #43d895;
}

.menu-title a:hover {
  color: #43d895;
}

.submenu {
  padding-left: 60px;
}

.submenu li {
  margin-bottom: 8px;
}

.submenu li a {
  font-size: 14px;
  color: #ffffff;
  text-decoration: none;
}

.submenu li a:hover {
  color: #43d895;
}

a.router-link-exact-active {
  color: #43d895;
}

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

/* 頁尾樣式 */
footer {
  position: relative; /* 避免遮擋主內容 */
  background-color: #f0f0f0;
  width: 100%;
  text-align: center;
  padding: 10px 0;
  box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
}

footer p {
  font-size: small;
  margin: 0;
}

/* 上方列 */
.upsidebar {
  position: relative;
  background-color: #f0f0f0;
  width: 100%;
  height: 60px;
  text-align: center;
  box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
}

.upsidebar h1 {
  position: relative;
  top: -10px;
  text-align: center;
}

.logout {
  position: absolute;
  right: 20px;
  top: 25px;
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
  background-color: #f2f2f2;
  text-align: center;
}
</style>
