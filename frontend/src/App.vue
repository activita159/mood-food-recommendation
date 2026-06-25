<script setup>
import { ref } from 'vue'

const apiBaseUrl = 'http://localhost:8000'

const isLoading = ref(false)
const errorMessage = ref('')
const apiResult = ref(null)

async function callApi(path, options = {}) {
  isLoading.value = true
  errorMessage.value = ''

  try {
    const response = await fetch(`${apiBaseUrl}${path}`, {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      ...options,
    })

    const result = await response.json()

    if (!response.ok) {
      throw new Error(result.detail || 'API 呼叫失敗')
    }

    apiResult.value = result
  } catch (error) {
    errorMessage.value = error.message
    apiResult.value = null
  } finally {
    isLoading.value = false
  }
}

function getRestaurants() {
  callApi('/api/restaurants')
}

function getRecommendations() {
  callApi('/api/recommendations', {
    method: 'POST',
    body: JSON.stringify({
      mood: '放鬆',
      budget: '中',
      people_count: 2,
      purpose: '約會',
      category: '火鍋',
      city: '台北市',
      district: '大安區',
    }),
  })
}
</script>

<template>
  <main class="app-shell">
    <section class="hero">
      <p class="eyebrow">Mood Food Recommendation</p>
      <h1>心情導向餐廳推薦系統</h1>
      <p class="summary">
        前端框架已初始化為 Vue 3 + Vite。接下來可以依照文件串接後端 API，
        建立條件輸入、推薦結果、餐廳詳情與收藏功能。
      </p>
    </section>

    <section class="status-panel">
      <h2>目前 API 目標</h2>
      <ul>
        <li><code>{{ apiBaseUrl }}/api/restaurants</code></li>
        <li><code>{{ apiBaseUrl }}/api/recommendations</code></li>
        <li><code>{{ apiBaseUrl }}/api/favorites</code></li>
      </ul>
    </section>

    <section class="api-tester">
      <div class="tester-header">
        <h2>API 測試</h2>
        <p>請先確認後端已在 <code>http://localhost:8000</code> 啟動。</p>
      </div>

      <div class="action-row">
        <button type="button" :disabled="isLoading" @click="getRestaurants">
          取得餐廳列表
        </button>
        <button type="button" :disabled="isLoading" @click="getRecommendations">
          測試推薦 API
        </button>
      </div>

      <p v-if="isLoading" class="loading-text">API 呼叫中...</p>
      <p v-if="errorMessage" class="error-text">{{ errorMessage }}</p>

      <pre v-if="apiResult" class="result-box">{{ JSON.stringify(apiResult, null, 2) }}</pre>
    </section>
  </main>
</template>
