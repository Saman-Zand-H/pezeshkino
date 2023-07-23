<template>
    <div class="">
        <DashboardNavbar @toggle-sidebar="this.sidebarActive = !sidebarActive" />
        <div class="w-full relative flex h-fit px-4 justify-between items-start">
            <DashboardSidebar :sidebarActive="sidebarActive" />
            <main :class="[sidebarActive ? 'ms-[21%]' : 'lg:ms-[9%]', 'mt-20 w-full transition-all duration-200']">
                <router-view></router-view>
                <DashboardFooter />
            </main>
        </div>
    </div>
</template>

<style>
    body {
        background-color: rgb(226 232 240 / .6);
        height: 100vh;
    }
</style>

<script>
    import DashboardSidebar from '@/components/DashboardSidebar.vue'
    import DashboardNavbar from '@/components/DashboardNavbar.vue'
    import DashboardFooter from '@/components/DashboardFooter.vue'

    export default {
        name: 'GeneralDoctorDashboardView',
        components: {
            DashboardSidebar,
            DashboardNavbar,
            DashboardFooter
        },
        data() {
            return {
                sidebarActive: false
            }
        }
    }
</script>