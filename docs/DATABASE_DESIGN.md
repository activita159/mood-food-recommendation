# 資料庫設計

MVP 階段使用 JSON mock data，不連接正式資料庫。以下是未來可延伸的資料表設計。

## users

| 欄位 | 型別 | 說明 |
| --- | --- | --- |
| id | integer | 使用者 ID |
| name | varchar | 使用者名稱 |
| email | varchar | 電子信箱 |
| created_at | datetime | 建立時間 |

## restaurants

| 欄位 | 型別 | 說明 |
| --- | --- | --- |
| id | integer | 餐廳 ID |
| name | varchar | 餐廳名稱 |
| category | varchar | 餐廳類型 |
| city | varchar | 城市 |
| district | varchar | 行政區 |
| rating | decimal | 評分 |
| price_min | integer | 最低價格 |
| price_max | integer | 最高價格 |
| budget_level | varchar | 預算等級 |
| distance_km | decimal | 距離，單位為公里 |
| mood_tags | json | 心情標籤 |
| purpose_tags | json | 用餐目的標籤 |
| features | json | 餐廳特色 |
| address | varchar | 地址 |
| description | text | 餐廳描述 |

## restaurant_menus

| 欄位 | 型別 | 說明 |
| --- | --- | --- |
| id | integer | 菜單 ID |
| restaurant_id | integer | 餐廳 ID |
| name | varchar | 餐點名稱 |
| price | integer | 價格 |
| tags | json | 餐點標籤 |
| reason | text | 推薦理由 |

## favorites

| 欄位 | 型別 | 說明 |
| --- | --- | --- |
| id | integer | 收藏 ID |
| user_id | integer | 使用者 ID |
| restaurant_id | integer | 餐廳 ID |
| created_at | datetime | 建立時間 |

## food_records

| 欄位 | 型別 | 說明 |
| --- | --- | --- |
| id | integer | 紀錄 ID |
| user_id | integer | 使用者 ID |
| restaurant_id | integer | 餐廳 ID |
| mood | varchar | 當次心情 |
| budget | varchar | 當次預算 |
| purpose | varchar | 用餐目的 |
| rating | integer | 使用者回饋分數 |
| created_at | datetime | 建立時間 |
