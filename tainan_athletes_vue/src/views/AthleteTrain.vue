<template>
  <div class="app-layout">
    <!-- 側欄 -->
    <AthleteSidebar :profile="profile" :loading="loading" />
    
    <!-- 主畫面 -->
    <div class="main-div">
      <!-- 上方列 -->
      <Upsidebar
        :title="'運動訓練數據紀錄'"
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
        <!-- BasicInfo -->
        <BasicInfoTable v-if="!loading && (Object.keys(basic_info)).length" :data="basic_info" />
        <!-- PhysicalTest -->
        <PhysicalTestTable v-if="!loading && (Object.keys(physical_test)).length" :data="physical_test" />
        <!-- 數據分析 -->
        <!-- BasicInfo -->
        <h2 id="dataAnalyze">數據分析-身體數值</h2>
        <table class="overview-table">
          <thead>
            <th
              v-for="(label, field) in basicInfoFieldMappings"
              :key="field"
              class="title-button"
              @click="changeBasicInfoField(field)"
            >
              {{ label }}
            </th>
          </thead>
        </table>
        <LineChart
          v-if="!loading && basic_info.length && selectedBasicInfoField"
          :info="basic_info"
          :data-key="selectedBasicInfoField"
          :field-mappings="basicInfoFieldMappings"
        />
        <!-- PhysicalTest -->
        <h2>數據分析-物理測試</h2>
        <table class="overview-table">
          <thead>
            <th
              v-for="(label, field) in physicalTestFieldMappings"
              :key="field"
              class="title-button"
              @click="changePhysicalTestField(field)"
            >
              {{ label }}
            </th>
          </thead>
        </table>
        <LineChart
          v-if="!loading && physical_test.length && selectedPhysicalTestField"
          :info="physical_test"
          :data-key="selectedPhysicalTestField"
          :field-mappings="physicalTestFieldMappings"
        />
      </main>
      <!-- 頁尾 -->
      <Footor />
    </div>
  </div>
</template>

<script>
import AthleteSidebar from "@/components/AthleteSidebar.vue";
import Footor from "@/components/Footor.vue";
import Upsidebar from "@/components/Upsidebar.vue";
import EditProfileModal from "@/components/EditProfileModal.vue";

import BasicInfoTable from "@/components/BasicInfoTable.vue";
import PhysicalTestTable from "@/components/PhysicalTestTable.vue";
import LineChart from '@/components/LineChart.vue';

import axios from "axios";

export default {
  name: "AthleteTrain",
  components: {
    AthleteSidebar,
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
      loading: true,
      coaches: null,
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
    async fetchBasicInfo() {
      try {
        const response = await axios.get('http://localhost:8000/api/record/BasicInfo', {
          headers: {
            Authorization: `Token ${localStorage.getItem('Token')}`, // 添加 Authorization Header
          },
        });

        this.basic_info = response.data;
        // this.loading = false;
      
      } catch {
        alert('獲取 BasicInfo 發生問題');
      }
    },
    async fetchPhysicalTest() {
      try {
        const response = await axios.get('http://localhost:8000/api/record/PhysicalTest', {
          headers: {
            Authorization: `Token ${localStorage.getItem('Token')}`, // 添加 Authorization Header
          },
        });

        this.physical_test = response.data;
        this.loading = false;
      
      } catch {
        alert('獲取 PhysicalTest 發生問題');
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
        this.profile = response.data;
      } catch (error) {
        console.error("資料更新失敗：", error);
        alert("更新失敗，請稍後再試。");
      }
      this.isModalVisible = false;
    },
    changeBasicInfoField(field) {
      this.selectedBasicInfoField = field; // 更新選中的欄位
    },
    changePhysicalTestField(field) {
      this.selectedPhysicalTestField = field; // 更新選中的欄位
    },
  },
  mounted() {
    this.fetchUserProfile();
    this.fetchBasicInfo();
    this.fetchPhysicalTest();
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
</style>
