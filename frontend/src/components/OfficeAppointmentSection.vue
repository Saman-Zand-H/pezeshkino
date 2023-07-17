<template>
    <Teleport to="body">
        <AlertMessage :isVisible="alert.alertVisible" :alertType="alert.alertType" :ttl="alert.alertTTL" :msg="alert.alertMsg" />
    </Teleport>

    <fieldset class="px-9 w-full border border-gray-300 border-dashed" v-for="office in doctor.offices">
        <legend class="px-4 ms-auto text-xl text-gray-600">{{ office.office_title }}</legend>
        <div class="py-6 px-4 w-full">
            <OfficeMap :element_id="office.id" :office="office" />
            <p class="mt-8 mx-6 text-sm text-right">
                آدرس : {{ office.address }}
            </p>
            <p class="mt-4 mx-6 text-sm text-right">
                تلفن : {{ office.phonenumber }}
            </p>
            <div class="mt-8 text-xl text-right">
                <h1 class="mb-5">ساعات پذیرش</h1>
                <ul v-for="day in office.availability_days" class="mx-4 my-1">
                    <li class="flex flex-row-reverse gap-6 items-baseline">
                        <h4 class="text-lg">{{ day.get_day_of_week_display }}</h4>
                        <small class="text-sm">
                            {{ day.since }} - {{ day.till }}
                        </small>
                    </li>
                </ul>
            </div>
            <Teleport to="body">
                <div :class="appointment_modal_display ? '': 'hidden'">
                    <div class="fixed w-screen h-screen top-0 left-0 bg-slate-400/50 z-30"></div>
                    <div class="fixed text-slate-800 mx-auto inset-x-0 md:w-1/2 w-3/4 top-10 bg-white py-7 px-10 border rounded-xl shadow-lg z-50">
                        <div class="flex flex-col">
                            <header class="flex flex-row-reverse items-baseline border-b pb-5 gap-5">
                                <button class="" type="button" @click.prevent="appointment_modal_display=false">
                                    <i class="fa fa-close text-sm"></i>
                                </button>
                                <h1 class="text-lg">تعیین قرار ملاقات با دکتر {{ doctor.user.name }}</h1>
                            </header>
                            <Suspense>
                                <AppointmentNavigation 
                                    :appointment_time=appointment_time
                                    />
                            </Suspense>
                            <button 
                                    class="bg-amber-400 disabled:bg-amber-400/50 disabled:text-black/70 hover:bg-amber-400/90 rounded-lg py-2 px-3 w-full self-end mx-5 my-4"
                                    type="button"
                                    @click.prevent="requestAppointment"
                                    :disabled="appointment_time == null"
                                >
                                تایید نهایی
                            </button>
                        </div>
                    </div>
                </div>
            </Teleport>
            <fieldset class="mx-3 my-5 pb-5 pt-2 px-7 flex flex-col gap-5 border border-gray-400 border-dashed">
                <legend class="text-xl text-right mb-5 px-4">نوبت دهی اینترنتی</legend>
                <input 
                        class="hidden" 
                        type="radio" 
                        name="appointment_btn"
                        :value="[[office.earliest_appointment.date, 'T', office.earliest_appointment.time].join(''), office.id]"
                        @input="$emit('appointmentChange', $event.target.value.split(','))"
                        :id="['earliest_btn_', office.id].join('')"
                        :checked="appointment_time === $el.value"
                        >
                <label :for="['earliest_btn_', office.id].join('')" class="text-right justify-center px-5 py-4 w-full items-center rounded-lg transition-colors duration-200 border hover:cursor-pointer focus:border-sky-800 hover:border-sky-800/60 shadow-md gap-6">
                    <div class="flex flex-col gap-2">
                        <span class="text-lg">
                            :نزدیک ترین نوبت خالی
                        </span>
                        <span class="text-sm px-3" v-if="!isEmpty(office.earliest_appointment)">
                            {{ moment(office.earliest_appointment.date).format('dddd D jMMMM') }} - 
                            ساعت
                            {{ moment(office.earliest_appointment.time, "HH:mm:ss").format('HH:mm') }}
                        </span>
                        <span class="" v-else>
                            این مطب دارای زمان خالی نمیباشد
                        </span>
                    </div>
                </label>
                <button 
                    class="text-right justify-center px-5 py-4 mb-5 w-full items-center rounded-lg transition-colors duration-200 border hover:border-sky-800/60 shadow-md gap-6" 
                    type="button" 
                    v-show="!isEmpty(office.availability_days)"
                    @click.prevent="appointment_modal_display=true"
                    >
                    <div class="flex flex-col gap-2">
                        <span class="text-lg">
                            انتخاب زمان دیگر
                        </span>
                    </div>
                </button>
                <button 
                        class="bg-amber-400 disabled:bg-amber-400/50 disabled:text-black/70 hover:bg-amber-400/90 rounded-lg py-2 px-3 w-24 self-end mx-5 my-4"
                        type="button"
                        @click="requestAppointment"
                        :disabled="appointment_time == null"
                        v-show="!isEmpty(office.availability_days)"
                        >
                    تایید نهایی
                </button>
            </fieldset>
        </div>
    </fieldset>
</template>

<script>
    import api from '@/_helpers/api'
    import fa from 'moment/locale/fa'
    import moment from 'moment-jalaali'
    import original_moment from 'moment'
    import isEmpty from 'lodash/isEmpty'
    import AlertMessage from './AlertMessage.vue'
    import OfficeMap from '@/components/OfficeMap.vue'
    import AppointmentNavigation from './AppointmentNavigation.vue'

    export default {
        name: 'OfficeAppointmentSection',
        emits: {
            appointmentChange: Array
        },
        data() {
            return {
                appointment_modal_display: false,
                confirm_display: false,
                alert: {
                    alertType: 'danger',
                    alertMsg: '',
                    alertTTL: 3,
                    alertVisible: false
                }
            }
        },
        props: {
            doctor: Object,
            appointment_time: Array
        },
        components: {
            OfficeMap,
            AppointmentNavigation,
            AlertMessage,
        },
        methods: {
            async requestAppointment(e) {
                if (this.$props.appointment_time == null || !this.dataIsValid()) {
                    this.fireAlert('لطفا یک زمان را انتخاب کنبد')
                }
                try {
                    const data = {
                        office_id: this.$props.appointment_time[1],
                        datetime: this.$props.appointment_time[0]
                    }
                    const res = await api.post("/api/make_appointment/", data)
                    this.fireAlert('قرار ملاقات با موفقیت تنظیم شد', 3, 'success')
                } catch(errors) {
                    console.log(errors)
                }
            },
            dataIsValid() {
                const values = this.$props.appointment_time
                const dateValid = original_moment(values[0], moment.ISO_8601, true).isValid()
                return dateValid && Number.isSafeInteger(values[1])
            },
            fireAlert(msg, ttl = 3, type = "danger") {
                this.$data.alert.alertVisible = true
                this.$data.alert.alertTTL = ttl
                this.$data.alert.alertType = type
                this.$data.alert.alertMsg = msg
                setTimeout(
                    () => {
                        this.$data.alert.alertVisible = false
                    },
                    ttl * 1000
                )
            }
        },
        setup() {
            moment.locale("fa", fa)
            moment.loadPersian()
            return {
                moment,
                isEmpty
            }
        },
    }
</script>
