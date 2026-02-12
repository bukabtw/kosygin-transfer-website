<script setup>
import { ref, onMounted } from 'vue'

const faqItems = [
  {
    question: 'Можно ли перевестись на бюджет?',
    answer: 'Да, перевод на бюджетные места возможен при наличии вакантных мест. Количество мест ограничено, поэтому рекомендуем уточнять актуальную информацию в деканате.'
  },
  {
    question: 'Что делать, если академическая разница больше 8 дисциплин?',
    answer: 'Если разница превышает 8 дисциплин или 30 зачетных единиц, в переводе могут отказать, но возможно оценить шансы на другом направлении или другой форме обучения. Рекомендуем заранее оценить разницу и проконсультироваться с деканатом.'
  },
  {
    question: 'Нужно ли сдавать ЕГЭ заново при переводе?',
    answer: 'Нет, при переводе ЕГЭ не требуется.'
  },
  {
    question: 'Как долго рассматривается заявление о переводе?',
    answer: 'Обычно рассмотрение занимает от 10 до 14 рабочих дней. В периоды высокой нагрузки срок может увеличиться.'
  },
  {
    question: 'Можно ли перевестись с заочной на очную форму?',
    answer: 'Да, перевод между формами обучения возможен. Однако учитывайте, что может возникнуть дополнительная академическая разница.'
  },
  {
    question: 'Что такое справка текущего месяца и почему она важна?',
    answer: 'Справка должна быть датирована текущим месяцем подачи документов. Это подтверждает ваш текущий статус студента и актуальность информации.'
  },
  {
    question: 'Можно ли перевестись в середине семестра?',
    answer: 'Да, перевод возможен в течение всего учебного года, но рекомендуем делать это во время каникул или до начала сессии.'
  },
  {
    question: 'Какие документы нужны от негосударственного вуза?',
    answer: 'От негосударственных вузов требуются заверенные копии лицензии и свидетельства о государственной аккредитации.'
  }
]

const activeIndex = ref(null)
const itemRefs = ref([])
const visibilityStates = ref([])

const toggleItem = (index) => {
  if (activeIndex.value === index) {
    activeIndex.value = null
  } else {
    activeIndex.value = index
  }
}

onMounted(() => {
  // Initialize visibility states
  visibilityStates.value = new Array(faqItems.length).fill(false)

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // Find index from data attribute
        const index = parseInt(entry.target.dataset.index)
        if (!isNaN(index)) {
          visibilityStates.value[index] = true
          observer.unobserve(entry.target)
        }
      }
    })
  }, { threshold: 0.1 })

  itemRefs.value.forEach((el, index) => {
    if (el) {
      el.dataset.index = index
      observer.observe(el)
    }
  })
  
  // Also observe title
  const title = document.querySelector('.faq-section .section-title')
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

<template>
  <section id="faq" class="faq-section">
    <h2 class="section-title section-animate">Частые вопросы</h2>
    <div class="faq-container">
      <div 
        v-for="(item, index) in faqItems" 
        :key="index"
        :ref="el => itemRefs[index] = el"
        class="faq-item section-animate"
        :class="{ active: activeIndex === index, visible: visibilityStates[index] }"
        @click="toggleItem(index)"
        :style="{ transitionDelay: `${index * 0.1}s` }"
      >
        <div class="faq-question">
          <span>{{ item.question }}</span>
          <div class="faq-icon">+</div>
        </div>
        <div class="faq-answer">
          <p>{{ item.answer }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

