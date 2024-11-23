* Vue dir
  * `npm install chart.js`
* Django dir
  * `pip install pandas`
  * settings.py
    ```
    CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",  # Vue 項目地址
    ]
    ```
  * urls.py
    ```
    path('user_data/', include('user_data.urls')),  # 引入 user_data 的路由
    ```
  * views.py
    ```
    from django.http import JsonResponse
    import pandas as pd
    import os

    def get_data(request):
        # CSV 檔案的路徑 (修改為你 CSV 的實際路徑)
        file_path = os.path.join(os.path.dirname(__file__), '身體資料.csv')

        # 讀取 CSV 資料
        data = pd.read_csv(file_path)

        # 將資料轉換為 JSON 格式回傳
        return JsonResponse(data.to_dict(orient='records'), safe=False)

    ```