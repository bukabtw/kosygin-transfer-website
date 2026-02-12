<template>
  <section class="reviews-section section-animate" id="reviews" ref="sectionRef">
    <div class="reviews-container">
      <h2 class="section-title">Студенты, которые уже перевелись</h2>

      <!-- Фильтры -->
      <div class="reviews-filter" role="toolbar" aria-label="Фильтры отзывов">
        <button 
          v-for="filter in filters" 
          :key="filter.value"
          class="filter-tag"
          :class="{ active: currentFilter === filter.value }"
          :aria-pressed="currentFilter === filter.value"
          @click="setFilter(filter.value)"
        >
          {{ filter.label }}
        </button>
      </div>

      <!-- Список отзывов -->
      <div class="reviews-slider">
        <div 
          v-for="(review, index) in filteredReviews" 
          :key="review.id"
          class="review-card"
          :class="{ highlighted: index === 0 && currentFilter === 'all' }"
        >
          <div class="review-header">
            <div class="review-avatar">
              <img :src="review.avatar" :alt="review.name" loading="lazy">
            </div>
            <div class="review-author">
              <h3>{{ review.name }}</h3>
              <p class="review-meta-info">{{ review.meta }}</p>
              <div class="review-rating" aria-label="5 звезд">★★★★★</div>
            </div>
          </div>
          
          <div class="review-content">
            <p>"{{ review.text }}"</p>
          </div>
          
          <div class="review-tags">
            <span 
              v-for="tag in review.tags" 
              :key="tag.type"
              class="tag" 
              :data-tag="tag.type"
              @click="setFilter(tag.type)"
            >
              {{ tag.label }}
            </span>
          </div>
        </div>
      </div>

      <!-- Статистика -->
      <div class="reviews-stats">
        <div class="stat-item">
          <div class="stat-number">94%</div>
          <div class="stat-label">Довольных переводом</div>
        </div>
        <div class="stat-item">
          <div class="stat-number">2-3 недели</div>
          <div class="stat-label">Средний срок перевода</div>
        </div>
        <div class="stat-item">
          <div class="stat-number">100+</div>
          <div class="stat-label">Студентов перевелось в 2024</div>
        </div>
      </div>

      <div class="add-review">
        <button class="add-review-button" @click="showModal = true">
          ✍️ Рассказать свою историю перевода
        </button>
        <p class="add-review-note">Ваш отзыв поможет другим студентам принять правильное решение!</p>
      </div>
    </div>

    <!-- Модальное окно -->
    <Teleport to="body">
      <div v-if="showModal" class="review-modal-overlay" role="dialog" aria-modal="true" @click.self="showModal = false">
        <div class="review-modal">
          <button class="modal-close" aria-label="Закрыть форму" @click="showModal = false">&times;</button>
          <h3>Расскажите о своем опыте перевода</h3>
          <p style="color: #718096; margin-bottom: 30px;">Ваш отзыв поможет другим студентам принять правильное решение</p>
          
          <form @submit.prevent="submitReview" class="review-form">
            <div class="form-group">
              <label style="display: block; margin-bottom: 5px; font-weight: 500;">Имя (можно только имя)</label>
              <input type="text" v-model="form.name" placeholder="Ваше имя" required>
            </div>
            
            <div class="form-group">
              <label style="display: block; margin-bottom: 5px; font-weight: 500;">Email (не публикуется)</label>
              <input type="email" v-model="form.email" placeholder="Email" required>
            </div>
            
            <div class="form-group">
              <label style="display: block; margin-bottom: 5px; font-weight: 500;">Отзыв</label>
              <textarea v-model="form.text" placeholder="Ваш отзыв о переводе..." rows="5" required></textarea>
            </div>
            
            <div class="form-group">
              <label style="display: block; margin-bottom: 8px; font-weight: 500;">Специальность:</label>
              <select v-model="form.specialty">
                <option value="">Выберите направление</option>
                <option value="data-science">Data Science</option>
                <option value="web-dev">Веб-разработка</option>
                <option value="cyber">Кибербезопасность</option>
                <option value="ux-ui">UX/UI дизайн</option>
                <option value="mobile">Мобильная разработка</option>
                <option value="other">Другое</option>
              </select>
            </div>
            
            <div class="form-group">
              <label style="display: block; margin-bottom: 8px; font-weight: 500;">Оценка:</label>
              <div class="rating-stars">
                <span 
                  v-for="star in 5" 
                  :key="star"
                  class="star" 
                  :class="{ active: star <= form.rating }"
                  @click="form.rating = star"
                  style="cursor: pointer; font-size: 1.5rem; color: #cbd5e0;"
                >★</span>
              </div>
            </div>
            
            <button type="submit" class="submit-button" :disabled="isSubmitting">
              {{ isSubmitting ? 'Отправка...' : 'Отправить отзыв' }}
            </button>
          </form>
        </div>
      </div>
    </Teleport>
  </section>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const sectionRef = ref(null)
