<template>
  <div class="app-layout">
    <!-- 側欄 -->
    <AthleteSidebar :profile="profile" :loading="loading" />

    <!-- 主畫面 -->
    <div class="main-div">
      <!-- 上方列 -->
      <Upsidebar
        :title="'競賽紀錄'"
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
        <!-- 總覽 -->
        <!-- RaceRecord -->
        <h2 id="dataOverview">總覽</h2>
        <!-- 比賽紀錄表格 -->
        <div v-if="record && record.length">
          <RaceRecordTable
            v-for="rec in record"
            :key="rec.id"
            :record="rec"
          />
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
import EditProfileModal from "@/components/EditProfileModal.vue";
import RaceRecordTable from "@/components/RaceRecordTable.vue";
import axios from "axios";

export default {
  name: "AthleteCompetition",
  components: {
    AthleteSidebar,
    ProfileCard,
    Footor,
    Upsidebar,
    EditProfileModal,

    RaceRecordTable,
  },
  data() {
    return {
      profile: {},
      record: {},
      loading: true,
      coaches: null,
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
    async fetchRaceRecord() {
      try {
        const response = await axios.get('http://localhost:8000/api/record/Race', {
          headers: {
            Authorization: `Token ${localStorage.getItem('Token')}`, // 添加 Authorization Header
          },
        });

        this.record = response.data;
        this.loading = false;
      
      } catch {
        alert('獲取 RaceRecord 發生問題');
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
    this.fetchRaceRecord();
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
  box-sizing: border-box;
}

/* 主畫面區 */
.main-div {
  display: flex;
  flex-direction: column;
  flex: 1;
  position: relative;
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
  background-color: #f9f9f9;
  text-align: center;
}

.title-button:hover {
  cursor: pointer;
  background-color: #f0f0f0;
}

.title-tr {
  flex-wrap: wrap;
}

.th-title {
  width: 20%;
}
</style>
