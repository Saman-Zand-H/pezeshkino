<template>
    <div class="relative">
        <DoctorsContainer 
                :breadcrumb='[
                    {title: "پزشکان", url: {name: "doctors"}}, 
                    {title: `دکتر ${doctor.user.name}`, url: {name: "doctor", params: {username: this.$route.params.username}}}
                ]' 
            />

        <div class="flex lg:flex-row-reverse flex-col my-9 mx-10 gap-8">
            <aside class="lg:w-1/4 w-full">
                <div class="rounded-lg shadow-xl bg-white border flex flex-col justify-center items-center py-8" v-if="!loading">
                    <div class="h-60 w-40 mt-2 bg-white z-10">
                        <img :alt="[doctor.user.name, 'picture']" :src="doctor.user.picture || require('@/assets/blank-user.png')"
                            class="box-content shadow-lg h-44 aspect-video overflow-clip rounded-full border-4 border-slate-200/40 -z-10">
                    </div>
                    <div class="flex flex-col justify-center items-center">
                        <span>
                            <h2 class="text-base text-gray-600 font-semibold">
                                دکتر
                                {{ doctor.user.name }}
                            </h2>
                        </span>
                        <span class="mt-2">
                            <small class="text-sm text-gray-500">{{ doctor.get_specialty_display }}</small>
                        </span>
                        <span class="mt-2">
                            <small class="text-gray-500" style="font-size: xx-small;">نظام پزشکی: {{ doctor.upin }}</small>
                        </span>
                    </div>
                </div>
                <div class="rounded-lg animate-pulse shadow-xl bg-gray-200 border flex flex-col justify-center items-center py-8" v-else>
                    <div class="h-60 w-40 mt-2 z-10">
                        <div class="box-content shadow-lg h-44 w-44 overflow-clip rounded-full border-4 border-slate-200/40 -z-10"></div>
                    </div>
                    <div class="flex flex-col justify-center items-center w-2/3 gap-3">
                        <span class="h-6 bg-gray-300/80 rounded-full w-full"></span>
                        <span class="h-4 bg-gray-300/80 rounded-full w-full"></span>
                        <span class="h-3 bg-gray-300/80 rounded-full w-full"></span>
                    </div>
                </div>
            </aside>
            <main class="lg:w-3/4 w-full" v-if="!loading">
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
                    <li class="">
                        <button @click="tab_page='reviews'" :class="[tab_page === 'reviews' ? 'active bg-gray-100 text-cyan-800': 'hover:bg-gray-100/50 hover:text-gray-600 text-gray-500', 'inline-block transition-all duration-200 rounded-xl text-sm py-2 px-6 font-medium text-center']">
                            نظرات
                        </button>
                    </li>
                </ul>
                <div class="rounded-lg shadow-xl bg-white border flex flex-col justify-center relative w-full items-center py-8 px-10">
                    <div v-if="tab_page === 'office_info'" class="w-full">
                        <OfficeAppointmentSection 
                            v-if="!isEmpty(doctor.offices)"
                            :doctor="doctor"
                            :appointment_time="appointment_time" 
                            @appointmentChange="newVal => this.appointment_time=newVal" />
                        <div class="w-full h-full py-8 bg-white flex text-gray-500 flex-col items-center" v-else>
                            <span><i class="fa fa-close text-7xl"></i></span>
                            <span>هیچ مطبی برای پزشک مورد نظر ثبت نشده است</span>
                        </div>
                    </div>
                    <div v-else-if="tab_page === 'about'" class="w-full'">
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
                    <div v-else-if="tab_page === 'reviews'" class="w-full">
                        <div class="flex flex-col gap-8">
                            <router-link :to="{ name: 'new_review', params: {username: this.$route.params.username} }" class="text-center py-2.5 transition-colors duration-200 text-xl border border-sky-700 text-sky-800 rounded-xl hover:bg-sky-700 hover:text-white w-full" type="button">
                                ثبت نظر
                            </router-link>
                            <div class="">
                                <CommentSection :reviews="doctor.reviews" />
                            </div>
                        </div>
                    </div>
                </div>
            </main>
            <main class="lg:w-3/4 w-full animate-pulse" v-else>
                <ul class="flex flex-row-reverse flex-wrap shadow-lg border bg-gray-200 py-3 gap-3 px-7 mb-4 lg:mt-0 mt-4 rounded-lg justify-start">
                    <li class="h-8 rounded-lg bg-gray-300 w-1/12"></li>
                    <li class="h-8 rounded-lg bg-gray-300 w-1/12"></li>
                    <li class="h-8 rounded-lg bg-gray-300 w-1/12"></li>
                </ul>
                <div class="rounded-lg shadow-xl bg-gray-200 h-5/6 border flex flex-col justify-center relative w-full items-center py-8 px-10"></div>
            </main>
        </div>
    </div>
</template>

<style>
    body {
        position: relative;
    }

    nav {
        padding: .8rem
    }

    input[type="radio"]:checked+label {
        border-color: rgb(7 89 133);
    }
</style>

<script>
import axios from 'axios'
import isEmpty from 'lodash/isEmpty'
import jmoment from 'moment-jalaali'
import StarRating from 'vue-star-rating'
import CommentSection from '@/components/CommentSection.vue'
import DoctorsContainer from '@/components/DoctorsContainer.vue'
import OfficeAppointmentSection from '@/components/OfficeAppointmentSection.vue'

export default {
    name: "DoctorView",
    components: {
        DoctorsContainer,
        OfficeAppointmentSection,
        StarRating,
        CommentSection
    },
    setup() {
        return {
            jmoment,
            isEmpty
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
            appointment_time: null,
            loading: false,
            page: 1
        }
    },
    async beforeMount() {
        const username = this.$route.params.username
        this.loading = true
        try {
            const res = await axios.get(`/api/doctor/${username}`)
            this.$data.doctor = res.data
        } catch {
            console.error("non-existent user!")
        }
        this.loading = false
    },
}
</script>