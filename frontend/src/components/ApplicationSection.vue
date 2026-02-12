<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const form = ref({
  name: '',
  phone: '',
  email: '',
  faculty: '',
  message: '',
  agreement: false
})

const isSubmitting = ref(false)

const submitForm = async () => {
  if (!form.value.agreement) {
    alert('Пожалуйста, подтвердите согласие на обработку персональных данных')
    return
  }

  isSubmitting.value = true
  
  try {
    const { agreement, ...payload } = form.value
    const response = await axios.post('/api/consultations/', payload)
    if (response.status === 200 || response.status === 201) {
      alert('Заявка успешно отправлена! Наш специалист свяжется с вами в ближайшее время.')
      // Reset form
      form.value = {
        name: '',
        phone: '',
        email: '',
        faculty: '',
        message: '',
        agreement: false
      }
    }
  } catch (error) {
    console.error('Error submitting form:', error)
    alert('Произошла ошибка при отправке заявки. Пожалуйста, попробуйте позже или свяжитесь с нами по телефону.')
  } finally {
    isSubmitting.value = false
  }
}

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
  <section id="application" class="application-section">
    <div class="application-container">
      <div class="application-content section-animate">
        <h2 class="section-title">Оставьте заявку на консультацию по переводу</h2>
        <p class="application-subtitle">Наш специалист свяжется с вами в течение 2 часов для бесплатной консультации</p>
        
        <div class="application-features">
          <div class="feature">
            <div class="feature-icon">✅</div>
            <p>Проверим академическую разницу бесплатно</p>
          </div>
          <div class="feature">
            <div class="feature-icon">✅</div>
            <p>Подскажем какие документы нужны именно вам</p>
          </div>
          <div class="feature">
            <div class="feature-icon">✅</div>
            <p>Забронируем место на выбранной специальности</p>
          </div>
        </div>
        
        <form class="application-form" @submit.prevent="submitForm">
          <div class="form-row">
            <div class="form-group">
              <input 
                v-model="form.name" 
                type="text" 
                placeholder="Ваше ФИО" 
                required
              >
            </div>
            <div class="form-group">
              <input 
                v-model="form.phone" 
                type="tel" 
                placeholder="Телефон" 
                required
              >
            </div>
          </div>
          
          <div class="form-row">
            <div class="form-group">
              <input 
                v-model="form.email" 
                type="email" 
                placeholder="Email"
              >
            </div>
            <div class="form-group">
              <select v-model="form.faculty" required>
                <option value="">Интересующий факультет</option>
                <option value="it">Институт информационных технологий</option>
                <option value="design">Дизайн и мода</option>
                <option value="economics">Экономика и менеджмент</option>
              </select>
            </div>
          </div>
          
          <div class="form-group">
            <textarea 
              v-model="form.message" 
              placeholder="Откуда переводитесь и какие вопросы есть?" 
              rows="3"
            ></textarea>
          </div>
          
          <div class="form-agreement">
            <input 
              v-model="form.agreement" 
              type="checkbox" 
              id="agreement" 
              required
            >
            <label for="agreement">Согласен на обработку персональных данных</label>
          </div>
          
          <button type="submit" class="submit-button" :disabled="isSubmitting">
            {{ isSubmitting ? 'Отправка...' : 'Оставить заявку' }}
          </button>
          
          <p class="form-note">Или напишите нам напрямую: <a href="mailto:itct@rguk.ru">itct@rguk.ru</a></p>
        </form>
      </div>
    </div>
  </section>
</template>
