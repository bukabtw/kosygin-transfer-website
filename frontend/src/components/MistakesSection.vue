<script setup>
import { onMounted } from 'vue'

const mistakes = [
  {
    title: 'Незаверенные копии',
    text: 'Копии документов должны быть заверены печатью вуза. Обычные ксерокопии не принимаются.',
    icon: '❌'
  },
  {
    title: 'Отсутствие лицензии вуза',
    text: 'Для негосударственных вузов обязательны копии лицензии и аккредитации.',
    icon: '❌'
  },
  {
    title: 'Большая академическая разница',
    text: 'Разница более 8 дисциплин или 30 зачетных единиц - основная причина отказа.',
    icon: '❌'
  },
  {
    title: 'Пропуск сроков подачи',
    text: 'Документы принимаются только в установленные периоды - проверяйте дедлайны!',
    icon: '❌'
  },
  {
    title: 'Неполный пакет документов',
    text: 'Отсутствие любого из обязательных документов ведет к отказу в рассмотрении.',
    icon: '❌'
  },
  {
    title: 'Ошибки в заявлении',
    text: 'Некорректно заполненные данные или ошибки в названии специальности могут стать причиной отказа.',
    icon: '📝'
  }
]

onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible')
      }
    })
  }, { threshold: 0.1 })

  document.querySelectorAll('.section-animate').forEach(el => {
    observer.observe(el)
  })
})
</script>

<template>
  <section id="mistakes" class="mistakes-section">
    <h2 class="section-title">Частые ошибки</h2>
    <div class="mistakes-container">
      <div 
        v-for="(mistake, index) in mistakes" 
        :key="index"
        class="mistake-card section-animate"
        :style="{ transitionDelay: `${index * 0.1}s` }"
      >
        <div class="mistake-icon">{{ mistake.icon }}</div>
        <div class="mistake-content">
          <h3>{{ mistake.title }}</h3>
          <p>{{ mistake.text }}</p>
        </div>
      </div>
    </div>

    <div class="mistakes-tip section-animate" style="transition-delay: 0.3s">
      <div class="tip-icon">💡</div>
      <div class="tip-content">
        <h3>Важный совет</h3>
        <p>Перед подачей документов обязательно проконсультируйтесь с деканатом и используйте наш чек-лист для проверки готовности!</p>
        <a href="#checklist" class="tip-button">Проверить готовность</a>
      </div>
    </div>
  </section>
</template>

<style scoped>
/* Scoped styles removed to rely on global style.css */
</style>
