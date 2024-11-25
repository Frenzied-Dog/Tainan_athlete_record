<template>
    <!-- 運動員資料卡片 -->
    <div class="profile-section">
        <h2 class="section-title" id="basicData">運動員資料</h2>
        <div class="profile-card">
            <div class="profile-photo">
                <img src="@/assets/user-avatar.png" alt="運動員照片" />
            </div>
            <div class="profile-details">
                <p><strong>姓名：</strong>王小明</p>
                <p><strong>身分證字號：</strong>A123456789</p>
                <p><strong>性別：</strong>男</p>
                <p><strong>出生日期：</strong>1990/01/01</p>
                <p><strong>聯絡電話：</strong>0912-345-678</p>
                <p><strong>電子郵件：</strong>example@mail.com</p>
                <p><strong>地址：</strong>台南市中西區健康路一段100號</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "AthleteData",
};
</script>

<style>
/* 個人資料卡樣式 */
.profile-card {
    display: flex;
    align-items: flex-start;
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 20px;
    background-color: #f9f9f9;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
    /* 卡片之間的間距 */
}

.profile-photo img {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    margin-right: 20px;
    /* 圖片與文字之間的間距 */
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