<template>
  <div class="upsidebar">
    <h1>{{ title }}</h1>
    <button type="button" class="logout" @click="handleLogout">登出</button>
    <button type="button" class="edit" @click="handleEdit">編輯</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    title: { type: String, default: "標題" }, // 動態傳入標題
    profile: { type: Object, required: true }, // 傳入 profile 資料，用於編輯
  },
  methods: {
    async handleLogout() {
      try {
        localStorage.removeItem('Token'); // 移除 Token
        await axios.get('http://localhost:8000/api/user-data/auth/logout/'); // 發送登出請求
        axios.defaults.headers.common['Authorization'] = ''; // 清除 axios 的 Authorization Header
        alert('您已登出');
        this.$router.push('/login'); // Vue Router 的導航方法
      } catch (error) {
        console.error("登出失敗：", error);
        alert("登出失敗，請稍後再試。");
      }
    },
    handleEdit() {
      this.$emit("edit", this.profile); // 傳遞 profile 資料到父組件進行處理
    },
  },
};
</script>

<style scoped>
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
