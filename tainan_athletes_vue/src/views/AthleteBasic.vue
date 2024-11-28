<template>
  <div class="app-layout">
    <!-- 側欄 -->
    <aside class="sidebar">
      <div class="logo">
        <img src="@/assets/logo.png" alt="Logo" />
        <h2>台南優秀運動員<br />健康管理系統</h2>
      </div>
      <div class="user-info">
        <img v-if="!loading && profile.avatar" :src=getAvaUrl(profile.avatar) alt="運動員照片" class="user-avatar"/>
        <img v-else src="@/assets/avatar-default.jpg" alt="未設定運動員照片" class="user-avatar"/>
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
        <h1>基本資料</h1>
        <button type="button" class="logout" @click="logout">登出</button>
        <button type="button" class="edit" @click="edit">編輯</button>
      </div>
      <!-- 主頁面 -->
      <main class="main-content">
        <!-- 運動員資料卡片 -->
        <div v-if="!loading" class="profile-section">
          <h2 class="section-title" id="basicData">運動員資料</h2>
          <div class="profile-card">
            <div class="profile-photo">
              <img v-if="profile.avatar" :src=getAvaUrl(profile.avatar) alt="運動員照片" /> <!-- 載入完且有設定 avatar -->
              <img v-else src="@/assets/avatar-default.jpg" alt="未設定運動員照片" />
            </div>
            <div class="profile-details">
              <p><strong>姓名：</strong>{{ profile.name }}</p>
              <p><strong>性別：</strong>{{ getGender(profile.gender) }}</p>
              <p v-if="profile.birth"><strong>出生日期：</strong>{{ profile.birth }}</p>
              <p v-else><strong>出生日期：</strong>尚未設定</p>
              <p v-if="profile.phone"><strong>聯絡電話：</strong>{{ profile.phone }}</p>
              <p v-else><strong>聯絡電話：</strong>尚未設定</p>
              <p v-if="profile.email"><strong>電子郵件：</strong>{{ profile.email}}</p>
              <p v-else><strong>電子郵件：</strong>尚未設定</p>
              <p v-if="profile.address"><strong>地址：</strong>{{ profile.address }}</p>
              <p v-else><strong>地址：</strong>尚未設定</p>
            </div>
          </div>
        </div>

        <!-- 教練資料卡片 -->
        <div class="profile-section">
          <h2 class="section-title" id="coachData">教練資料</h2>
          <div v-if="!loading">
            <div v-for="coach in coaches" :key="coach.user">
              <div class="profile-card">
                <div class="profile-photo">
                  <img v-if="coach.avatar" :src="coach.avatar" alt="運動員照片" />
                  <img v-else src="@/assets/avatar-default.jpg" alt="未設定運動員照片" />
                </div>
                <div class="profile-details">
                  <p><strong>姓名：</strong>{{ coach.name }}</p>
                  <p><strong>性別：</strong>{{ getGender(coach.gender) }}</p>
                  <p v-if="profile.birth"><strong>出生日期：</strong>{{ coach.birth }}</p>
                  <p v-else><strong>出生日期：</strong>尚未設定</p>
                  <p v-if="profile.phone"><strong>聯絡電話：</strong>{{ coach.phone }}</p>
                  <p v-else><strong>聯絡電話：</strong>尚未設定</p>
                  <p v-if="profile.email"><strong>電子郵件：</strong>{{ coach.email}}</p>
                  <p v-else><strong>電子郵件：</strong>尚未設定</p>
                  <p v-if="profile.address"><strong>地址：</strong>{{ coach.address }}</p>
                  <p v-else><strong>地址：</strong>尚未設定</p>
                </div>
              </div>
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
import axios from "axios";

export default {
  name: "AtheleBasic",
  data() {
    return {
      profile: null,
      loading: true,
      coaches: null,
    };
  },
  methods: {
    async fetchUserProfile() {
      try {
        const response = await axios.get('http://localhost:8000/api/user-data/self/', {
          headers: {
            Authorization: `Token ${localStorage.getItem('Token')}`, // 添加 Authorization Header
          },
        });

        this.profile = response.data;
        // this.loading = false;

      } catch {
        alert('獲取 Profile 發生問題');
      }
    },
    async fetchCoachProfile() {
      try {
        // 發送 GET 請求到 ProfileView 的 list 方法
        const response = await axios.get('http://localhost:8000/api/user-data/profile', {
          headers: {
            Authorization: `Token ${localStorage.getItem('Token')}`, // 添加 Authorization Header
          },
        });

        this.coaches = response.data;
        this.loading = false;

      } catch (error) {
        alert('獲取教練資料發生問題');
      }
    },
    async logout() {
      localStorage.removeItem('Token'); // 移除 Token
      await axios.get('http://localhost:8000/api/user-data/auth/logout/'); // 發送登出請求
      axios.defaults.headers.common['Authorization'] = ''; // 清除 axios 的 Authorization Header
      alert('您已登出');
      this.$router.push('/login'); // Vue Router 的導航方法
    },
    getGender(genderCode) {
        const genderMap = {
          M: "男",
          F: "女",
          O: "其他",
        };
        return genderMap[genderCode];
    },
    getAvaUrl(avaCode) {
      return "http://localhost:8000" + avaCode;
    },
  },
  mounted() {
    // 組件加載完成後請求資料
    this.fetchUserProfile();
    this.fetchCoachProfile();
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

.edit {
  position: absolute;
  right: 65px;
  top: 25px;
}

.logout {
  position: absolute;
  right: 20px;
  top: 25px;
}
</style>
