import axios, { Axios } from "axios";
import { createRouter, createWebHistory } from 'vue-router'
import LogIn from "../views/LogIn.vue";
import AthleteBasic from "../views/AthleteBasic.vue";
import AthleteTrain from "../views/AthleteTrain.vue";
import AthleteCompetition from "../views/AthleteCompetition.vue";
import CoachBasic from "../views/CoachBasic.vue";
import CoachAthlete from "../views/CoachAthlete.vue";
import CoachA1 from "../views/CoachA1.vue";

const routes = [
    { path: "/login", name: "Login", component: LogIn },
    { path: "/athlete-basic", name: "AthleteBasic", component: AthleteBasic },
    { path: "/athlete-train", name: "AthleteTrain", component: AthleteTrain },
    { path: "/athlete-competition", name: "AthleteCompetition", component: AthleteCompetition },
    { path: "/coach-basic", name: "CoachBasic", component: CoachBasic },
    { path: "/coach-athlete", name: "CoachAthlete", component: CoachAthlete },
    { path: "/coach-a1", name: "CoachA1", component: CoachA1 },
    { path: "/:pathMatch(.*)*", redirect: "/login" }, // 其他未知路徑導向 login
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

// 導航守衛
router.beforeEach(async (to, from, next) => {
    const token = localStorage.getItem("Token");

    if (token) {
        try {
            // 驗證 Token
            const responce = await axios.get("http://localhost:8000/api/user-data/info/");

            // 有 Token 則跳過登入頁面，進入 Dashboard
            if (to.path === "/login") {


                const group = responce.data.group;
                if (group.includes("Coach")) {
                    next("/coach-baisc");
                } else if (group.includes("Athlete")) {
                    next("/athlete-basic");
                } else {
                    alert("未知群組，請聯繫管理員！");
                    next("/login");
                }

            } else { next(); }
        } catch (error) {
            // 驗證失敗，清除 Token，導向登入頁面
            alert("驗證失敗，請重新登入！");
            localStorage.removeItem("Token");
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

