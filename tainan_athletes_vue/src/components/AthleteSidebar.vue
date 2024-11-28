<template>
  <!-- 側欄 -->
  <aside class="sidebar">
    <div class="logo">
      <img src="@/assets/logo.png" alt="Logo" />
      <h2>台南優秀運動員<br />健康管理系統</h2>
    </div>
    <div class="user-info">
      <img v-if="!loading && profile.avatar" :src="profile.avatar" alt="運動員照片" class="user-avatar" />
      <img v-else src="@/assets/avatar-default.jpg" alt="未設定運動員照片" class="user-avatar" />
      <p v-if="!loading">{{ profile.name }}</p>
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
            <li><a href="#dataOverview">> 總覽</a></li>
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
</template>

<script>
export default {
  props: {
    profile: { type: Object, required: true }, // 接收 profile 資料作為 props
    loading: { type: Boolean, default: false }, // 接收 loading 狀態
  },
  methods: {
    getAvaUrl(relativePath) {
      const baseUrl = "http://localhost:8000"; // 替換為你的後端 URL
      return `${baseUrl}${relativePath}`;
    },
  },
};
</script>

<style scoped>
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
  overflow-y: auto; /* 修改為只垂直滾動 */
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
</style>
