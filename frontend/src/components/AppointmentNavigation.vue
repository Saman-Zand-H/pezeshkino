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
                    <button 
                        class="rounded-lg border hover:border-sky-600 focus:border-sky-600 transition-colors duration-300 shadow-md py-4 px-5 text-lg" 
                        type="button" 
                        @click.prevent="this.$data.date=time_obj"
                    >
                        <h1 class="">{{ moment(time_obj).format('dddd') }}</h1>
                        <small class="text-sm">{{ moment(time_obj).format("jYYYY/jMM/jDD") }}</small>
                    </button>
                </swiper-slide>
            </swiper>
        </div>
        <div v-if="date" class="w-full py-5 my-5 px-7 h-[450px] flex flex-row rounded-lg border gap-4">
            <div 
                v-for="time in available_times[date]" 
                :key="time.time" 
                class="rounded-lg border hover:border-sky-600 focus:border-sky-600 transition-color duration-200 shadow-sm py-3 px-4 h-[3.2rem]"
               >
                <button 
                        class="hover:cursor-pointer" 
                        type="button" 
                        @click.prevent="$emit('show-confirm')" 
                        @focusout="$emit('hide-confirm')"
                    >
                    {{ moment(time.time, "HH:mm:ss").format("HH:mm") }}
                </button>
            </div>
        </div>
    </div>
</template>

<style>
    .swiper {
        height: 450px;
        width: 120px;
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
        emits: ['show-confirm', 'hide-confirm'],
        props: {
            office_id: {type: Number, default: 6}
        },
        data() {
            return {
                date: ''
            }
        },
        async setup(props, context) {
            let available_times = {}

            moment.locale("fa", fa)
            moment.loadPersian()

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
