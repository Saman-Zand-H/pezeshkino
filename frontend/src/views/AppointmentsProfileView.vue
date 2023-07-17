<template>
    <div class="mt-8 mb-2 mx-8 text-end">
        <h1 class="text-3xl">نوبت ها</h1>
    </div>
    <div class="w-full text-end flex border-b-2 border-slate-200 flex-row justify-end pt-5 text-lg my-2">
        <button @click.prevent="appointmentType = 'doctor'" :class="[appointmentType === 'doctor'  ? 'border-indigo-600' : 'border-slate-200', 'w-full md:w-fit px-2 pb-2 border-b-2 hover:border-indigo-600/50 hover:text-slate-950/70 hover:cursor-pointer']" v-if="user.user_type === 'D'">
            درخواست ها
        </button>
        <button @click.prevent="appointmentType = 'patient'" :class="[appointmentType === 'patient' ? 'border-indigo-600' : 'border-slate-200', 'w-full md:w-fit px-2 pb-2 border-b-2 hover:border-indigo-600/50 hover:text-slate-950/70 hover:cursor-pointer']">
            نوبت ها
        </button>
    </div>
    <div class="py-2 w-full">
        <div v-if="appointmentType === 'patient'">
            <Suspense>
                <template #default>
                    <AppointmentsList :appointmentType="appointmentType" />
                </template>
            </Suspense>
        </div>
        <div v-else>
            <Suspense>
                <template #default>
                    <AppointmentsList :appointmentType="appointmentType" />
                </template>
            </Suspense>
        </div>
    </div>
</template>

<script>
    import AppointmentsList from '@/components/AppointmentsList.vue'
    import { mapState } from 'vuex'

    export default {
        name: 'AppointmentsProfileView',
        data() {
            return {
                appointmentType: 'patient'
            }
        },
        components: {
            AppointmentsList
        },
        computed: {
            ...mapState(["user"])
        }
    }
</script>