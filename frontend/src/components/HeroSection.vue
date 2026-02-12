<template>
  <section class="main-section" id="hero">
    <div class="container" style="display: flex; flex-direction: column; align-items: center;">
      <div class="hero-text-wrapper" style="width: fit-content; display: flex; flex-direction: column; align-items: center;">
        <h1 class="hero-title section-animate">Переводитесь в РГУ им. Косыгина без стресса</h1>
        <p class="hero-subtitle section-animate" style="text-align: center; width: 100%;">Пошаговая инструкция, которая проведет вас от идеи до зачисления. Четко, ясно, ничего лишнего.</p>
      </div>
      <a href="#steps" class="cta-button section-animate" @click.prevent="scrollTo('#steps')">Начать перевод</a>
    </div>
  </section>
</template>

<script setup>
const scrollTo = (selector) => {
  const element = document.querySelector(selector)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' })
  }
}
</script>
