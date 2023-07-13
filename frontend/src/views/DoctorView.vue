<template>
    <div class="relative">
        <Teleport to="body">
            <AlertMessage v-if="alert.alertVisible" :alertType="alert.alertType" :ttl="alert.alertTTL" :msg="alert.alertMsg" />
        </Teleport>

        <DoctorsContainer :breadcrumb="['پزشکان', `دکتر ${doctor.user.name}`]" />

        <div class="flex lg:flex-row-reverse flex-col my-9 mx-10 gap-8">
            <aside class="lg:w-1/4 w-full">
                <div class="rounded-lg shadow-xl bg-white border flex flex-col justify-center items-center py-8">
                    <div class="h-60 w-40 mt-2 bg-white z-10">
                        <!-- todo: consider a default picture -->
                        <img :alt="[doctor.user.name, 'picture']" :src="doctor.user.picture"
                            class="box-content shadow-lg overflow-clip rounded-full border-8 border-slate-200/40 -z-10">
                    </div>
                    <div class="flex flex-col justify-center items-center">
                        <span>
                            <h2 class="text-base text-gray-600 font-semibold">{{ doctor.user.name }} دکتر</h2>
                        </span>
                        <span class="mt-2">
                            <small class="text-sm text-gray-500">{{ doctor.get_specialty_display }}</small>
                        </span>
                        <span class="mt-2">
                            <small class="text-gray-500" style="font-size: xx-small;">نظام پزشکی: {{ doctor.upin }}</small>
                        </span>
                    </div>
                </div>
            </aside>
            <main class="lg:w-3/4 w-full">
                <ul class="flex flex-row-reverse flex-wrap shadow-lg border bg-white py-3 gap-3 px-7 mb-4 lg:mt-0 mt-4 rounded-lg justify-start">
                    <li>
                        <button @click="tab_page='office_info'" :class="[tab_page === 'office_info' ? 'active bg-gray-100 text-cyan-800': 'hover:bg-gray-100/50 hover:text-gray-600 text-gray-500', 'inline-block transition-all duration-200 rounded-xl text-sm py-2 px-6 font-medium text-center']">
                            آدرس و نوبت دهی
                        </button>
                    </li>
                    <li class="">
                        <button @click="tab_page='about'" :class="[tab_page === 'about' ? 'active bg-gray-100 text-cyan-800': 'hover:bg-gray-100/50 hover:text-gray-600 text-gray-500', 'inline-block transition-all duration-200 rounded-xl text-sm py-2 px-6 font-medium text-center']">
                            درباره پزشک
                        </button>
                    </li>
                </ul>
                <div class="rounded-lg shadow-xl bg-white border flex flex-col justify-center relative w-full items-center py-8 px-10">
                    <div :class="tab_page === 'office_info' ? 'w-full' : 'hidden'">
                        <fieldset class="px-9 w-full border border-gray-300 border-dashed" v-for="office in doctor.offices">
                            <legend class="px-4 ms-auto text-xl text-gray-600">{{ office.office_title }}</legend>
                            <div class="py-6 px-4 w-full">
                                <OfficeMap :office="office" />
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
                                        <div class="absolute text-slate-800 mx-auto inset-x-0 md:w-1/2 w-3/4 top-[18.5rem] bg-white py-7 px-10 border rounded-xl shadow-lg z-50">
                                            <div class="flex flex-col">
                                                <header class="flex flex-row-reverse items-baseline border-b pb-5 gap-5">
                                                    <button class="" type="button" @click.prevent="appointment_modal_display=false">
                                                        <i class="fa fa-close text-sm"></i>
                                                    </button>
                                                    <h1 class="text-lg">تعیین قرار ملاقات با دکتر {{ doctor.user.name }}</h1>
                                                </header>
                                                <Suspense>
                                                    <AppointmentNavigation @hide-confirm="confirm_display=false" @show-confirm="confirm_display=true" />
                                                </Suspense>
                                                <button 
                                                        v-if="confirm_display" class="bg-amber-400 rounded-lg py-2 px-3 w-24 self-end mx-5 my-4"
                                                        @click.prevent="requestAppointment"
                                                    >
                                                    تایید نهایی
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </Teleport>
                                <fieldset class="mx-3 my-5 py-5 px-7 flex flex-col gap-5 border border-gray-400 border-dashed">
                                    <legend class="text-xl text-right mb-5 px-4">نوبت دهی اینترنتی</legend>
                                    <div class="flex flex-row-reverse">
                                        
                                    </div>
                                    <input 
                                            class="hidden" 
                                            type="radio" 
                                            name="appointment_btn"
                                            :value="office.earliest_appointment"
                                            v-model="appointment_time"
                                            id="earliest_btn"
                                         >
                                    <label for="earliest_btn" class="text-right justify-center px-5 py-4 w-full items-center rounded-lg transition-colors duration-200 border hover:cursor-pointer focus:border-sky-800 hover:border-sky-800/60 shadow-md gap-6">
                                        <div class="flex flex-col gap-2">
                                            <span class="text-lg">
                                                :نزدیک ترین نوبت خالی
                                            </span>
                                            <span class="text-sm px-3" v-if="office.earliest_appointment">
                                                {{ moment(office.earliest_appointment.date).format('dddd D jMMMM') }} - 
                                                ساعت
                                                {{ moment(office.earliest_appointment.data).format('HH:mm') }}
                                            </span>
                                        </div>
                                    </label>
                                    <button 
                                        class="text-right justify-center px-5 py-4 mb-5 w-full items-center rounded-lg transition-colors duration-200 border hover:border-sky-800/60 shadow-md gap-6" 
                                        type="button" 
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
                                            @click.prevent="requestAppointment"
                                            :disabled="appointment_time == null"
                                         >
                                        تایید نهایی
                                    </button>
                                </fieldset>
                            </div>
                        </fieldset>
                    </div>
                    <div :class="tab_page === 'about' ? 'w-full' : 'hidden'">
                        <fieldset class="text-right px-4 border border-dashed">
                            <legend class="flex flex-row-reverse gap-3 px-4 items-center">
                                <i class="fas fa-newspaper text-2xl"></i>
                                <h1 class="text-xl">بیوگرافی</h1>
                            </legend>
                            <pre class="text-right my-5 text-sm leading-7 px-3">
                                {{ doctor.bio }}
                            </pre>
                        </fieldset>
                    </div>
                </div>
            </main>
        </div>
    </div>
