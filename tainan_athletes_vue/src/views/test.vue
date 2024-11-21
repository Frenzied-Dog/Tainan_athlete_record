<template>
    <div class="dashboard">
        <!-- Header -->
        <div class="header">
            <h2>智發中心 - 秀琪</h2>
            <p>2024.11.18 13:22</p>
        </div>

        <!-- Profile Info -->
        <div class="profile">
            <img src="path/to/avatar.png" alt="Avatar" class="avatar" />
            <div class="info">
                <h3>王大明 - 運動員數據追蹤</h3>
                <p>籃球 | 台北隊</p>
            </div>
        </div>

        <!-- Navigation -->
        <div class="navigation">
            <button>基本資料</button>
            <button>體能測試</button>
            <button>傷病記錄</button>
            <button>比賽記錄</button>
        </div>

        <!-- Chart Section -->
        <div class="chart">
            <h3>體能測試趨勢</h3>
            <canvas id="performance-chart"></canvas>
        </div>
    </div>
</template>

<script>
import { ref, onMounted } from "vue";
import Chart from "chart.js/auto";

export default {
    setup() {
        const chartRef = ref(null);

        onMounted(() => {
            const ctx = document.getElementById("performance-chart").getContext("2d");
            new Chart(ctx, {
                type: "line",
                data: {
                    labels: ["2024-01", "2024-02", "2024-03"],
                    datasets: [
                        {
                            label: "垂直跳",
                            data: [75, 80, 78],
                            borderColor: "blue",
                            fill: false,
                        },
                        {
                            label: "速度",
                            data: [60, 65, 63],
                            borderColor: "green",
                            fill: false,
                        },
                    ],
                },
            });
        });

        return { chartRef };
    },
};
</script>

<style>
.dashboard {
    padding: 20px;
    font-family: Arial, sans-serif;
}

.header {
    text-align: left;
}

.profile {
    display: flex;
    align-items: center;
    margin: 20px 0;
}

.avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin-right: 20px;
}

.info h3 {
    margin: 0;
}

.navigation button {
    margin-right: 10px;
    padding: 5px 10px;
    border: none;
    background-color: #f2f2f2;
    cursor: pointer;
}

.navigation button:hover {
    background-color: #ddd;
}

.chart {
    margin-top: 20px;
}
</style>
