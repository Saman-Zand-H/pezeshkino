<template>
    <div :class="[success ? 'bg-teal-400' : 'bg-red-400', 'flex relative justify-center items-center h-screen']">
        <div class="lg:w-1/3 w-2/3 bg-white gap-2 flex flex-col rounded-md shadow-lg py-6 px-4 my-9">
            <div v-if="!success">
                <div class="w-fit h-fit mx-auto mt-6">
                    <i class="fa fa-circle-exclamation text-7xl my-3"></i>
                    <h2 class="text-2xl">
                        پرداخت ناموفق
                    </h2>
                </div>
                <div class="my-2">
                    <small v-if="trackId" class="text-xs">
                        درصورت اطمینان از صحت پرداخت برای پیگیری لطفا کد {{ trackId }} را به همکاران ما در بخش پشتیبانی گزارش دهید
                    </small>
                </div>
            </div>
            <div v-else>
                <div class="w-fit h-fit mx-auto mt-6">
                    <i class="fa fa-check-circle text-7xl my-3"></i>
                    <h2 class="text-2xl">
                        پرداخت ناموفق
                    </h2>
                </div>
                <div class="my-2">
                    <small v-if="trackId" class="text-xs">
                        پرداخت شما با موفقیت در تاریخ و زمان {{ jmoment(paid_at, "YYYY-MM-DDTHH:mm:ss").format("dddd jD jMMMM jYYYY  ساعت HH:mm") }} با کد رهگیری {{ reference_number }} تکمیل شد
                    </small>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import api from '@/_helpers/api'
    import moment from 'moment'
    import fa from 'moment/locale/fa'
    import jmoment from 'moment-jalaali'

    export default {
        name: 'PaymentStatusView',
        data() {
            return {
                success: false,
                paid_at: "",
                reference_number: "",
                amount: NaN,
                currency: "",
                trackId: ""
            }
        },
        async beforeCreate() {
            const requiredQueryParams = ["trackId"]
            const urlParams = Object.keys(this.$route.query)
            if (!requiredQueryParams.every(i => urlParams.includes(i))) {
                this.success = false
            }
            try {
                const res = await api.post(
                    '/api/transaction/validate/', 
                    {
                        trackId: this.$route.query.trackId
                    }
                )
                this.success = true
                this.paid_at = res.data.payment_time
                this.reference_number = res.data.reference_number,
                this.amount = res.data.amount,
                this.currency = res.data.get_currency_display,
                this.trackId = this.$route.query.trackId
            } catch {
                this.success = false
                this.trackId = this.$route.query.trackId
            }
        },
        setup() {
            moment.locale("fa", fa)
            jmoment.loadPersian()
            return {
                jmoment
            }
        }
    }
</script>