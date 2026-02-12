<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const days = ref('00')
const hours = ref('00')
const minutes = ref('00')
const seconds = ref('00')
const isExpired = ref(false)
const timerColor = ref('')
const timerTitle = ref('')

const deadline = new Date('February 10, 2026 23:59:59').getTime()
let timerInterval = null

const updateTimer = () => {
  const now = new Date().getTime()
  const timeLeft = deadline - now

  if (timeLeft < 0) {
    isExpired.value = true
    if (timerInterval) clearInterval(timerInterval)
    return
  }

  const d = Math.floor(timeLeft / (1000 * 60 * 60 * 24))
  const h = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
  const m = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60))
  const s = Math.floor((timeLeft % (1000 * 60)) / 1000)

  days.value = d.toString().padStart(2, '0')
  hours.value = h.toString().padStart(2, '0')
  minutes.value = m.toString().padStart(2, '0')
  seconds.value = s.toString().padStart(2, '0')

  if (d < 7) {
    timerColor.value = '#e53e3e'
  } else if (d < 30) {
    timerColor.value = '#dd6b20'
  } else {
    timerColor.value = ''
  }

  timerTitle.value = `Осталось: ${d} дней, ${h} часов, ${m} минут, ${s} секунд`
}

onMounted(() => {
  updateTimer()
  timerInterval = setInterval(updateTimer, 1000)
  
  // Intersection Observer for animation
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible')
        observer.unobserve(entry.target)
      }
    })
  }, { threshold: 0.1, rootMargin: '50px' })

  const section = document.querySelector('.deadline-section')
  if (section) {
    section.classList.add('section-animate')
    observer.observe(section)
  }
  
  const card = document.querySelector('.deadline-card')
  if (card) {
    card.classList.add('animate-in')
    observer.observe(card)
  }
})

onUnmounted(() => {
  if (timerInterval) clearInterval(timerInterval)
})
</script>

<template>
  <section id="deadline" class="deadline-section">
    <div class="deadline-container">
      <div class="deadline-card">
        <div class="deadline-icon">⏰</div>
        <h2>До конца приёма документов на перевод</h2>
        
        <div v-if="isExpired" class="deadline-expired">
          Приём документов завершён
        </div>
        
        <div v-else class="countdown-timer" id="countdownTimer" :title="timerTitle">
          <div class="time-unit">
            <span class="time-number" :style="{ color: timerColor }">{{ days }}</span>
            <span class="time-label">дней</span>
          </div>
          <div class="time-separator" :style="{ color: timerColor }">:</div>
          <div class="time-unit">
            <span class="time-number" :style="{ color: timerColor }">{{ hours }}</span>
            <span class="time-label">часов</span>
          </div>
          <div class="time-separator" :style="{ color: timerColor }">:</div>
          <div class="time-unit">
            <span class="time-number" :style="{ color: timerColor }">{{ minutes }}</span>
            <span class="time-label">минут</span>
          </div>
          <div class="time-separator" :style="{ color: timerColor }">:</div>
          <div class="time-unit">
            <span class="time-number" :style="{ color: timerColor }">{{ seconds }}</span>
            <span class="time-label">секунд</span>
          </div>
        </div>
        
        <p class="deadline-note">Успей подать документы до окончания срока!</p>
        <a href="#materials" class="deadline-button">Скачать документы</a>
      </div>
    </div>
  </section>
</template>

<style scoped>
/* Scoped styles removed to rely on global style.css */
</style>
