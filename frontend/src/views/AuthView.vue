<template>
    <main 
          class="w-full h-screen relative after:bg-contain after:fixed after:w-full after:h-full after:-z-10 after:top-0 after:left-0 after:brightness-50"
         >
        <HomeNavbar :isActive="isActive" @toggle-collapse="this.$data.isActive = !isActive" />

        <div :class="[isActive ? 'brightness-50 transition-all duration-300' : '', 'relative']">
            <router-view></router-view>
        </div>
    </main>
</template>

<style scoped>
    main::after {
        background-image: url('@/assets/auth-bg.webp');
    }
</style>

<script>
    import HomeNavbar from '@/components/HomeNavbar.vue'
    import HomeFooter from '@/components/HomeFooter.vue'

    export default {
        name: 'AuthView',
        data() {
            return {
                isActive: false
            }
        },
        components: {
            HomeNavbar,
            HomeFooter,
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
            },
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