<template>
  <div class="relative w-full">
    <HomeNavbar :isActive="isActive" @toggle-collapse="toggleCollapse" />
    <div :class="[isActive ? 'brightness-50' : '', 'w-full transition-all duration-300 h-full relative']">
      <HomeSection />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import HomeNavbar from '@/components/HomeNavbar.vue'
import HomeSection from '@/components/HomeSection.vue'
import AlertMessage from '@/components/AlertMessage.vue'

export default {
  name: 'HomeView',
  components: {
    HomeNavbar,
    HomeSection
  },
  data() {
    return {
      isActive: false
    }
  }, 
  methods: {
    toggleCollapse() {
      this.isActive = !this.isActive
    }
  },
  updated() {
    if (this.isActive) {
      window.addEventListener('click', e => {
        if (!(document.querySelector("#navSidebar").contains(e.target) || e.target.id === "navToggleMenuBtn")) {
          this.isActive = !this.isActive
        }
      })
    }
  }
}
</script>

<style>
  html {
    scroll-behavior: smooth;
  }
</style>
