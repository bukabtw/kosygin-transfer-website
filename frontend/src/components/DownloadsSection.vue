<template>
  <section class="downloads-section section-animate" id="downloads" ref="sectionRef">
    <h2 class="section-title">Все документы одним архивом</h2>
    <div class="downloads-container">
      
      <div class="downloads-card">
        <div class="downloads-icon">📦</div>
        <div class="downloads-content">
          <h3>Полный пакет документов для перевода</h3>
          <p>Скачайте все необходимые бланки, формы и примеры заполнения в одном ZIP-архиве. Экономьте время - не ищите по отдельности!</p>
          
          <div class="files-list">
            <div v-for="(file, index) in files" :key="index" class="file-item">
              <span class="file-icon">📄</span>
              <span class="file-name">{{ file.name }}</span>
              <span class="file-size">{{ file.size }}</span>
            </div>
          </div>
          
          <div class="downloads-info">
            <div class="info-item">
              <span class="info-icon">⚡</span>
              <span>Всего {{ files.length }} документов</span>
            </div>
            <div class="info-item">
              <span class="info-icon">📁</span>
              <span>Общий размер: ~400 КБ</span>
            </div>
            <div class="info-item">
              <span class="info-icon">🕒</span>
              <span>Актуально на 2025 год</span>
            </div>
          </div>
          
          <a href="#" class="download-archive-button" @click.prevent="downloadArchive">
            <span class="button-icon">💾</span>
            Скачать ZIP-архив (400 КБ)
          </a>
          
          <div class="downloads-note">
            <p>💡 <strong>Совет:</strong> После скачивания распакуйте архив и проверьте все документы по нашему чек-листу</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const sectionRef = ref(null)

const files = [
  { name: 'Бланк заявления о переводе', size: '(PDF, 45 КБ)' },
  { name: 'Согласие на обработку персональных данных', size: '(PDF, 38 КБ)' },
  { name: 'Образец справки об обучении', size: '(PDF, 52 КБ)' },
  { name: 'Пример заполнения заявления', size: '(PDF, 68 КБ)' },
  { name: 'Положение о порядке перевода', size: '(PDF, 120 КБ)' },
  { name: 'Чек-лист документов', size: '(PDF, 35 КБ)' }
]

const downloadArchive = () => {
  // Logic to download archive (mocked)
  alert('Скачивание архива начнется автоматически...')
}

onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible')
        observer.unobserve(entry.target)
      }
    })
  }, { threshold: 0.1 })

  if (sectionRef.value) {
    observer.observe(sectionRef.value)
  }
})
</script>