const showModal = ref(false)
const currentFilter = ref('all')
const isSubmitting = ref(false)

const filters = [
  { label: 'Все отзывы', value: 'all' },
  { label: 'Учеба', value: 'academic' },
  { label: 'Карьера', value: 'career' },
  { label: 'Атмосфера', value: 'community' },
  { label: 'Перевод', value: 'transition' }
]

const form = ref({
  name: '',
  email: '',
  text: '',
  specialty: '',
  rating: 0
})

const reviews = [
  {
    id: 1,
    name: 'Дмитрий В.',
    avatar: '/addons/dmitrii.jpg',
    meta: 'Перевелся с вечернего на очное • Кибербезопасность • 2024',
    text: 'Ценил в старом вузе определенные места для перекура между парами. Здесь нашел крутые open-space зоны с диванами - идеально для общения и отдыха. И Wi-Fi везде ловит!',
    tags: [
      { type: 'campus', label: '🛋️ Open-space зоны' },
      { type: 'community', label: '💬 Студенческое комьюнити' },
      { type: 'facilities', label: '📶 Wi-Fi на всей территории' },
      { type: 'transition', label: '🔄 Смена формы обучения' }
    ]
  },
  {
    id: 2,
    name: 'Анна К.',
    avatar: '/addons/anna.jpg',
    meta: 'Перевелась с экономики • Data Science • 2024',
    text: 'Боялась большой академической разницы, но в деканате ИТ помогли составить индивидуальный план. Закрыла разницу за семестр, теперь работаю аналитиком в стартапе!',
    tags: [
      { type: 'academic', label: '📚 Академическая разница' },
      { type: 'career', label: '💼 Карьерный рост' },
      { type: 'support', label: '🤝 Поддержка деканата' }
    ]
  },
  {
    id: 3,
    name: 'Евгения М.',
    avatar: '/addons/evgenia.jpg',
    meta: 'Перевелась из другого вуза Москвы • UX/UI дизайн • 2024',
    text: 'Искала вуз с сильной IT-школой и современным подходом. В ИТ-институте РГУ Косыгина - идеальный баланс теории и практики. Преподаватели сами работают в IT-компаниях и дают актуальные знания!',
    tags: [
      { type: 'practice', label: '🎯 Практические навыки' },
      { type: 'teachers', label: '👨‍🏫 Преподаватели-практики' },
      { type: 'it', label: '💻 IT-образование' },
      { type: 'relevance', label: '🚀 Актуальные знания' },
      { type: 'academic', label: '📚 Учеба' }
    ]
  },
  {
    id: 4,
    name: 'Максим П.',
    avatar: '/addons/maksim.jpg',
    meta: 'Перевелся из регионального вуза • Мобильная разработка • 2024',
    text: 'Процесс перевода оказался намного проще, чем я думал. Отправил документы онлайн, получил справку о зачислении и приехал уже на учебу. Общежитие дали сразу!',
    tags: [
      { type: 'transition', label: '⚡ Быстрый перевод' },
      { type: 'housing', label: '🏢 Общежитие' },
      { type: 'remote', label: '🌐 Онлайн-подача' },
      { type: 'community', label: '💬 Атмосфера' }
    ]
  }
]

