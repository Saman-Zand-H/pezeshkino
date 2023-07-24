<template>
    <div>
        <div class="grid grid-cols-1">
            <div class="flex flex-col gap-10 rounded-xl shadow-md w-full px-12 py-7 bg-white my-2" v-for="appointment in appointments">
                <div class="flex justify-between w-full">
                    <div class="flex flex-col items-center gap-2">
                        <span>{{ appointment.office.doctor }}</span>
                        <span><i class="fa fa-user-doctor"></i></span>
                    </div>
                    <div class="flex flex-col items-center gap-2">
                        <span>
                            {{ appointment.patient.first_name }} 
                            {{ appointment.patient.last_name }}
                        </span>
                        <span><i class="fa fa-user-injured"></i></span>
                    </div>
                </div>
                <div class="flex flex-col items-end gap-5">
                    <div style="direction: rtl">
                        شماره تماس بیمار 
                        : 
                        {{ appointment.patient.phonenumber }}
                    </div>
                    <div style="direction: rtl">
                        ساعت و تاریخ ملاقات
                        :
                        {{ jmoment(appointment.datetime, "YYYY-MM-DTHH:mm:ss").format("dddd jD jMMMM jYYYY, ساعت HH:mm") }}
                    </div>
                    <div style="direction: rtl">
                        پذیرش در مطب
                        :
                        {{ appointment.office.office_title }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import moment from 'moment'
    import api from '@/_helpers/api'
    import fa from 'moment/locale/fa'
    import jmoment from 'moment-jalaali'

    export default {
        name: 'AppointmentsDashboardView',
        data() {
            return {
                appointments: [],
                page: 1
            }
        },
        setup() {
            moment.updateLocale("fa", fa)
            jmoment.loadPersian({dialect: "persian-modern", usePersianDigits: true})

            return {
                moment, 
                jmoment
            }
        },
        async beforeMount() {
            const url = `/api/doctor_appointments?page=${this.page}`
            try {
                const res = await api.get(url)
                if (res.status === 200) {
                    this.appointments = res.data.results
                }
            } catch (error) {console.error(error)}
        }
    }
</script>