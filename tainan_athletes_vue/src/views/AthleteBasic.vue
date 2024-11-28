<template>
  <div class="app-layout">
    <!-- 側欄 -->
    <AthleteSidebar :profile="profile" :loading="loading" />
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
              <img v-if="profile.avatar" :src="getAvaUrl(profile.avatar)" alt="運動員照片" /> <!-- 載入完且有設定 avatar -->
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
import AthleteSidebar from "@/components/AthleteSidebar.vue";
import axios from "axios";

export default {
  name: "AtheleBasic",
  components: {
    AthleteSidebar,
  },
  data() {
    return {
      profile: {},
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
    getAvaUrl(relativePath) {
      const baseUrl = "http://localhost:8000"; // 替換為你的後端 URL
      return `${baseUrl}${relativePath}`;
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
