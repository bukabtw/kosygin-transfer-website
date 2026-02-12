<script setup>
const currentYear = new Date().getFullYear()

const scrollToSection = (id) => {
  const element = document.getElementById(id)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' })
  }
}
</script>

<template>
  <footer class="footer">
    <div class="footer-content">
      <div class="footer-section">
        <h3>Навигация</h3>
        <ul>
          <li><a href="#steps" @click.prevent="scrollToSection('steps')">Этапы перевода</a></li>
          <li><a href="#materials" @click.prevent="scrollToSection('materials')">Полезные материалы</a></li>
          <li><a href="#contacts" @click.prevent="scrollToSection('contacts')">Контакты</a></li>
        </ul>
      </div>
      
      <div class="footer-section">
        <h3>Контакты</h3>
        <div class="footer-contact">
          <p>📧 itct@rguk.ru</p>
          <p>📞 +7 (495) 811-01-01, доб. 1069</p>
          <p>📍 Москва, ул. Малая Калужская, д. 1</p>
        </div>
      </div>
      
      <div class="footer-section">
        <h3>Официальные ресурсы</h3>
        <ul>
          <li><a href="https://rguk.ru/" target="_blank">Официальный сайт РГУ Косыгина</a></li>
          <li><a href="https://rguk.ru/sveden/vacant/" target="_blank">Вакантные места</a></li>
          <li><a href="https://rguk.ru/university/college/abitur/priem/" target="_blank">Приемная комиссия</a></li>
        </ul>
      </div>
    </div>
    
    <div class="footer-bottom">
      <p>&copy; {{ currentYear }} РГУ им. А.Н. Косыгина. Все права защищены.</p>
      
      <div class="footer-author">
        <span class="author-text">Designed & developed by </span>
        <a href="https://t.me/bukabtw" target="_blank" class="author-link">
          bukabtw
        </a>
      </div>
    </div>
  </footer>
</template>

<style scoped>
/* Footer styles are mainly in style.css, but we add specific overrides here */
.footer-author {
  margin-top: 10px;
  font-size: 0.9rem;
}

.author-text {
  font-style: italic;
  color: rgba(255, 255, 255, 0.6);
}

.author-link {
  font-weight: bold;
  background: linear-gradient(90deg, #ff00cc, #3333ff);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  text-decoration: none;
  background-size: 200% auto;
  animation: shine 3s linear infinite;
}

.author-link:hover {
  text-decoration: underline;
}

@keyframes shine {
  to {
    background-position: 200% center;
  }
}
</style>
