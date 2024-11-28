<template>
  <div class="profile-card">
    <div class="profile-photo">
      <img v-if="profile.avatar" :src="getAvaUrl(profile.avatar)" alt="照片" />
      <img v-else src="@/assets/avatar-default.jpg" alt="未設定照片" />
    </div>
    <div class="profile-details">
      <p><strong>姓名：</strong>{{ profile.name }}</p>
      <p><strong>性別：</strong>{{ getGender(profile.gender) }}</p>
      <p v-if="profile.birth"><strong>出生日期：</strong>{{ profile.birth }}</p>
      <p v-else><strong>出生日期：</strong>尚未設定</p>
      <p v-if="profile.phone"><strong>聯絡電話：</strong>{{ profile.phone }}</p>
      <p v-else><strong>聯絡電話：</strong>尚未設定</p>
      <p v-if="profile.email"><strong>電子郵件：</strong>{{ profile.email }}</p>
      <p v-else><strong>電子郵件：</strong>尚未設定</p>
      <p v-if="profile.address"><strong>地址：</strong>{{ profile.address }}</p>
      <p v-else><strong>地址：</strong>尚未設定</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    profile: { type: Object, required: true }, // 接收動態 profile 資料
  },
  methods: {
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
};
</script>

<style scoped>
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
</style>
