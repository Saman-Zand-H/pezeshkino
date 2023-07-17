<template>
    <header class="bg-white">
        <DoctorsNavbar />
        <div class="">
            <div class="flex flex-row-reverse relative h-14 text-white text-base border-b shadow-md border-slate-500/50 bg-cyan-950 gap-2 items-center pe-6">
                <router-link to="home" class="hover:text-cyan-500 transition-all duration-500">صفحه اصلی</router-link>
                <div v-for="item in breadcrumb" class="flex flex-row-reverse gap-3">
                    <span><i class="fa fa-circle text-cyan-700/90" style="font-size:.5rem"></i></span>
                    <!-- todo: consider using an array of objects containing both a title and a path-name. -->
                    <router-link :to="{name:doctors}" class="hover:text-cyan-500 transition-all duration-500">{{ item }}</router-link>
                </div>
            </div>
        </div>
    </header>
</template>

<script>
    import DoctorCard from './DoctorCard.vue'
    import DoctorsNavbar from './DoctorsNavbar.vue'
    import DoctorsSearchForm from './DoctorsSearchForm.vue'

    export default {
        name: "DoctorsContainer",
        props: {
            breadcrumb: Array
        },
        components: {
            DoctorCard,
            DoctorsNavbar,
            DoctorsSearchForm,
        }
    }
</script>