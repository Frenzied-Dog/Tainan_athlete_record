<template>
	<div class="login-container">
		<div class="login-card">
			<img src="@/assets/logo.png" alt="Logo" class="login-logo" />
			<h1 class="login-title">台南優秀運動員<br />健康管理系統</h1>
			<form @submit.prevent="handleLogin">
				<div class="form-group">
					<label for="username">使用者名稱</label>
					<input type="text" id="username" v-model="username" placeholder="請輸入使用者名稱" required />
				</div>
				<div class="form-group">
					<label for="password">密碼</label>
					<input type="password" id="password" v-model="password" placeholder="請輸入密碼" required />
				</div>
				<button type="submit" class="login-button">登入</button>
			</form>
		</div>
	</div>
</template>

<script>
import axios from "axios";

export default {
	data() {
		return {
			username: "",
			password: "",
		};
	},
	methods: {
		async handleLogin() {
			try {
				// 發送登入請求到 Django 後端
				const response = await axios.post("http://localhost:8000/api/user-data/auth/login/", {
					username: this.username,
					password: this.password,
				});

				// 從返回數據中獲取 Token 和 Group
				const { access, refresh, groups } = response.data;

				// 儲存 Token 到 localStorage
				localStorage.setItem("accessToken", access);
				localStorage.setItem("refreshToken", refresh);
				localStorage.setItem("userGroups", JSON.stringify(groups)); // 儲存 Group 信息

				// 根據 Group 導向對應的 Dashboard
				if (groups.includes("Coach")) {
					this.$router.push("/coach-basic");
				} else if (groups.includes("Athlete")) {
					this.$router.push("/athlete-basic");
					// this.$router.push("/athlete-train"); // add this
				} else {
					alert("未知群組，請聯繫管理員！");
				}
			} catch (error) {
				// 登入失敗時的提示
				if (error.response && error.response.status === 401) {
					console.log(error.response);
					alert("登入失敗，使用者名稱或密碼錯誤！");
				} else {
					console.log(error.response);
					alert("登入時發生錯誤，請稍後再試。");
				}
			}
		},
	},
};
</script>


<style scoped>
.login-container {
	display: flex;
	justify-content: center;
	align-items: center;
	height: 100vh;
	background-color: #1a2b47;
}

.login-card {
	background-color: #ffffff;
	border-radius: 10px;
	padding: 2rem;
	text-align: center;
	width: 400px;
	box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.login-logo {
	width: 100px;
	margin-bottom: 1rem;
}

.login-title {
	font-size: 1.5rem;
	color: #1a2b47;
	margin-bottom: 2rem;
}

.form-group {
	margin-bottom: 1.5rem;
	text-align: left;
}

label {
	font-size: 0.9rem;
	color: #1a2b47;
	display: block;
	margin-bottom: 0.5rem;
}

input {
	width: 95%; /* add this */
	padding: 0.8rem;
	padding: 0.8rem 0rem 0.8rem 1rem;
	border: 1px solid #ccc;
	border-radius: 5px;
	font-size: 1rem;
	color: #333;
}

input:focus {
	outline: none;
	border-color: #1a2b47;
	box-shadow: 0 0 3px rgba(26, 43, 71, 0.5);
}

.login-button {
	width: 100%;
	padding: 0.8rem;
	background-color: #0066cc;
	color: white;
	border: none;
	border-radius: 5px;
	font-size: 1rem;
	cursor: pointer;
}

.login-button:hover {
	background-color: #005bb5;
}
</style>
