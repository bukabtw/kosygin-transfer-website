<template>
  <div class="not-found-page">
    <div class="not-found-content">
      <h1 class="error-code">404</h1>
      <h2 class="error-title">Страница не найдена</h2>
      <p class="error-message">
        Похоже, вы заблудились. Страница, которую вы ищете, не существует или была перемещена.
      </p>
      <router-link to="/" class="home-button">Вернуться на главную</router-link>
    </div>
  </div>
</template>

<script setup>
// No script needed for this simple component
</script>

<style scoped>
.not-found-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--background-light);
  text-align: center;
  padding: 20px;
}

.not-found-content {
  max-width: 600px;
  animation: fadeIn 0.8s ease-out;
}

.error-code {
  font-size: 8rem;
  font-weight: 800;
  color: var(--primary-color);
  line-height: 1;
  margin-bottom: 20px;
  background: linear-gradient(135deg, var(--primary-color), var(--accent-blue));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.error-title {
  font-size: 2rem;
  margin-bottom: 20px;
  color: var(--text-dark);
}

.error-message {
  font-size: 1.2rem;
  color: var(--text-gray);
  margin-bottom: 40px;
  line-height: 1.6;
}

.home-button {
  display: inline-block;
  padding: 15px 30px;
  background-color: var(--accent-blue);
  color: white;
  text-decoration: none;
  border-radius: var(--radius-md);
  font-weight: 600;
  transition: all 0.3s ease;
  box-shadow: var(--shadow-md);
}

.home-button:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-lg);
  background-color: #3182ce;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
