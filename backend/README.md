# 後端

FastAPI 後端服務，負責提供餐廳列表、餐廳菜單、餐廳推薦與收藏功能 API。

## 安裝與啟動

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

API 文件網址：

```text
http://localhost:8000/docs
```

## 主要路由

- `GET /`：健康檢查與服務狀態
- `GET /api/restaurants`：取得餐廳列表
- `GET /api/restaurants/{restaurant_id}`：取得單一餐廳詳細資料
- `GET /api/restaurants/{restaurant_id}/menus`：取得單一餐廳菜單
- `POST /api/recommendations`：根據使用者條件取得推薦餐廳
- `POST /api/favorites`：新增收藏餐廳
- `GET /api/favorites?user_id=1`：取得指定使用者的收藏清單
- `DELETE /api/favorites/{restaurant_id}?user_id=1`：刪除指定收藏
