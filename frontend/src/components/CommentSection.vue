<template>
    <div class="flex bg-white flex-col gap-5 px-3 items-end border-t py-4" v-for="review in reviews">
        <div class="flex flex-row-reverse items-center gap-3 px-3">
            <div class="rounded-full bg-lime-800 text-white flex items-center justify-center text-xl w-14 aspect-square">
                {{ review.by_user.first_name[0] }}
            </div>
            <div class="flex flex-col text-sm items-end">
                <div class="">
                    <span v-if="review.by_user.visited" class="rounded-2xl inline-flex items-center justify-center bg-slate-300/60 px-2.5 py-1 text-center text-xs text-slate-500">
                        ویزیت شده
                    </span>
                    {{ review.by_user.first_name }}
                </div>
                <div class="">
                    {{ jmoment(review.update_at).format("jYYYY/jMM/jD") }}
                </div>
            </div>
        </div>
        <div class="px-3">
            <span class="flex flex-row-reverse gap-3 text-green-800" v-if="review.suggests_doctor">
                <i class="fa fa-thumbs-up text-xl"></i>
                پزشک را توصیه میکنم
            </span>
            <span class="flex flex-row-reverse gap-3 text-orange-500" v-else>
                <i class="fa fa-thumbs-down text-xl"></i>
                پزشک را توصیه نمیکنم
            </span>
        </div>
        <div class="px-3 text-xs">
            <b>علت مراجعه</b> : {{ review.illness }}
        </div>
        <div class="px-2 mb-2 text-base text-right" style="direction:rtl">
            {{ review.review }}
        </div>
    </div>
</template>

<script>
    import moment from 'moment'
    import fa from 'moment/locale/fa'
    import jmoment from 'moment-jalaali'

    export default {
        name: 'CommentSection',
        data() {
            return {
                page: 1
            }
        },
        setup() {
            moment.updateLocale("fa", fa)
            jmoment.loadPersian({dialect: 'persian-modern', usePersianDigits: true})
            return {
                moment,
                jmoment
            }
        },
        props: {
            reviews: Array
        }
    }
</script>