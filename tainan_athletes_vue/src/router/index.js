import axios, { Axios } from "axios";
import { createRouter, createWebHistory } from 'vue-router'
import LogIn from "../views/LogIn.vue";
import CoachDashboard from "../views/CoachDashboard.vue";
import AthleteDashboard from "../views/AthleteDashboard.vue";

const routes = [
  { path: "/login", name: "Login", component: LogIn },
  { path: "/coach-dashboard", name: "CoachDashboard", component: CoachDashboard },
  { path: "/athlete-dashboard", name: "AthleteDashboard", component: AthleteDashboard },
  { path: "/:pathMatch(.*)*", redirect: "/login" }, // 其他未知路徑導向 login
]

const router = createRouter({
  history: createWebHistory(),
  routes
});

// 導航守衛
router.beforeEach(async (to, from, next) => {
  const token = localStorage.getItem("accessToken");

  if (token) {
    try {
      // 驗證 Token
      await axios.post("http://localhost:8000/auth/jwt/verify/", { token });

      const groups = JSON.parse(localStorage.getItem("userGroups"));
      console.log("Groups: ", groups);
      // 有 Token 則跳過登入頁面，進入 Dashboard
      if (to.path === "/login") {
        // 使用 Group 信息進行導向
        if (groups.includes("Coach")) {
          next("/coach-dashboard");
        } else if (groups.includes("Athlete")) {
          next("/athlete-dashboard");
        } else {
          alert("未知群組，請聯繫管理員！");
          next("/login");
        }
      } else { next(); }
    } catch (error) {
      // Token 無效或過期
      localStorage.removeItem("accessToken");
      localStorage.removeItem("refreshToken");
      next("/login");
    }
  } else {
    // 無 Token，阻止訪問受保護路由，導向登入頁面
    if (to.path !== "/login") {
      next("/login");
    } else {
      next();
    }
  }
});

export default router;

