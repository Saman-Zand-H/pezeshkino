<template>
    <div class="flex lg:flex-row-reverse flex-col px-4 mt-8 gap-6">
        <aside class="lg:w-1/4 w-full">
            <DoctorsSearchForm />
        </aside>
        <main class="lg:w-3/4 w-full px-8 mt-4 mb-7 flex flex-row flex-wrap gap-7">
            <DoctorCard 
                        v-for="doctor in doctors.doctors"
                        :name="doctor.user.name"
                        :username="doctor.user.username"
                        :spcialty="doctor.specialty"
                        :specialty_display="doctor.get_specialty_display"
                        :picture_link="doctor.user.picture"
                        :verified="doctor.verified"
                        />
        </main>
    </div>
</template>

<script>
    import { mapState } from 'vuex'
    import DoctorCard from '@/components/DoctorCard.vue'
    import DoctorsSearchForm from './DoctorsSearchForm.vue'

    export default {
        name: "DoctorsListBody",
        components: {
            DoctorCard,
            DoctorsSearchForm
        },
        computed: {
            ...mapState(["doctors"])
        },
        mounted() {
            this.$store.dispatch("doctors/fetchDoctors")
        }
    }
</script>