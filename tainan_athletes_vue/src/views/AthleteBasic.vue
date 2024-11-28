<template>
  <div class="app-layout">
    <!-- 側欄 -->
    <AthleteSidebar :profile="profile" :loading="loading" />

    <!-- 主畫面 -->
    <div class="main-div">
      <!-- 上方列 -->
      <!-- <div class="upsidebar">
        <h1>基本資料</h1>
        <button type="button" class="logout" @click="logout">登出</button>
        <button type="button" class="edit" @click="edit">編輯</button>
      </div> -->
      <Upsidebar
        :title="'基本資料'"
        :profile="profile"
        @edit="handleEditProfile"
      />

      <!-- 主頁面 -->
      <main class="main-content">
        <!-- 運動員資料卡片 -->
        <div v-if="!loading" class="profile-section">
          <h2 class="section-title" id="basicData">運動員資料</h2>
          <ProfileCard :profile="profile" />
        </div>
        <!-- 教練資料卡片 -->
        <div class="profile-section">
          <h2 class="section-title" id="coachData">教練資料</h2>
          <div v-if="!loading">
            <ProfileCard v-for="coach in coaches" :key="coach.user" :profile="coach" />
          </div>
        </div>
      </main>

      <!-- 頁尾 -->
      <Footor />
    </div>
  </div>
</template>

<script>
import AthleteSidebar from "@/components/AthleteSidebar.vue";
import ProfileCard from "@/components/ProfileCard.vue";
import Footor from "@/components/Footor.vue";
import Upsidebar from "@/components/Upsidebar.vue";
import axios from "axios";

export default {
  name: "AtheleBasic",
  components: {
    AthleteSidebar,
    ProfileCard,
    Footor,
    Upsidebar,
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
    async handleEditProfile(profileData) {
      // 接收來自 UpSidebar 的 profile 資料，並執行後端更新邏輯
      try {
        const response = await axios.put(
          "http://localhost:8000/api/user-data/self/",
          profileData,
          {
            headers: {
              Authorization: `Token ${localStorage.getItem("Token")}`,
            },
          }
        );
        alert("資料更新成功");
        this.profile = response.data; // 更新資料顯示
      } catch (error) {
        console.error("資料更新失敗：", error);
        alert("更新失敗，請稍後再試。");
      }
    },
    // getGender(genderCode) {
    //     const genderMap = {
    //       M: "男",
    //       F: "女",
    //       O: "其他",
    //     };
    //     return genderMap[genderCode];
    // },
    // getAvaUrl(relativePath) {
    //   const baseUrl = "http://localhost:8000"; // 替換為你的後端 URL
    //   return `${baseUrl}${relativePath}`;
    // },
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
