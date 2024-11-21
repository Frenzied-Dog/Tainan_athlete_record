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
        <p>運動員</p>
      </div>
      <nav>
        <ul>
          <li>
            <span class="menu-title">>> 使用者基本資料</span>
            <ul class="submenu">
              <li><router-link to="/basic">> 基本資料</router-link></li>
              <li><router-link to="/training">> 教練資料</router-link></li>
            </ul>
          </li>
          <li>
            <span class="menu-title">>> 運動訓練數據紀錄</span>
            <ul class="submenu">
              <li><router-link to="/training-summary">> 總覽</router-link></li>
              <li><router-link to="/training-data">> 數據紀錄</router-link></li>
            </ul>
          </li>
          <li>
            <span class="menu-title">>> 健康紀錄</span>
            <ul class="submenu">
              <li><router-link to="/health-summary">> 總覽</router-link></li>
              <li><router-link to="/health-data">> 數據紀錄</router-link></li>
              <li><router-link to="/special-data">> 特殊紀錄</router-link></li>
            </ul>
          </li>
          <li><router-link class="menu-title" to="/competition">>> 競賽紀錄</router-link></li>
          <li><router-link class="menu-title" to="/nutrition">>> 營養</router-link></li>
          <li><router-link class="menu-title" to="/injury">>> 受傷紀錄</router-link></li>
        </ul>
      </nav>
    </aside>
    <!-- 主畫面 -->
    <div class="main-div">
      <main class="main-content">
        <h1>基本資料</h1>
        <!-- 運動員資料卡片 -->
        <div class="profile-section">
          <h2 class="section-title">運動員資料</h2>
          <div class="profile-card">
            <div class="profile-photo">
              <img src="@/assets/user-avatar.png" alt="運動員照片" />
            </div>
            <div class="profile-details">
              <p><strong>姓名：</strong>王小明</p>
              <p><strong>身分證字號：</strong>A123456789</p>
              <p><strong>性別：</strong>男</p>
              <p><strong>出生日期：</strong>1990/01/01</p>
              <p><strong>聯絡電話：</strong>0912-345-678</p>
              <p><strong>電子郵件：</strong>example@mail.com</p>
              <p><strong>地址：</strong>台南市中西區健康路一段100號</p>
            </div>
          </div>
        </div>

        <!-- 教練資料卡片 -->
        <div class="profile-section">
          <h2 class="section-title">教練資料</h2>
          <div class="profile-card">
            <div class="profile-photo">
              <img src="@/assets/coach-avatar.png" alt="教練照片" />
            </div>
            <div class="profile-details">
              <p><strong>姓名：</strong>李大華</p>
              <p><strong>身分證字號：</strong>B987654321</p>
              <p><strong>性別：</strong>男</p>
              <p><strong>出生日期：</strong>1985/05/15</p>
              <p><strong>聯絡電話：</strong>0987-654-321</p>
              <p><strong>電子郵件：</strong>coach@mail.com</p>
              <p><strong>地址：</strong>台北市大安區和平東路一段200號</p>
            </div>
          </div>
        </div>
      </main>
      <footer>
        <p>台南優秀運動員健康管理系統</p>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  name: "Sidebar",
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

.menu-title:hover {
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
  padding-bottom: 50px; /* 確保底部有 50px 空白區域 */
  box-sizing: border-box;
}

/* 主畫面區 */
.main-div {
  display: flex;
  flex-direction: column;
  flex: 1;
  position: relative;
}

/* 個人資料卡樣式 */
.profile-card {
  display: flex;
  align-items: flex-start;
  border: 1px solid #ddd;
  border-radius: 10px;
  padding: 20px;
  background-color: #f9f9f9;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px; /* 卡片之間的間距 */
}

.profile-photo img {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  margin-right: 20px; /* 圖片與文字之間的間距 */
}

.profile-details {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  text-align: left;
}

.profile-details p {
  margin: 5px 0;
  font-size: 16px;
}

.profile-details p strong {
  font-weight: bold;
}

/* 頁尾樣式 */
footer {
  position: relative; /* 修改為相對定位，避免遮擋主內容 */
  background-color: #f0f0f0;
  width: 100%;
  text-align: center;
  padding: 10px 0; /* 統一頁尾內邊距 */
  box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
}

footer p {
  font-size: small;
  margin: 0; /* 移除多餘的上下邊距 */
}

</style>
