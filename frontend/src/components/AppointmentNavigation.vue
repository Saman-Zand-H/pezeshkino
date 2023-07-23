<template>
    <div class="w-full flex flex-row-reverse gap-7">
        <div class="my-5 ms-auto pe-5 w-32">
            <swiper
                :mousewheel="true"
                :modules="modules"
                :direction="'vertical'"
                :slides-per-view="4"
                :space-between="-40"
                :scrollbar="{ draggable: true }"
            >
                <swiper-slide :key="date" v-for="(date, time_obj) in available_times">
                    <input 
                        type="radio" 
                        name="appointment_day"
                        :value="time_obj" 
                        :id="time_obj" 
                        class="hidden"
                    >
                    <label 
                        class="rounded-lg border hover:border-sky-600 hover:cursor-pointer text-center focus:border-sky-600 transition-colors duration-300 shadow-md py-4 px-5 text-lg" 
                        type="button" 
                        :for="time_obj"
                        @click="this.$data.date=time_obj"
                    >
                        <h1 class="">{{ moment(time_obj).format('dddd') }}</h1>
                        <small class="text-sm">{{ moment(time_obj).format("jYYYY/jMM/jDD") }}</small>
                    </label>
                </swiper-slide>
            </swiper>
        </div>
        <div v-if="date" class="w-full py-5 my-5 px-7 h-[450px] flex flex-row rounded-lg border gap-4">
            <div 
                v-for="time in available_times[date]"
                :key="[time.date, 'T', time.time, office_id].join('')"
               >
                <input 
                       name="appointment_btn" 
                       @input="this.$parent.$emit('appointmentChange', $event.target.value.split(',')); $event.target.checked = true" 
                       :value="[[date, 'T', time.time].join(''), Number(office_id)]" 
                       class="hidden" 
                       type="radio" 
                       :id="['appointment', time.date, time.time, office_id].join('').replaceAll(':', '-')"
                       :checked="$el.value === appointment_time"
                    >
                <label 
                        :for="['appointment', time.date, time.time, office_id].join('').replaceAll(':', '-')" 
                        class="rounded-lg border hover:border-sky-600 hover:cursor-pointer focus:border-sky-600 transition-color duration-200 shadow-sm py-3 px-4 h-[3.2rem]"
                    >
                    {{ moment(time.time, "HH:mm:ss").format("HH:mm") }}
                </label>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .swiper {
        height: 450px;
        width: 120px;
    }
    
    input[type="radio"]:checked+label {
        border-color: rgb(7 89 133);
    }
</style>

<script>
    import 'swiper/css'
    import axios from 'axios'
    import 'swiper/css/scrollbar'
    import groupBy from 'lodash/groupBy'
    import moment from 'moment-jalaali'
    import fa from 'moment/locale/fa'
    import { Scrollbar, Mousewheel } from 'swiper/modules'
    import { Swiper, SwiperSlide } from 'swiper/vue'

    export default {
        name: 'AppointmentNavigation',
        components: {
            Swiper,
            SwiperSlide
        },
        emits: {
            appointmentChange: Array
        },
        props: {
            office_id: Number,
            appointment_time: Array
        },
        data() {
            return {
                date: ''
            }
        },
        async setup(props, context) {
            let available_times = {}

            moment.updateLocale("fa", fa)
            moment.loadPersian({dialect: 'persian-modern'})

            try {
                const res = await axios.post("/api/get_free_times/", {office_id: props.office_id})
                available_times = res.data
            } catch (error) {
                console.error("something went wrong while catching appointment data. " + error)
            }

            if (available_times.length > 0) {
                available_times = groupBy(available_times, 'date')
            }
            return {
                modules: [Scrollbar, Mousewheel],
                available_times: available_times,
                moment: moment
            }
        }
    }
</script>
