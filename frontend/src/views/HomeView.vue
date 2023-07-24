<template>
    <div class="w-full overflow-hidden scroll-smooth">
        <HomeNavbar :isActive="isActive" @toggle-collapse="this.$data.isActive = !isActive" />
        <div :class="[isActive ? 'brightness-50' : '', 'transition-all overflow-hidden flex flex-col duration-300 h-full']">
            <HomeSearchSection />
            <HomeFooter />
        </div>
    </div>
</template>

<script>
import HomeNavbar from '@/components/HomeNavbar.vue'
import HomeSearchSection from '@/components/HomeSearchSection.vue'
import HomeFooter from '@/components/HomeFooter.vue'

export default {
    name: 'HomeView',
    components: {
        HomeNavbar,
        HomeFooter,
        HomeSearchSection
    },
    data() {
        return {
            isActive: false
        }
    },
    methods: {
        handleClick(e) {
            if (
                !(document.querySelector("#navSidebar").contains(e.target)
                    || e.target.id === "navToggleMenuBtn"
                    || e.target.id === "navToggleBurger") && this.isActive
            ) {
                this.isActive = !this.isActive
            }
        }
    },
    created() {
        if (document.body.scrollTop >= 30 || document.activeElement.scrollTop >= 30) {
            this.isActive = true
        }
    },
    updated() {
        if (this.isActive) {
            window.addEventListener('click', this.handleClick)
        }
    },
    beforeUnmount() {
        window.removeEventListener('click', this.handleClick)
    },
}
</script>
