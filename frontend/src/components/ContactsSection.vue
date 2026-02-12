<template>
  <section id="contacts" class="contacts-section section-animate" ref="sectionRef">
    <h2 class="section-title">Контакты</h2>
    <div class="contacts-container">
      <div class="contact-info">
        <div class="contact-item">
          <h3>Деканат для консультаций</h3>
          <ul class="contact-details">
            <li>📧 <a href="mailto:itct@rguk.ru" class="contact-link">itct@rguk.ru</a></li>
            <li>📞 <a href="tel:+74958110101" class="contact-link">+7 (495) 811-01-01, доб. 1069</a></li>
            <li>🕒 Пн-Пт: 9:00-18:00</li>
            <li>💬 Консультации по переводу</li>
          </ul>
        </div>
        <div class="contact-item">
          <h3>Приемная комиссия</h3>
          <ul class="contact-details">
            <li>📧 <a href="mailto:priem@rguk.ru" class="contact-link">priem@rguk.ru</a></li>
            <li>📞 <a href="tel:+74959515801" class="contact-link">+7 (495) 951-58-01</a></li>
            <li>🕒 Пн-Пт: 10:00-17:00</li>
            <li>📄 Подача документов</li>
          </ul>
        </div>
        <div class="contact-item">
          <h3>Адрес университета</h3>
          <ul class="contact-details">
            <li style="cursor: pointer;" @click="copyAddress">
              📍 <span class="address-text">Москва, ул. Малая Калужская, д. 1</span>
            </li>
            <li>🚇 Метро: Шаболовская</li>
            <li>🏛️ Главный учебный корпус</li>
          </ul>
        </div>
      </div>
      <div class="map-container">
        <iframe 
          src="https://yandex.ru/map-widget/v1/?ll=37.601494%2C55.720467&pt=37.601494%2C55.720467%2Cpm2orgl&z=17"
          frameborder="0"
          allowfullscreen="true"
          style="width: 100%; height: 100%; display: block;"
        ></iframe>
      </div>
    </div>
  </section>
</template>

<script setup>
import { onMounted, ref } from 'vue'

const sectionRef = ref(null)

const copyAddress = async () => {
  const address = 'Москва, ул. Малая Калужская, д. 1'
  try {
    await navigator.clipboard.writeText(address)
    alert('Адрес скопирован в буфер обмена!')
  } catch (err) {
    console.error('Failed to copy text: ', err)
  }
}

onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible')
        observer.unobserve(entry.target)
      }
    })
  }, {
    threshold: 0.1
  })

  if (sectionRef.value) {
    observer.observe(sectionRef.value)
  }
})
</script>

<style scoped>
/* Scoped styles are not strictly necessary as we are using global styles from style.css */
/* But we can add component specific overrides if needed */
.section-animate {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.8s ease-out, transform 0.8s ease-out;
}

.section-animate.visible {
  opacity: 1;
  transform: translateY(0);
}

.map-container iframe {
    width: 100%;
    height: 100%;
}
</style>
