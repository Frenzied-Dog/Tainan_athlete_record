<template>
  <div class="app-layout">
    <!-- 側欄 -->
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
              <li><a href="/coach-a1">> 王小明</a></li>
              <li><a href="#athlete2">> 李曉華</a></li>
            </ul>
          </li>
        </ul>
      </nav>
    </aside>
    <!-- 主畫面 -->
    <div class="main-div">
      <!-- 上方列 -->
      <div class="upsidebar">
        <h1>運動員資料</h1>
        <button type="button" class="logout" @click="logout">登出</button> <!-- 觸發 js -->
      </div>
      <!-- 主頁面 -->
      <main class="main-content">
        <!-- 運動員資料卡片 1 -->
        <div class="profile-section">
          <div class="profile-card" @click="changePage1">
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
        <!-- 運動員資料卡片 2 -->
        <div class="profile-section">
          <div class="profile-card" @click="changePage2">
            <div class="profile-photo">
              <img src="@/assets/user2-avatar.png" alt="運動員照片" />
            </div>
            <div class="profile-details">
              <p><strong>姓名：</strong>李曉華</p>
              <p><strong>身分證字號：</strong>B987654321</p>
              <p><strong>性別：</strong>男</p>
              <p><strong>出生日期：</strong>1992/03/15</p>
              <p><strong>聯絡電話：</strong>0987-654-321</p>
              <p><strong>電子郵件：</strong>sample123@mail.com</p>
              <p><strong>地址：</strong>高雄市苓雅區中山路200號</p>
            </div>
          </div>
        </div>
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
    changePage1() {
      this.$router.push('/coach-a1');
    },
    changePage2() {
      this.$router.push('/coach-a2');
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

.profile-card:hover {
  cursor: pointer;
  background-color: #f0f0f0;
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
