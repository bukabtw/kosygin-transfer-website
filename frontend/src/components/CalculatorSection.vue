<script setup>
import { ref, computed, onMounted } from 'vue'

const disciplineCount = ref(0)
const creditUnits = ref(0)
const budgetType = ref('contract') // Default to contract

const weights = {
  disciplineLimit: 0.4,
  creditLimit: 0.3,
  budgetType: 0.2,
  otherFactors: 0.1
}

// Helpers for custom input buttons
const increment = (field, max) => {
  if (field === 'discipline') {
    if (disciplineCount.value < max) disciplineCount.value++
  } else if (field === 'credit') {
    if (creditUnits.value < max) creditUnits.value++
  }
}

const decrement = (field, min) => {
  if (field === 'discipline') {
    if (disciplineCount.value > min) disciplineCount.value--
  } else if (field === 'credit') {
    if (creditUnits.value > min) creditUnits.value--
  }
}

const calculationResult = computed(() => {
  const disciplineScore = Math.max(0, 100 - (Math.max(0, disciplineCount.value - 6) * 10))
  const creditScore = Math.max(0, 100 - (Math.max(0, creditUnits.value - 20) * 5))
  const budgetScore = budgetType.value === 'budget' ? 70 : 100
  
  let chancePercentage = (
    disciplineScore * weights.disciplineLimit +
    creditScore * weights.creditLimit +
    budgetScore * weights.budgetType +
    100 * weights.otherFactors
  )
  
  const criticalMessages = []
  // Adjusted thresholds to match new input limits, though max inputs prevent reaching these extreme values via UI
  if (disciplineCount.value > 8) {
    chancePercentage *= 0.5
    criticalMessages.push("❌ Критическое количество дисциплин")
  }
  if (creditUnits.value > 30) {
    chancePercentage *= 0.6
    criticalMessages.push("❌ Критическое количество зачетных единиц")
  }
  
  // Special case: Perfect match
  if (disciplineCount.value <= 4 && creditUnits.value <= 15 && budgetType.value === 'contract') {
    chancePercentage = 100
  }
  
  chancePercentage = Math.max(0, Math.min(100, chancePercentage))
  
  return {
    percentage: Math.round(chancePercentage),
    disciplineScore,
    creditScore,
    budgetScore,
    criticalMessages
  }
})

const chance = computed(() => calculationResult.value.percentage)

const recommendations = computed(() => {
  const recs = []
  
  if (disciplineCount.value > 6) {
    recs.push('• Рассмотрите возможность сокращения количества дисциплин')
  }
  
  if (creditUnits.value > 25) {
    recs.push('• Попробуйте перезачесть некоторые дисциплины')
  }
  
  if (budgetType.value === 'budget' && disciplineCount.value > 5) {
    recs.push('• Рассмотрите контрактную форму обучения')
  }

  if (disciplineCount.value <= 4 && creditUnits.value <= 15) {
    recs.push('• У вас идеальные условия для перевода!')
  }
  
  return recs
})

const resultDetails = computed(() => {
  const p = chance.value
  let className = 'low'
  let icon = '💡'
  let title = 'Очень низкие шансы'

  if (p >= 70) {
    className = 'high' // Green
    icon = '🚀'
    title = p >= 90 ? 'Отличные шансы!' : 'Хорошие шансы'
  } else if (p >= 40) {
    className = 'medium' // Yellow
    icon = '📊'
    title = 'Средние шансы'
  } else {
    className = 'low' // Red
    icon = '💡'
    title = p >= 30 ? 'Низкие шансы' : 'Очень низкие шансы'
  }

  return { 
    icon, 
    title, 
    className,
    disciplineScore: calculationResult.value.disciplineScore,
    creditScore: calculationResult.value.creditScore,
    budgetScore: calculationResult.value.budgetScore,
    criticalMessages: calculationResult.value.criticalMessages
  }
})

onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible')
      }
    })
  }, { threshold: 0.1 })

  const card = document.querySelector('.calculator-card')
  if (card) observer.observe(card)
})
</script>

