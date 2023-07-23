<template>
    <div>
        <div class="grid grid-cols-1 md:grid-cols-2">
            <div class="" v-for="appointment in appointments">
                
            </div>
        </div>
    </div>
</template>

<script>
    import api from '@/_helpers/api'

    export default {
        name: 'AppointmentsDashboardView',
        data() {
            return {
                appointments: []
            }
        },
        async beforeCreate() {
            const url = "/api/doctor_appointments/"

        }
    }
</script>