const filteredReviews = computed(() => {
  if (currentFilter.value === 'all') {
    return reviews
  }
  return reviews.filter(review => {
    return review.tags.some(tag => {
      // Direct match
      if (tag.type === currentFilter.value) return true;
      // Category mapping
      if (currentFilter.value === 'academic' && ['academic', 'practice', 'teachers', 'relevance', 'it'].includes(tag.type)) return true;
      if (currentFilter.value === 'career' && ['career', 'practice'].includes(tag.type)) return true;
      if (currentFilter.value === 'community' && ['community', 'campus', 'facilities', 'housing'].includes(tag.type)) return true;
      if (currentFilter.value === 'transition' && ['transition', 'support', 'remote'].includes(tag.type)) return true;
      return false;
    })
  })
})

const setFilter = (filter) => {
  currentFilter.value = filter
}

const submitReview = async () => {
  if (isSubmitting.value) return
  isSubmitting.value = true
  
  // Simulate API call
  await new Promise(resolve => setTimeout(resolve, 1500))
  
  alert('Спасибо за ваш отзыв! Он будет опубликован после модерации.')
  showModal.value = false
  isSubmitting.value = false
  form.value = {
    name: '',
    email: '',
    text: '',
    specialty: '',
    rating: 0
  }
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
</script>    meta: 'Перевелся из регионального вуза • Веб-разработка • 2023',
    text: 'В РГУ Косыгина невероятная атмосфера! После пар все собираемся в зоне отдыха (есть где и кофе попить, и поработать в группе). Москва - это новые возможности!',
    tags: [
      { type: 'campus', label: '🏛️ Кампус' },
      { type: 'community', label: '👥 Сообщество' },
      { type: 'location', label: '📍 Локация' },
      { type: 'facilities', label: '🛋️ Зоны отдыха' }
    ]
  }
]

// Extract unique tags for filter buttons
const filters = computed(() => {
  const unique = new Set()
  const result = [{ value: 'all', label: '👁️ Все отзывы' }]
  
  reviews.forEach(review => {
    review.tags.forEach(tag => {
      if (!unique.has(tag.type)) {
        unique.add(tag.type)
        // Clean up label for button (remove emoji if needed, but keeping it for now as per original)
        // Original JS code: tag.textContent.replace(/[^a-zA-Zа-яА-ЯёЁ\s]/g, '').trim()
        // But here I'll just use the label directly or a simplified version
        // Let's use the label from the tag but maybe shorten it if it's too long?
        // Actually the original code extracted text from the tag element.
        // Let's just use the full label for now.
        result.push({ value: tag.type, label: tag.label })
      }
    })
  })
  return result
})

const filteredReviews = computed(() => {
  if (currentFilter.value === 'all') return reviews
  return reviews.filter(review => 
    review.tags.some(tag => tag.type === currentFilter.value)
  )
})

const setFilter = (filter) => {
  currentFilter.value = filter
}

const submitReview = async () => {
  isSubmitting.value = true
  // Simulate API call
  await new Promise(resolve => setTimeout(resolve, 1500))
  
  alert('Спасибо за ваш отзыв! Он будет опубликован после проверки модератором.')
  showModal.value = false
  form.value = { name: '', email: '', text: '', specialty: '', rating: 0 }
  isSubmitting.value = false
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

<style scoped>
.reviews-section {
  padding: 100px 0;
  background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
  position: relative;
  overflow: hidden;
}

.reviews-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  position: relative;
  z-index: 1;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 60px;
  color: var(--text-color);
  font-weight: 800;
  position: relative;
  display: inline-block;
  left: 50%;
  transform: translateX(-50%);
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: -15px;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 4px;
  background: var(--primary-color);
  border-radius: 2px;
}

/* Filters */
.reviews-filter {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 40px;
}

.filter-tag {
  background: white;
  border: 1px solid #e2e8f0;
  padding: 8px 16px;
  border-radius: 50px;
  font-size: 0.9rem;
  color: var(--text-color);
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: inherit;
}

.filter-tag:hover {
  border-color: var(--primary-color);
  color: var(--primary-color);
}

.filter-tag.active {
  background: var(--primary-color);
  color: white;
  border-color: var(--primary-color);
  box-shadow: 0 4px 12px rgba(66, 153, 225, 0.3);
}

/* Reviews Grid/Slider */
.reviews-slider {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  margin-bottom: 60px;
}

