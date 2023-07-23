<template>
    <div class="rounded-md bg-zinc-200/60 w-full my-2 py-6 px-12 flex flex-col gap-9" v-for="appointment in appointments">
        <div class="flex md:flex-row flex-col md:items-center items-end md:gap-0 gap-6 flex-wrap md:justify-between md:flex-nowrap px-4 text-xl">
            <div class="flex gap-4 items-center">
                دکتر {{ appointment.office.doctor }} ({{ appointment.office.doctor_specialty }})
                <i class="fa fa-user-doctor text-3xl"></i>
            </div>
            <div class="flex gap-4 items-center">
                {{ user.first_name }} {{ user.last_name }}
                <i class="fa fa-user-injured text-3xl"></i>
            </div>
        </div>
        <div class="w-full flex flex-col gap-4">
            <div class="flex gap-2 justify-end items-center">
                تاریخ و زمان : {{ jmoment(appointment.datetime, "YYYY-MM-DDTHH:mm:ss").format("dddd jD jMMMM jYYYY  ساعت HH:mm") }}
                <i class="fa fa-clock"></i>
            </div>
            <div class="flex gap-2 justify-end items-center">
                شماره تماس : {{ appointment.office.phonenumber }}
                <i class="fa fa-phone"></i>
            </div>
        </div>
        <div class="flex flex-col">
            <span class="flex gap-4 justify-end items-center">
                آدرس و مکان : {{ appointment.office.address }}
                <i class="fa fa-map"></i>
            </span>
            <div class="mt-6 mb-3">
                <OfficeMap :element_id="appointment.uuid" :office="appointment.office" />
            </div>
        </div>
    </div>
</template>

<script>
    import jmoment from 'moment-jalaali'
    import OfficeMap from './OfficeMap.vue'
    import api from '@/_helpers/api'
    import fa from 'moment/locale/fa'
    import { mapState } from 'vuex'
    
    export default {
        name: 'AppointmentsList',
        props: {
            appointmentType: String
        },
        async beforeCreate() {
            await this.$store.dispatch("updateUserInfo")
        },
        computed: {
            ...mapState(["user"])
        },
        components: {
            OfficeMap,
        },
        async setup(props, ctx) {
            let appointments = []
            jmoment.updateLocale("fa", fa)
            jmoment.loadPersian({dialect: 'persian-modern'})
            switch (props.appointmentType) {
                case 'patient':
                    try {
                        const res = await api.get("/api/patient/get_appointments/")
                        appointments = res.data
                    } catch {}
                // todo: handle reject and doctor appointment
                case 'doctor':
                    try {
                        const res = await api.get("/api/patient/get_appointments/")
                        appointments = res.data
                    } catch {}
            }
            return {
                appointments: appointments,
                jmoment
            }
        }
    }
</script>
