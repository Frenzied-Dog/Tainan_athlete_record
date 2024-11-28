<template>
  <div v-if="visible" class="modal-overlay">
    <div class="modal">
      <h2>編輯個人資料</h2>
      <form @submit.prevent="submitEdit">
        <div class="form-group">
          <label for="name">姓名</label>
          <input type="text" id="name" v-model="formData.name" />
        </div>
        <div class="form-group">
          <label for="gender">性別（M / F / O）</label>
          <input type="text" id="gender" v-model="formData.gender">
        </div>
        <div class="form-group">
          <label for="birth">出生日期</label>
          <input type="text" id="birth" v-model="formData.birth" />
        </div>
        <div class="form-group">
          <label for="phone">聯絡電話</label>
          <input type="tel" id="phone" v-model="formData.phone" />
        </div>
        <div class="form-group">
          <label for="email">電子郵件</label>
          <input type="email" id="email" v-model="formData.email" />
        </div>
        <div class="form-group">
          <label for="address">地址</label>
          <input type="text" id="address" v-model="formData.address" />
        </div>
        <div class="modal-buttons">
          <button type="button" class="cancel-button" @click="closeModal">取消</button>
          <button type="submit" class="confirm-button">確認</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    visible: { type: Boolean, required: true }, // 控制彈窗是否顯示
    profile: { type: Object, required: true }, // 接收初始的 profile 資料
  },
  data() {
    return {
      formData: { ...this.profile }, // 初始化表單數據為傳入的 profile
    };
  },
  methods: {
    submitEdit() {
      this.$emit("confirm-edit", this.formData); // 將編輯後的資料傳回父組件
      this.closeModal();
    },
    closeModal() {
      this.$emit("close"); // 通知父組件關閉彈窗
    },
    // getGender(genderCode) {
    //   const genderMap = {
    //     M: "男",
    //     F: "女",
    //     O: "其他",
    //   };
    //   return genderMap[genderCode];
    // },
  },
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}
.modal {
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  width: 400px;
  max-width: 90%;
}
.form-group {
  margin-bottom: 15px;
}
.form-group label {
  display: block;
  margin-bottom: 5px;
}
.form-group input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}
.modal-buttons {
  display: flex;
  justify-content: space-between;
}
.confirm-button {
  background-color: #4caf50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.cancel-button {
  background-color: #f44336;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