<template>
  <section id="calculator" class="calculator-section">
    <div class="calculator-container">
      <h2 class="section-title">Калькулятор шансов</h2>
      <p class="section-subtitle">Оцените свои шансы на успешный перевод, учитывая академическую разницу и другие факторы</p>
      
      <div class="calculator-card">
        <div class="calculator-form">
          <div class="calc-input-group">
            <label>Количество дисциплин (разница)</label>
            <div class="number-input-wrapper">
              <button class="num-btn" @click="decrement('discipline', 0)">-</button>
              <input 
                type="number" 
                v-model.number="disciplineCount" 
                min="0" 
                max="8"
                placeholder="5"
              >
              <button class="num-btn" @click="increment('discipline', 8)">+</button>
            </div>
            <div class="calc-hint">Максимум: 8 дисциплин</div>
          </div>

          <div class="calc-input-group">
            <label>Зачетные единицы (разница)</label>
            <div class="number-input-wrapper">
              <button class="num-btn" @click="decrement('credit', 0)">-</button>
              <input 
                type="number" 
                v-model.number="creditUnits" 
                min="0" 
                max="30"
                placeholder="15"
              >
              <button class="num-btn" @click="increment('credit', 30)">+</button>
            </div>
            <div class="calc-hint">Максимум: 30 зачетных единиц</div>
          </div>

          <div class="calc-input-group">
            <label>Тип обучения</label>
            <div class="select-wrapper">
                <select v-model="budgetType">
                <option value="contract">Контракт</option>
                <option value="budget">Бюджет</option>
                </select>
            </div>
          </div>

          <!-- Extras moved here -->
          <div class="calculator-extras">
            <div class="result-details-box">
              <h4 class="details-title">Детали расчета:</h4>
              <ul class="details-list">
                <li>• Дисциплины: {{ resultDetails.disciplineScore }}%</li>
                <li>• Зачетные единицы: {{ resultDetails.creditScore }}%</li>
                <li>• Тип финансирования: {{ resultDetails.budgetScore }}%</li>
              </ul>
            </div>

            <div v-if="resultDetails.criticalMessages.length > 0" class="result-attention-box">
               <h4 class="attention-title">Внимание:</h4>
               <ul class="attention-list">
                  <li v-for="msg in resultDetails.criticalMessages" :key="msg">
                    {{ msg }}
                  </li>
               </ul>
            </div>

            <div class="result-recommendations">
              <h4 class="recs-title">Рекомендации:</h4>
              <ul class="recs-list">
                <li v-for="(rec, index) in recommendations" :key="index">
                  {{ rec }}
                </li>
                <li v-if="recommendations.length === 0">
                  Заполните данные для получения рекомендаций
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="calculator-result" :class="resultDetails.className">
          <div class="result-main-content">
            <div class="result-icon-top">{{ resultDetails.icon }}</div>
            <div class="result-percentage">{{ chance }}%</div>
            <h3 class="result-title">{{ resultDetails.title }}</h3>
          </div>
          
          <div class="result-disclaimer">
            * Расчет основан на статистике прошлых лет. Для точной оценки обратитесь в деканат.
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
/* Inputs styling */
.number-input-wrapper {
  display: flex;
  align-items: center;
  border: 2px solid #e2e8f0;
  border-radius: 12px;
  background: #fff;
  overflow: hidden;
  transition: all 0.2s ease;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  margin-bottom: 8px; /* Added margin for better spacing */
}

