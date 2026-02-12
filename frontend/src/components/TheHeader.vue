<script setup>
import { ref } from 'vue'

const isMenuOpen = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
  document.body.style.overflow = isMenuOpen.value ? 'hidden' : ''
}

const closeMenu = () => {
  isMenuOpen.value = false
  document.body.style.overflow = ''
}

const scrollToSection = (id) => {
  closeMenu()
  const element = document.getElementById(id)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' })
  }
}
</script>

<template>
  <header class="main-header">
    <a href="#" class="logo" @click.prevent="scrollToSection('hero')">
      <img src="/addons/rguk.svg" alt="РГУ им. А.Н. Косыгина">
    </a>

    <nav class="header-nav">
      <ul>
        <li><a href="#benefits" @click.prevent="scrollToSection('benefits')">Преимущества</a></li>
        <li><a href="#steps" @click.prevent="scrollToSection('steps')">Этапы</a></li>
        <li><a href="#materials" @click.prevent="scrollToSection('materials')">Материалы</a></li>
        <li><a href="#reviews" @click.prevent="scrollToSection('reviews')">Отзывы</a></li>
        <li><a href="#contacts" @click.prevent="scrollToSection('contacts')">Контакты</a></li>
        <li><a href="#faq" @click.prevent="scrollToSection('faq')">FAQ</a></li>
      </ul>
    </nav>

    <button class="burger" @click="toggleMenu">☰</button>

    <div class="mobile-menu-overlay" :class="{ active: isMenuOpen }" @click="closeMenu"></div>

    <div class="mobile-menu" :class="{ open: isMenuOpen }">
      <button class="close-btn" @click="closeMenu">
        <img src="/addons/close.svg" alt="Закрыть">
      </button>
      
      <div class="mobile-nav">
        <ul>
          <li><a href="#benefits" @click.prevent="scrollToSection('benefits')">Преимущества</a></li>
          <li><a href="#steps" @click.prevent="scrollToSection('steps')">Этапы</a></li>
          <li><a href="#materials" @click.prevent="scrollToSection('materials')">Материалы</a></li>
          <li><a href="#reviews" @click.prevent="scrollToSection('reviews')">Отзывы</a></li>
          <li><a href="#contacts" @click.prevent="scrollToSection('contacts')">Контакты</a></li>
          <li><a href="#faq" @click.prevent="scrollToSection('faq')">FAQ</a></li>
        </ul>
      </div>
    </div>
  </header>
</template>

<style scoped>
.main-header {
  background-color: var(--primary-dark);
  color: var(--text-white);
  padding: 15px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 1000;
  box-sizing: border-box;
  height: 80px;
  min-height: 80px;
  transition: var(--transition);
}

.logo {
  display: flex;
  align-items: center;
  height: 100%;
}

.logo img {
  max-width: 300px;
  height: auto;
  filter: brightness(0) invert(1);
}

.header-nav {
  margin-left: auto;
  margin-right: 20px;
}

.header-nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
}

.header-nav > ul > li {
  margin-left: 30px;
}

.header-nav a {
  color: var(--text-white);
  text-decoration: none;
  padding: 10px 16px;
  border-radius: 6px;
  font-weight: bold;
  font-size: 1.1rem;
  transition: var(--transition);
  letter-spacing: 0.3px;
  display: flex;
  align-items: center;
}

.header-nav a:hover {
  background-color: var(--secondary-color);
  color: var(--text-dark);
  box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.1);
}

.burger {
  display: none;
  font-size: 28px;
  background: none;
  border: none;
  color: var(--text-white);
  cursor: pointer;
  margin-left: auto;
  padding: 0;
  width: 40px;
  height: 40px;
}

.mobile-menu-overlay {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1000;
  backdrop-filter: blur(3px);
  transition: opacity 0.3s ease;
  opacity: 0;
}

.mobile-menu-overlay.active {
  display: block;
  opacity: 1;
}

.mobile-menu {
  display: none;
  position: fixed;
  top: 0;
  right: -100%;
  width: 85%;
  max-width: 320px;
  height: 100vh;
  background-color: var(--primary-dark);
  z-index: 1001;
  padding: 80px 20px 40px;
  box-sizing: border-box;
  flex-direction: column;
  overflow-y: auto;
  transition: right 0.3s ease-in-out;
  box-shadow: -5px 0 15px rgba(0, 0, 0, 0.3);
}

.mobile-menu.open {
  display: flex;
  right: 0;
}

.close-btn {
  display: block; /* Always visible in mobile menu */
  position: absolute;
  right: 20px;
  top: 20px;
  background: none;
  border: none;
  cursor: pointer;
  z-index: 1002;
  padding: 0;
}

.close-btn img {
  width: 28px;
  height: 28px;
  filter: brightness(0) invert(1);
}

.mobile-nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.mobile-nav li {
  margin-bottom: 15px;
}

.mobile-nav a {
  color: var(--text-white);
  text-decoration: none;
  font-size: 1.2rem;
  display: block;
  padding: 10px;
  border-radius: var(--radius-sm);
  transition: var(--transition);
}

.mobile-nav a:hover {
  background-color: rgba(255, 255, 255, 0.1);
  padding-left: 20px;
}

@media (max-width: 992px) {
  .header-nav {
    display: none;
  }
  
  .burger {
    display: block;
  }
  
  .mobile-menu {
    display: block; /* Enable flex via .open class, but block for base display property override if needed? No, css says display: none by default */
  }
}

@media (max-width: 768px) {
  .main-header {
    height: 65px;
    min-height: 65px;
    padding: 10px 15px;
  }
  
  .logo img {
    max-width: 180px;
  }
}
</style>
