# Mood Food Recommendation

心情導向餐廳與菜單推薦系統。這是一個學生團體專題的 monorepo 骨架，目標是讓使用者輸入心情、預算、人數、用餐目的、餐廳類型與地區後，由後端根據 mock 餐廳資料計算推薦分數，回傳適合的餐廳與推薦理由。

## 專案結構

- `frontend/`：Vue 3 + Vite 前端專案
- `backend/`：FastAPI 後端 API
- `docs/`：專題規格、API 文件、資料庫設計、工作流程與分工文件
- `.github/`：合併請求樣板

## 技術棧

- Frontend：Vue 3 + Vite
- Backend：FastAPI
- Data：MVP 階段使用 JSON mock data

## 啟動順序

開發時需要同時啟動後端與前端。建議先啟動後端，再啟動前端。

### 1. 啟動後端

```powershell
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

API 文件網址：

```text
http://localhost:8000/docs
```

### 2. 啟動前端

請開另一個終端機視窗執行：

```powershell
cd frontend
npm install
npm run dev
```

前端網址：

```text
http://localhost:5173
```

## 前後端資料傳遞方式

前端不直接讀取 `backend/app/data/` 裡的 JSON 檔案。所有資料都透過 FastAPI API 取得。

```text
Vue 前端 http://localhost:5173
  -> 使用 fetch 呼叫 API
FastAPI 後端 http://localhost:8000
  -> 讀取 mock JSON / 計算推薦
  -> 回傳 JSON 給前端
```

主要 API：

- `GET /api/restaurants`：取得餐廳列表
- `GET /api/restaurants/{restaurant_id}`：取得餐廳詳細資料
- `GET /api/restaurants/{restaurant_id}/menus`：取得餐廳菜單
- `POST /api/recommendations`：取得推薦餐廳
- `POST /api/favorites`：新增收藏
- `GET /api/favorites?user_id=1`：取得收藏清單
- `DELETE /api/favorites/{restaurant_id}?user_id=1`：刪除收藏

前端呼叫範例：

```js
const response = await fetch('http://localhost:8000/api/restaurants')
const result = await response.json()

console.log(result.data)
```

## Git 分支建議

- `main`：穩定版本分支
- `develop`：開發整合分支
- `feature/*`：個別功能分支
