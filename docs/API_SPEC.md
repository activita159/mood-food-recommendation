# API 規格

Base URL：

```text
http://localhost:8000
```

除了根路由以外，成功回應統一使用以下格式：

```json
{
  "data": {}
}
```

## GET /

確認 API 服務是否正在執行。

回應：

```json
{
  "message": "Mood Food API is running"
}
```

## GET /api/restaurants

取得餐廳列表摘要。

回應：

```json
{
  "data": [
    {
      "id": 1,
      "name": "暖鍋日常",
      "category": "火鍋",
      "city": "台北市",
      "district": "大安區",
      "rating": 4.6,
      "price_min": 280,
      "price_max": 520,
      "budget_level": "中",
      "distance_km": 1.2,
      "features": ["可訂位", "湯頭清爽", "適合聊天"]
    }
  ]
}
```

## GET /api/restaurants/{restaurant_id}

取得單一餐廳詳細資料。

錯誤狀態：

- `404 Restaurant not found`

## GET /api/restaurants/{restaurant_id}/menus

取得單一餐廳的菜單資料。

錯誤狀態：

- `404 Restaurant not found`
- `404 Menus not found`

## POST /api/recommendations

根據使用者輸入條件回傳推薦餐廳。

請求：

```json
{
  "mood": "放鬆",
  "budget": "中",
  "people_count": 2,
  "purpose": "約會",
  "category": "火鍋",
  "city": "台北市",
  "district": "大安區"
}
```

驗證規則：

- `mood` 必填
- `budget` 必填
- `people_count` 必填，且必須大於 0
- `purpose` 必填
- `category`、`city`、`district` 選填

推薦計分：

- `mood` 出現在 `restaurant.mood_tags`：+30
- `budget` 等於 `restaurant.budget_level`：+20
- `purpose` 出現在 `restaurant.purpose_tags`：+15
- `category` 等於 `restaurant.category`：+10
- `city` 等於 `restaurant.city`：+10
- `district` 等於 `restaurant.district`：+5
- `distance_km <= 2`：+10
- `rating >= 4.5`：+5

只回傳 `score > 0` 的餐廳，並依照分數由高到低排序。

回應：

```json
{
  "data": [
    {
      "id": 1,
      "name": "暖鍋日常",
      "category": "火鍋",
      "score": 95,
      "rating": 4.6,
      "price_min": 280,
      "price_max": 520,
      "budget_level": "中",
      "distance_km": 1.2,
      "reason": "符合你的「放鬆」心情, 預算等級符合「中」"
    }
  ]
}
```

## POST /api/favorites

新增收藏。同一個使用者重複收藏同一間餐廳時，不會重複新增。

請求：

```json
{
  "user_id": 1,
  "restaurant_id": 1
}
```

## GET /api/favorites?user_id=1

取得指定使用者的收藏餐廳列表。

## DELETE /api/favorites/{restaurant_id}?user_id=1

刪除指定使用者的某一筆餐廳收藏。
