<template>
  <aside class="sidebar">
    <div class="logo">
      <img src="@/assets/logo.png" alt="Logo" />
      <h2>台南優秀運動員<br />健康管理系統</h2>
    </div>
    <div class="user-info">
      <img class="user-avatar" src="@/assets/coach-avatar.png" alt="User Avatar" />
      <p>李大華</p>
    </div>
    <nav>
      <ul>
        <li>
          <span class="menu-title"><router-link to="/coach-basic">>> 使用者基本資料</router-link></span>
          <ul class="submenu">
            <!-- <li><a href="#basicData">> 基本資料</a></li> -->
            <!-- <li><a href="#coachData">> 教練資料</a></li> -->
          </ul>
        </li>
        <li>
          <span class="menu-title"><router-link to="/coach-athlete">>> 運動員資料</router-link></span>
          <ul class="submenu">
            <!-- <li><a href="#athlete1">> 王曉明</a></li>
        <li><a href="#athlete2">> 李曉華</a></li> -->
          </ul>
        </li>
      </ul>
      <!-- 運動員側邊欄 -->
      <div class="athlete-info">
        <img class="user-avatar" src="@/assets/user-avatar.png" alt="User Avatar" />
        <p>王小明</p>
      </div>
      <ul>
        <li @click="$emit('changeSection', 'basic-info')">
          <span class="menu-title">>> 使用者基本資料</span>
          <ul class="submenu">
            <li><a href="#basicData">> 基本資料</a></li>
            <li><a href="#coachData">> 教練資料</a></li>
          </ul>
        </li>
        <li @click="$emit('changeSection', 'training-data')">
          <span class="menu-title">>> 運動訓練數據紀錄</span>
          <ul class="submenu">
            <!-- <li><a href="#dataRecord">> 總覽</a></li>
            <li><a href="#dataAnalyze">> 數據分析</a></li> -->
          </ul>
        </li>
        <li @click="$emit('changeSection', 'competition-data')">
          <span class="menu-title">>> 競賽紀錄</span>
          <ul class="submenu">
            <!-- <li><a href="#">> 總覽</a></li>
              <li><a href="#">> 數據紀錄</a></li>
              <li><a href="#">> 特殊紀錄</a></li> -->
          </ul>
        </li>
        <li @click="$emit('changeSection', 'health-data')"><span class="menu-title">>> 健康紀錄</span></li>
        <li @click="$emit('changeSection', 'nutrition-data')"><span class="menu-title">>> 營養紀錄</span></li>
        <li @click="$emit('changeSection', 'injury-data')"><span class="menu-title">>> 受傷紀錄</span></li>
      </ul>
    </nav>
  </aside>
</template>

<script>
export default {
  name: "CoachSidebar",
};
</script>

<style scoped>
/* 側欄樣式 */
.sidebar {
  background-color: #1a2b47;
  color: #ffffff;
  width: 250px;
  display: flex;
  flex-direction: column;
  /* 垂直排列內容 */
  padding: 20px;
  box-sizing: border-box;
}

nav {
  overflow-y: auto;
  /* 垂直滾動 */
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
  top: -5px;
  /* 向上微調文字 */
}

/* 使用者資訊樣式 */
.user-info {
  margin-bottom: 20px;
  text-align: center;
  /* flex-direction: row; */
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

.athlete-info {
  margin-bottom: 20px;
  margin-top: 10px;
  text-align: center;
}

.athlete-info .user-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-bottom: 10;
}

.athlete-info p {
  font-size: 14px;
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
