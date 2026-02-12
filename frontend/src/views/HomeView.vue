<template>
  <div class="home">
    <TheHeader />
    <main>
      <!-- Components will be added here -->
      <HeroSection />
      <BenefitsSection />
      <StepsSection />
      <MaterialsSection />
      <ChecklistSection />
      <CalculatorSection />
      <ReviewsSection />
      <DownloadsSection />
      <MistakesSection />
      <DeadlineSection />
      <ContactsSection />
      <FaqSection />
      <ApplicationSection />
    </main>
    <TheFooter />
  </div>
</template>

<script setup>
import TheHeader from '@/components/TheHeader.vue'
import TheFooter from '@/components/TheFooter.vue'
import HeroSection from '@/components/HeroSection.vue'
import BenefitsSection from '@/components/BenefitsSection.vue'
import StepsSection from '@/components/StepsSection.vue'
import MaterialsSection from '@/components/MaterialsSection.vue'
import ChecklistSection from '@/components/ChecklistSection.vue'
import CalculatorSection from '@/components/CalculatorSection.vue'
import ReviewsSection from '@/components/ReviewsSection.vue'
import DownloadsSection from '@/components/DownloadsSection.vue'
import MistakesSection from '@/components/MistakesSection.vue'
import DeadlineSection from '@/components/DeadlineSection.vue'
import ContactsSection from '@/components/ContactsSection.vue'
import FaqSection from '@/components/FaqSection.vue'
import ApplicationSection from '@/components/ApplicationSection.vue'

import { onMounted } from 'vue'

onMounted(() => {
  // Init intersection observer for animations
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1
  });

  document.querySelectorAll('.section-animate, .animate-in').forEach(el => {
    observer.observe(el);
  });
});
</script>
