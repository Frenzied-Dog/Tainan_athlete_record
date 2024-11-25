<template>
  <div class="app-layout">
    <!-- 專屬側邊欄 -->
    <Sidebar @changeSection="changeSection" />
    <div class="main-div">
      <!-- 上方列 -->
      <div class="upsidebar">
        <h1>王小明</h1>
        <button type="button" class="logout" @click="logout">登出</button> <!-- 觸發 js -->
      </div>
      <!-- 主內容區域 -->
      <main class="content">
        <div>
          <div v-if="currentSection === 'basic-info'">
            <AthleteData />
          </div>
          <div v-else-if="currentSection === 'training-data'">
            <TrainingData />
          </div>
          <div v-else-if="currentSection === 'competition-data'">
            <CompetitionData />
          </div>
          <div v-else-if="currentSection === 'health-data'">
            <HealthData />
          </div>
          <div v-else-if="currentSection === 'nutrition-data'">
            <NutritionData />
          </div>
          <div v-else-if="currentSection === 'injury-data'">
            <InjuryData />
          </div>
          <div v-else>
            <h2>請選擇一個功能</h2>
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
import Sidebar from "../components/CoachSidebar.vue"; // CoachA1 專屬的側邊欄
import AthleteData from "../components/AthleteData.vue"; // 子組件: 使用者基本資料
import TrainingData from "../components/TrainingData.vue"; // 子組件: 訓練數據
import CompetitionData from "../components/CompetitionData.vue"; // 子組件: 競賽數據
import HealthData from "../components/HealthData.vue"; // 子組件: 健康數據
import NutritionData from "../components/NutritionData.vue"; // 子組件: 營養數據
import InjuryData from "../components/InjuryData.vue"; // 子組件: 受傷記錄

export default {
  name: "CoachA1",
  components: {
    Sidebar,
    AthleteData,
    TrainingData,
    CompetitionData,
    HealthData,
    NutritionData,
    InjuryData,
  },
  data() {
    return {
      currentSection: "", // 當前選中的功能
    };
  },
  methods: {
    changeSection(section) {
      this.currentSection = section; // 切換主內容區域
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

/* 頁尾樣式 */
footer {
  position: relative;
  /* 避免遮擋主內容 */
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



.coach-a1 {
  display: flex;
  height: 100vh;
}

.sidebar {
  width: 250px;
  background-color: #1a2b47;
  color: white;
  padding: 20px;
}

.content {
  flex-grow: 1;
  padding: 20px;
}
</style>
