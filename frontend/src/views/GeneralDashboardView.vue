<template>
    <div class="overflow-hidden bg-slate-100">
        <DashboardNavbar />
        <div class="w-full relative flex h-screen px-4 justify-between items-start">
            <DashboardSidebar />
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
    import DashboardSidebar from '@/components/DashboardSidebar.vue'
    import DashboardNavbar from '@/components/DashboardNavbar.vue'

    export default {
        name: 'GeneralDoctorDashboardView',
        components: {
            DashboardSidebar,
            DashboardNavbar
        }
    }
</script>