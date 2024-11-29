<!-- <template>
  <div>
    <h1>運動員詳情</h1>
    <p v-if="loading">載入中...</p>
    <div v-else>
      <img :src="athlete.avatar || defaultAvatar" alt="運動員照片" />
      <h2>{{ athlete.name }}</h2>
      <p>年齡: {{ athlete.age || "未提供" }}</p>
      <p>簡介: {{ athlete.description || "無" }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      athlete: {}, // 運動員詳情
      loading: true,
      defaultAvatar: "@/assets/avatar-default.jpg",
    };
  },
  methods: {
    async fetchAthleteDetail() {
      try {
        const response = await axios.get(`http://localhost:8000/api/user-data/profile/${this.$route.params.id}`, {
          headers: {
            Authorization: `Token ${localStorage.getItem("Token")}`, // 添加 Authorization Header
          },
        });
        this.athlete = response.data;
        this.loading = false;
      } catch (error) {
        alert("獲取運動員詳情發生問題");
        console.error(error);
      }
    },
  },
  mounted() {
    this.fetchAthleteDetail(); // 組件掛載時請求運動員詳情
  },
};
</script>

<style scoped>
/* 根據需求設置樣式 */
</style> -->

<template>
  <div class="app-layout">
    <!-- 側欄 -->
    <CoachSidebar :profile="profile" :loading="loading" :athletes="athletes" />
    
    <!-- 主畫面 -->
    <div class="main-div">
      <!-- 上方列 -->
      <Upsidebar
        :title="'基本資料'"
        :profile="profile"
        @edit="openEditModal"
      />

      <!-- 主頁面 -->
      <main class="main-content">
        <!-- 編輯資料區域 -->
        <EditProfileModal
          v-if="isModalVisible"
          :visible="isModalVisible"
          :profile="profile"
          @confirm-edit="handleEditProfile"
          @close="isModalVisible = false"
        />
        <!-- 運動員資料卡片 -->
        <!-- <div v-if="!loading" class="profile-section">
          <h2 class="section-title" id="basicData">運動員資料</h2>
          <ProfileCard :profile="filteredAthletes" />
        </div> -->
      </main>

      <!-- 頁尾 -->
      <Footor />
    </div>
  </div>
</template>

<script>
import CoachSidebar from "@/components/CoachSidebar.vue";
import ProfileCard from "@/components/ProfileCard.vue";
import Footor from "@/components/Footor.vue";
import Upsidebar from "@/components/Upsidebar.vue";
import EditProfileModal from "@/components/EditProfileModal.vue";

import BasicInfoTable from "@/components/BasicInfoTable.vue";
import PhysicalTestTable from "@/components/PhysicalTestTable.vue";
import LineChart from '@/components/LineChart.vue';

import axios from "axios";

export default {
  name: "CoachAthleteDetail",
  components: {
    CoachSidebar,
    ProfileCard,
    Footor,
    Upsidebar,
    EditProfileModal,

    BasicInfoTable,
    PhysicalTestTable,
    LineChart,
  },
  data() {
    return {
      profile: {},
      athletes: null,
      loading: true,
      isModalVisible: false, // 控制彈窗顯示

      basic_info: {},
      physical_test: {},

      basicInfoFields: [
        "height",
        "weight",
        "BMI",
        "musule_mass",
        "body_fat",
      ],
      basicInfoFieldMappings: {
        height: "身高 (cm)",
        weight: "體重 (kg)",
        BMI: "BMI",
        musule_mass: "肌肉量 (kg)",
        body_fat: "體脂率 (%)",
      },
      selectedBasicInfoField: "height",

      physicalTestFields: [
        "vertical_jump",
        "agility",
        "grip_strength",
        "sprint_30m",
        "back_muscle_strength",
        "aerobic_fitness",
      ],
      physicalTestFieldMappings: {
        vertical_jump: "垂直跳 (cm)",
        agility: "敏捷性 (s)",
        grip_strength: "握力 (kg)",
        sprint_30m: "30M 衝刺 (s)",
        back_muscle_strength: "背肌力 (kg)",
        aerobic_fitness: "有氧適能",
      },
      selectedPhysicalTestField: "vertical_jump",
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
    async fetchAthleteProfile() {
      try {
        // 發送 GET 請求到 ProfileView 的 list 方法
        const response = await axios.get('http://localhost:8000/api/user-data/profile', {
          headers: {
            Authorization: `Token ${localStorage.getItem('Token')}`, // 添加 Authorization Header
          },
        });

        this.athletes = response.data;
        this.loading = false;

      } catch (error) {
        alert('獲取教練資料發生問題');
      }
    },
    openEditModal() {
      this.isModalVisible = true; // 顯示編輯彈窗
    },
    async handleEditProfile(updatedProfile) {
      // 從 Cookie 中獲取 CSRF Token
      const csrfToken = document.cookie
        .split("; ")
        .find((row) => row.startsWith("csrftoken"))
        ?.split("=")[1];

      // 發送 PATCH 請求到後端
      try {
        const response = await axios.patch(
          "http://localhost:8000/api/user-data/profile/${updatedProfile.id}/",
          updatedProfile, {
            headers: {
              Authorization: `Token ${localStorage.getItem("Token")}`,
              "X-CSRFToken": csrfToken,
          },
        });
        alert("資料更新成功");
        this.profile = response.data; // 更新前端顯示的資料
      } catch (error) {
        console.error("資料更新失敗：", error);
        alert("更新失敗，請稍後再試。");
      }
      this.isModalVisible = false; // 關閉彈窗
    },
  },
  mounted() {
    // 組件加載完成後請求資料
    this.fetchUserProfile();
    this.fetchAthleteProfile();
  },
  computed: {
    filteredAthletes() {
      // 過濾出 group = 1 的數據
      return this.athletes.filter(athlete => athlete.group === 1);
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
