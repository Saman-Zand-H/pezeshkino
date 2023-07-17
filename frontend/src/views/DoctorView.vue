<template>
    <div class="relative">
        <DoctorsContainer 
                :breadcrumb='[
                    {title: "پزشکان", url: {name: "doctors"}}, 
                    {title: `دکتر ${doctor.user.name}`, url: {name: "doctors", params: {username: this.$route.params.username}}}
                ]' 
            />

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
                        <OfficeAppointmentSection 
                            :doctor="doctor" 
                            :appointment_time="appointment_time" 
                            @appointmentChange="newVal => appointment_time=newVal" />
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

    input[type="radio"]:checked+label {
        border-color: rgb(7 89 133);
    }
</style>

<script>
import axios from 'axios'
import DoctorsContainer from '@/components/DoctorsContainer.vue'
import OfficeAppointmentSection from '@/components/OfficeAppointmentSection.vue'

export default {
    name: "DoctorView",
    components: {
        DoctorsContainer,
        OfficeAppointmentSection,
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