</template>

<style>
    body {
        position: relative;
    }

    input[name="appointment_btn"]:checked+label {
        border-color: rgb(7 89 133);
    }
</style>

<script>
import axios from 'axios'
import moment from 'moment-jalaali'
import AlertMessage from '@/components/AlertMessage.vue'
import OfficeMap from '@/components/OfficeMap.vue'
import DoctorsContainer from '@/components/DoctorsContainer.vue'
import AppointmentNavigation from '@/components/AppointmentNavigation.vue'

export default {
    name: "DoctorView",
    components: {
        DoctorsContainer,
        AppointmentNavigation,
        OfficeMap,
        AlertMessage
    },
    setup() {
        return {
            moment
        }
    },
    data() {
        return {
            doctor: {
                user: {
                    name: null
                }
            },
            tab_page: 'office_info',
            appointment_modal_display: false,
            confirm_display: false,
            appointment_time: null,
            alert: {
                alertType: 'danger',
                alertMsg: '',
                alertTTL: 3,
                alertVisible: false
            }
        }
    },
    methods: {
        requestAppointment(e) {
            console.log("bitch")
            // if (!Boolean(this.$data.appointment_time)) {
            //     this.fireAlert("لطفا ابتدا زمان نوبت خود را انتخاب کنید.")
            // }
        },
        fireAlert(msg, ttl=3, type="danger") {
            let alertOptions = this.$data.alert
            alertOptions.alertVisible = true
            alertOptions.alertTTL = ttl
            alertOptions.alertType = type
            alertOptions.alertMsg = msg
            setTimeout(
                () => {
                    alertOptions.alertVisible = false
                    alertOptions.alertMsg = ''
                }, 
                ttl * 1000
            )
        }
    },
    async beforeCreate() {
        const username = this.$route.params.username
        try {
            const res = await axios.get(`/api/doctor/${username}`)
            this.$data.doctor = res.data
        } catch {
            console.error("non-existent user!")
        }
    },
}
</script>