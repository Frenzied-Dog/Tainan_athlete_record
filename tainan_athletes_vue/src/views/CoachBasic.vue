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
        <!-- 教練資料卡片 -->
        <div v-if="!loading" class="profile-section">
          <h2 class="section-title" id="basicData">教練資料</h2>
          <ProfileCard :profile="profile" />
        </div>
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
import axios from "axios";

export default {
  name: "CoachBasic",
  components: {
    CoachSidebar,
    ProfileCard,
    Footor,
    Upsidebar,
    EditProfileModal,
  },
  data() {
    return {
      profile: {},
      athletes: null,
      loading: true,
      isModalVisible: false, // 控制彈窗顯示
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
</style>