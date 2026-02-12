<template>
  <section id="checklist" class="checklist-section">
    <h2 class="section-title section-animate">Готов ли ты к переводу?</h2>
    <div class="checklist-container">
      <div 
        ref="checklistCardRef"
        class="checklist-card section-animate"
        :class="{ 'visible': isVisible }"
      >
        <div class="checklist-progress">
          <div class="progress-bar">
            <div class="progress-fill" :style="{ width: progressPercentage + '%' }"></div>
          </div>
          <div class="progress-text">Готовность: {{ Math.round(progressPercentage) }}%</div>
        </div>
        
        <div class="checklist-items">
          <label 
            v-for="(item, index) in items" 
            :key="index" 
            class="checklist-item" 
            :class="{ completed: item.checked }"
          >
            <input 
              type="checkbox" 
              class="checklist-checkbox" 
              v-model="item.checked"
              @change="updateProgress"
            >
            <span class="checkmark"></span>
            {{ item.text }}
          </label>
        </div>
        
        <div class="checklist-result" :class="{ 'completed': isCompleted }">
          {{ resultMessage }}
          <span v-if="isCompleted" class="completion-icon">🎉</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import confetti from 'canvas-confetti'

const items = ref([
  { text: 'Справка об обучении (текущий месяц)', checked: false },
  { text: 'Справка о статусе студента (текущий месяц)', checked: false },
  { text: 'Копия паспорта (фото + прописка)', checked: false },
  { text: 'Копия СНИЛС', checked: false },
  { text: 'Заявление о переводе (заполнено)', checked: false },
  { text: 'Согласие на обработку персональных данных', checked: false },
  { text: 'Копии лицензии и аккредитации вуза (для негосударственных)', checked: false },
  { text: 'Уточнены вакантные места', checked: false },
  { text: 'Получена консультация деканата', checked: false },
  { text: 'Оценена академическая разница', checked: false }
])

const messages = [
  "Начни отмечать готовые документы!",
  "Так держать! Продолжай собирать документы",
  "Уже неплохо! Еще немного усилий",
  "Отлично! Ты на верном пути",
  "Почти готово! Остались последние штрихи",
  "Идеально! Ты полностью готов к переводу!"
]

const checklistCardRef = ref(null)
const isVisible = ref(false)

const progressPercentage = computed(() => {
  const checkedCount = items.value.filter(item => item.checked).length
  return (checkedCount / items.value.length) * 100
})

const isCompleted = computed(() => progressPercentage.value === 100)

const resultMessage = computed(() => {
  let index = Math.floor(progressPercentage.value / 20)
  if (index >= messages.length) index = messages.length - 1
  if (index < 0) index = 0
  return messages[index]
})

const updateProgress = () => {
  saveProgress()
}

const saveProgress = () => {
  const progress = {}
  items.value.forEach((item, index) => {
    progress[index] = item.checked
  })
  localStorage.setItem('checklistProgress', JSON.stringify(progress))
}

const loadProgress = () => {
  try {
    const saved = JSON.parse(localStorage.getItem('checklistProgress')) || {}
    items.value.forEach((item, index) => {
      if (saved[index]) {
        item.checked = true
      }
    })
  } catch (e) {
    console.warn('Не удалось загрузить прогресс чеклиста', e)
  }
}

watch(isCompleted, (newValue) => {
  if (newValue) {
    confetti({
      particleCount: 150,
      spread: 70,
      origin: { y: 0.6 },
      colors: ['#48bb78', '#2d3748', '#ffffff']
    })
  }
})

onMounted(() => {
  loadProgress()
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        isVisible.value = true
        observer.unobserve(entry.target)
      }
    })
  }, { threshold: 0.1 })
  
  if (checklistCardRef.value) {
    observer.observe(checklistCardRef.value)
  }
  
  // Observe title as well, though it's static
  const title = document.querySelector('.checklist-section .section-title')
  if (title) {
    const titleObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible')
          titleObserver.unobserve(entry.target)
        }
      })
    })
    titleObserver.observe(title)
  }
})
</script>

<style scoped>
.checklist-card {
  transition: all 0.5s ease;
}

/* Removed .checklist-card.completed styles from here */

.checklist-result {
  /* Ensure basic styling is present here or inherited */
  transition: all 0.3s ease;
  border-radius: 8px; /* Optional: adds rounded corners if background is applied */
  padding: 10px; /* Add some padding so the background doesn't hug text too tightly */
}

.checklist-result.completed {
  background: linear-gradient(135deg, #c6f6d5, #9ae6b4);
  border: 2px solid var(--accent-green);
  box-shadow: 0 0 15px rgba(72, 187, 120, 0.3);
  color: #1a202c; /* Ensure text is dark enough on green */
  font-weight: bold;
}

.completion-icon {
  font-size: 1.5rem;
  margin-left: 10px;
  display: inline-block;
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-5px); }
}
</style>