.number-input-wrapper:focus-within {
  border-color: var(--primary-color, #667eea);
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.number-input-wrapper input {
  flex: 1;
  border: none;
  text-align: center;
  margin: 0;
  border-radius: 0;
  -moz-appearance: textfield;
  font-size: 1.1rem;
  font-weight: 600;
  color: #2d3748;
  padding: 12px 0;
}

.number-input-wrapper input:focus {
  outline: none;
}

.number-input-wrapper input::-webkit-outer-spin-button,
.number-input-wrapper input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.num-btn {
  width: 45px;
  background: transparent;
  border: none;
  font-size: 1.5rem;
  font-weight: 400;
  color: #718096;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.num-btn:hover {
  background: #f7fafc;
  color: var(--primary-color, #667eea);
}

.select-wrapper {
  position: relative;
  margin-bottom: 8px; /* Added margin */
}

.select-wrapper select {
  width: 100%;
  appearance: none;
  -webkit-appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%232d3748' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 15px center;
  background-size: 18px;
  padding: 12px 45px 12px 15px;
  border: 2px solid #e2e8f0;
  border-radius: 12px;
  background-color: #fff;
  font-size: 1rem;
  color: #2d3748;
  font-weight: 500;
  transition: all 0.2s;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  cursor: pointer;
}

.select-wrapper select:focus {
  outline: none;
  border-color: var(--primary-color, #667eea);
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.calc-input-group {
  margin-bottom: 20px; /* Increased spacing between groups */
}

.calc-input-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: #4a5568;
}

.calc-hint {
  font-size: 0.8rem;
  color: #718096;
  margin-top: 4px;
}

/* Extras styling */
.calculator-extras {
  margin-top: 30px;
  padding-top: 25px;
  border-top: 2px dashed #e2e8f0; /* More distinct separator */
}

/* Result Card styling */
.calculator-card {
  display: flex;
  gap: 30px; /* Space between columns */
  align-items: flex-start; /* Fixes "unjustifiably high" issue */
}

.calculator-form {
  flex: 1;
  background: #ffffff;
  padding: 30px;
  border-radius: 16px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

.calculator-result {
  flex: 0 0 320px; /* Fixed width for result card to prevent squishing */
  padding: 30px;
  border-radius: 16px; /* Match form radius */
  text-align: center;
  color: #2d3748; 
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  /* height: auto; - implicitly handled by flex-start */
  position: sticky;
  top: 20px; /* Sticky behavior if form is long */
}

.result-main-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.calculator-result.high {
  background: linear-gradient(135deg, #bbf0d0 0%, #9ae6b4 100%);
  box-shadow: 0 10px 15px -3px rgba(72, 187, 120, 0.3);
}

.calculator-result.medium {
  background: linear-gradient(135deg, #fefcbf 0%, #faf089 100%);
  box-shadow: 0 10px 15px -3px rgba(236, 201, 75, 0.3);
}

.calculator-result.low {
  background: linear-gradient(135deg, #fed7d7 0%, #feb2b2 100%);
  box-shadow: 0 10px 15px -3px rgba(245, 101, 101, 0.3);
}

.result-icon-top {
  font-size: 4rem; 
  margin-bottom: 15px;
  animation: bounce 2s infinite;
}

.result-percentage {
  font-size: 4.5rem; /* Slightly bigger */
  font-weight: 800;
  line-height: 1;
  margin-bottom: 10px;
  color: #1a202c; 
}

.result-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0;
  color: #2d3748;
}

/* Adjusted styles for extras in left column */
.result-details-box, .result-attention-box {
  background: #f8fafc; /* Slightly cooler gray */
  border-radius: 12px;
  padding: 20px;
  width: 100%;
  margin-bottom: 20px;
  border: 1px solid #e2e8f0; /* Stronger border for contrast */
  box-shadow: 0 1px 2px rgba(0,0,0,0.05); /* Subtle shadow */
}

.result-attention-box {
  background: #fff5f5;
  border-color: #fc8181;
  color: #c53030;
  box-shadow: 0 1px 3px rgba(229, 62, 62, 0.1);
}

.details-title, .attention-title, .recs-title {
  margin: 0 0 12px 0;
  font-size: 1rem;
  font-weight: 700;
  color: #2d3748;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.attention-title {
  color: #c53030;
}

.details-list, .attention-list, .recs-list {
  list-style: none;
  padding: 0;
  margin: 0;
  text-align: left;
}

.details-list li, .attention-list li, .recs-list li {
  margin-bottom: 8px;
  font-size: 0.95rem;
  color: #4a5568;
  display: flex;
  align-items: center;
}

.attention-list li {
  color: #742a2a;
  font-weight: 500;
}

.result-recommendations {
  width: 100%;
  padding: 10px 0;
}

.result-disclaimer {
  font-size: 0.75rem;
  opacity: 0.7;
  font-style: italic;
  margin-top: 20px;
  line-height: 1.4;
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

/* Media query for mobile responsiveness */
@media (max-width: 768px) {
  .calculator-card {
    flex-direction: column;
    align-items: stretch;
  }
  
  .calculator-result {
    flex: auto;
    width: 100%;
    position: static;
  }
}
</style>