.review-card {
  background: white;
  border-radius: var(--radius-lg);
  padding: 30px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  transition: var(--transition);
  border: 1px solid rgba(0, 0, 0, 0.03);
  display: flex;
  flex-direction: column;
}

.review-card.highlighted {
  background: #f8fafc;
  border: 2px solid var(--accent-blue);
  box-shadow: 0 15px 40px rgba(66, 153, 225, 0.15);
  transform: scale(1.02);
}

.review-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
}

.review-header {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 20px;
}

.review-avatar {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  overflow: hidden;
  border: 3px solid #fff;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  flex-shrink: 0;
}

.review-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.review-author h3 {
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 2px;
  color: var(--text-color);
}

.review-meta-info {
  font-size: 0.8rem;
  color: #718096;
  margin-bottom: 5px;
}

.review-rating {
  color: #ecc94b;
  font-size: 1rem;
  letter-spacing: 2px;
}

.review-content {
  margin-bottom: 20px;
  flex-grow: 1;
}

.review-content p {
  color: var(--text-color);
  line-height: 1.6;
  font-style: italic;
  font-size: 0.95rem;
}

.review-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  background: #edf2f7;
  color: var(--text-color);
  padding: 6px 12px;
  border-radius: 50px;
  font-size: 0.75rem;
  font-weight: 500;
  border: 1px solid #e2e8f0;
  transition: var(--transition);
  cursor: pointer;
}

.tag:hover {
  background: #e2e8f0;
  transform: translateY(-2px);
}

/* Stats */
.reviews-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
  background: white;
  padding: 40px;
  border-radius: var(--radius-lg);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.05);
  margin-bottom: 40px;
  text-align: center;
}

.stat-item {
  position: relative;
}

.stat-item:not(:last-child)::after {
  content: '';
  position: absolute;
  right: -15px;
  top: 50%;
  transform: translateY(-50%);
  height: 60%;
  width: 1px;
  background: #e2e8f0;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 800;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 10px;
  line-height: 1;
}

.stat-label {
  color: #718096;
  font-weight: 500;
  font-size: 0.9rem;
}

/* Add Review Section */
.add-review {
  text-align: center;
  margin-top: 40px;
}

.add-review-button {
  background: transparent;
  border: 2px dashed #cbd5e0;
  color: #718096;
  padding: 15px 30px;
  border-radius: var(--radius-md);
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: inline-flex;
  align-items: center;
  gap: 10px;
}

.add-review-button:hover {
  border-color: var(--primary-color);
  color: var(--primary-color);
  background: rgba(66, 153, 225, 0.05);
}

.add-review-note {
  margin-top: 15px;
  font-size: 0.9rem;
  color: #a0aec0;
}

/* Modal */
.review-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(5px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  animation: fadeIn 0.3s ease;
}

.review-modal {
  background: white;
  width: 100%;
  max-width: 500px;
  padding: 40px;
  border-radius: var(--radius-lg);
  position: relative;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.25);
  animation: slideInUp 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  max-height: 90vh;
  overflow-y: auto;
}

.modal-close {
  position: absolute;
  top: 20px;
  right: 20px;
  background: none;
  border: none;
  font-size: 1.5rem;
  color: #a0aec0;
  cursor: pointer;
  transition: color 0.2s;
}

.modal-close:hover {
  color: var(--text-color);
}

.review-modal h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
  color: var(--text-color);
}

.form-group {
  margin-bottom: 20px;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 12px 15px;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.3s ease;
  font-family: inherit;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  border-color: var(--primary-color);
  outline: none;
  box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.15);
}

.star.active {
  color: #ecc94b !important;
}

.submit-button {
  width: 100%;
  background: var(--primary-color);
  color: white;
  border: none;
  padding: 15px;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.submit-button:hover {
  background: var(--secondary-color);
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(66, 153, 225, 0.4);
}

.submit-button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 768px) {
  .section-title {
    font-size: 2rem;
  }
  
  .reviews-stats {
    grid-template-columns: 1fr;
    gap: 20px;
    padding: 30px;
  }
  
  .stat-item:not(:last-child)::after {
    display: none;
  }
  
  .stat-item {
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 20px;
  }
  
  .stat-item:last-child {
    border-bottom: none;
    padding-bottom: 0;
  }
}
</style>
