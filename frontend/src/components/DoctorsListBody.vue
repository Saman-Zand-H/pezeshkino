<template>
    <div class="flex lg:flex-row-reverse flex-col px-4 mt-8 gap-6">
        <aside class="lg:w-1/4 w-full">
            <DoctorsSearchForm />
        </aside>
        <main class="lg:w-3/4 w-full px-8 mt-4 mb-7 flex flex-col items-center gap-7">
            <div class="flex flex-row flex-wrap w-full gap-7">
                <div class="flex gap-6 w-full flex-shrink-0 justify-start flex-grow-0 flex-wrap" v-if="doctors.loading">
                    <div v-for="_ in 6" :key="_" class="flex flex-col animate-pulse card relative rounded-lg border max-w-none overflow-hidden shadow-lg w-72 aspect-square pb-3 gap-5 transition-all duration-300">
                        <div class="-z-50 relative">
                            <div class="w-full aspect-square bg-gray-400/80"></div>
                        </div>
                        <div class="flex flex-col bg-gray-300 z-50 h-40 absolute inset-x-0 w-full -bottom-20 shadow-sm card-body transition-all duration-500">
                            <span class="w-3/4 bg-gray-400/80 h-3 rounded-full mx-auto my-3">
                                <h1 class="font-semibold text-lg"></h1>
                            </span>
                            <span class="w-1/2 mx-auto bg-gray-400/80 rounded-full h-2">
                                <small class="text-cyan-950"></small>
                            </span>
                        </div>
                    </div>
                </div>
                <div v-if="!doctors.loading && isEmpty(doctors.doctors)" class="bg-white rounded-xl w-full h-full p-5 text-3xl items-center justify-center text-gray-600 flex flex-col gap-5">
                    <span><i class="fa fa-close text-8xl"></i></span>
                    <span style="direction: rtl">هیچ پزشکی یافت نشد..</span>
                </div>
                <DoctorCard 
                            v-if="!doctors.loading"
                            v-for="doctor in doctors.doctors"
                            :name="doctor.user.name"
                            :username="doctor.user.username"
                            :spcialty="doctor.specialty"
                            :specialty_display="doctor.get_specialty_display"
                            :picture_link="doctor.user.picture || require('@/assets/blank-user.png/')"
                            :verified="doctor.verified"
                            />
            </div>
            <Paginator v-if="doctors?.paginator.pages>1" :page="page" :count="doctors?.paginator.pages" @page-changed="pageChanged" />
        </main>
    </div>
</template>

<script>
    import isEmpty from 'lodash/isEmpty'
    import { mapState, mapActions } from 'vuex'
    import Paginator from '@/components/Paginator.vue'
    import DoctorCard from '@/components/DoctorCard.vue'
    import DoctorsSearchForm from '@/components/DoctorsSearchForm.vue'

    export default {
        name: "DoctorsListBody",
        components: {
            DoctorCard,
            DoctorsSearchForm,
            Paginator
        },
        data() {
            return {
                page: 1
            }
        },
        computed: {
            ...mapState(["doctors"])
        },
        methods: {
            ...mapActions({fetchDoctors: "doctors/fetchDoctors"}),
            async pageChanged(value) {
                this.page = value
                await this.fetchDoctors(this.page)
            }
        },
        async beforeMount() {
            await this.fetchDoctors(this.page)
        },
        setup() {
            return {
                isEmpty
            }
        }
    }
</script>