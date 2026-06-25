# 工作流程

## 分支規則

- `main`：穩定版本分支，不直接推送
- `develop`：開發整合分支，不直接推送
- `feature/*`：個別功能分支

## 開發流程

1. 從 `develop` 更新最新版本
2. 建立自己的 `feature/*` 分支
3. 完成功能與基本測試
4. 發合併請求到 `develop`
5. 至少請一位組員 review
6. 合併前確認 API 文件與 mock data 是否同步更新

## 常用指令

```powershell
git checkout develop
git pull origin develop
git checkout -b feature/recommendation-api

git add .
git commit -m "feat: add recommendation api"
git push origin feature/recommendation-api
```

## PR 檢查重點

- 是否符合既有資料結構與 API 規格
- API 行為改變時是否同步更新文件
- 後端是否可以正常啟動
- 是否避免提交 `.env`、`venv`、`node_modules`
