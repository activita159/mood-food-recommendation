# 工作流程

## 分支規則

- `main`：穩定版本分支，平常由整合者負責合併
- `feature/*`：個別功能分支，組員在自己的功能分支上開發

本專題目前不使用 PR 流程。組員完成後推上自己的 `feature/*` 分支，再通知整合者手動合併。

## 組員開發流程

1. 更新最新的 `main`
2. 從 `main` 建立自己的 `feature/*` 分支
3. 完成功能與基本測試
4. 推上自己的 feature 分支
5. 通知整合者分支名稱與完成內容

## 組員常用指令

```powershell
git checkout main
git pull origin main
git checkout -b feature/recommendation-api

git add .
git commit -m "feat: add recommendation api"
git push origin feature/recommendation-api
```

## 整合者合併流程

整合者收到組員通知後，在本機檢查並合併：

```powershell
git checkout main
git pull origin main
git fetch origin
git merge origin/feature/recommendation-api
```

如果沒有衝突，推回遠端：

```powershell
git push origin main
```

如果有衝突，先解衝突並測試，確認可執行後再 commit 與 push。

## 合併前檢查重點

- 是否符合既有資料結構與 API 規格
- API 行為改變時是否同步更新文件
- 後端是否可以正常啟動
- 前端是否可以正常啟動或 build
- 是否避免提交 `.env`、`venv`、`node_modules`
