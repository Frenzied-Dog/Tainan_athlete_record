<template>
	<div class="app-layout">
		<!-- 側欄 -->
		<div class="sidebar">
			<div class="logo">
				<img src="@/assets/logo.png" alt="Logo" />
				<h2>台南優秀運動員<br />健康管理系統</h2>
			</div>
			<div class="user-info">
				<img class="user-avatar" src="@/assets/user-avatar.png" alt="User Avatar" />
				<p>運動員</p>
			</div>
			<nav>
				<ul>
					<li>
						<span class="menu-title">>> 使用者基本資料</span>
						<ul class="submenu">
							<li><router-link to="/basic">> 基本資料</router-link></li>
							<li><router-link to="/training">> 教練資料</router-link></li>
						</ul>
					</li>
					<li>
						<span class="menu-title">>> 運動訓練數據紀錄</span>
						<ul class="submenu">
							<li><router-link to="/training-summary">> 總覽</router-link></li>
							<li><router-link to="/training-data">> 數據紀錄</router-link></li>
						</ul>
					</li>
					<li>
						<span class="menu-title">>> 健康紀錄</span>
						<ul class="submenu">
							<li><router-link to="/health-summary">> 總覽</router-link></li>
							<li><router-link to="/health-data">> 數據紀錄</router-link></li>
							<li><router-link to="/special-data">> 特殊紀錄</router-link></li>
						</ul>
					</li>
					<li><router-link class="menu-title" to="/competition">>> 競賽紀錄</router-link></li>
					<li><router-link class="menu-title" to="/nutrition">>> 營養</router-link></li>
					<li><router-link class="menu-title" to="/injury">>> 受傷紀錄</router-link></li>
				</ul>
			</nav>
		</div>

		<!-- 主畫面 -->
		<div class="main-content">
			<router-view />
		</div>
	</div>
</template>

<script>
export default {
	name: "Sidebar",
};
</script>

<style scoped>
/* App 布局樣式 */
.app-layout {
	display: flex;
	height: 100vh;
	overflow: hidden;
}

/* 側欄樣式 */
.sidebar {
	background-color: #1a2b47;
	color: #ffffff;
	width: 250px;
	display: flex;
	flex-direction: column;
	/* 使用 Flex 排版 */
	padding: 20px;
	box-sizing: border-box;
}

/* Logo 區域樣式 */
.logo {
	margin-bottom: 20px;
	text-align: center;
}

.logo img {
	max-width: 80px;
	/* 縮小 Logo 大小 */
	height: auto;
	margin: 0 auto 10px;
	/* 上下居中對齊，並增加間距 */
}

.logo h2 {
	font-size: 12px;
	/* 調整文字大小 */
	margin: 0;
	line-height: 1.2;
	position: relative;
	top: -5px;
	/* 向上移動文字 */
}

/* 使用者資訊樣式 */
.user-info {
	margin-bottom: 20px;
	text-align: center;
}

.user-avatar {
	width: 70px;
	/* 縮小使用者頭像 */
	height: 70px;
	border-radius: 50%;
	margin-bottom: 10px;
}

.user-info p {
	font-size: 14px;
	margin: 0;
}

/* 列表樣式 */
ul {
	list-style: none;
	/* 移除默認的圓點符號 */
	margin: 0;
	padding: 0;
	display: flex;
	flex-direction: column;
	/* 垂直排列子項 */
	text-align: left;
}

li {
	margin-bottom: 15px;
	/* 強制子項目之間的間距 */
}

/* 標題樣式 */
.menu-title {
	font-size: 14px;
	font-weight: bold;
	padding-left: 30px;
	color: #ffffff;
	text-decoration: none;
	/* 移除底線 */
	cursor: pointer;
	/* 滑鼠移過時變成手指 */
}

.menu-title:hover {
	color: #43d895;
	/* 滑鼠滑過時變為綠色 */
}

/* 子選單樣式 */
.submenu {
	padding-left: 60px;
	/* 向內縮排 */
}

.submenu li {
	margin-bottom: 8px;
	/* 子選單項目之間的間距 */
}

.submenu li a {
	font-size: 14px;
	color: #ffffff;
	text-decoration: none;
	/* 移除底線 */
}

.submenu li a:hover {
	color: #43d895;
	/* 滑過效果 */
}

a.router-link-exact-active {
	color: #43d895;
	/* 選中的顏色 */
}

/* 主畫面樣式 */
.main-content {
	flex: 1;
	background-color: #ffffff;
	/* 主畫面背景色設為白色 */
	overflow-y: auto;
	/* 主畫面可滾動 */
	padding: 20px;
	box-sizing: border-box;
}
</style>
