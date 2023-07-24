<template>
    <div>
        <!-- todo:add office will be added soon.. -->
        <div class="my-2 rounded-xl flex flex-col gap-5 items-end bg-white py-6 px-8" v-for="office in offices">
            <span class=""><h1 class="text-2xl font-semibold">{{ office?.office_title }}</h1></span>
            <div class="flex flex-col gap-2 items-end">
                <span>
                    آدرس
                    :
                    {{ office?.address }}
                </span>
                <span>
                    تلفن تماس
                    :
                    {{ office?.phonenumber }}
                </span>
                <span>
                    شهر
                    :
                    {{ office?.city.name }}
                </span>
            </div>
            <OfficeMap :office="office" :element_id="office.id" />
        </div>
    </div>
</template>

<script>
    import api from '@/_helpers/api'
    import OfficeMap from '@/components/OfficeMap.vue'

    export default {
        name: 'OfficesDashboardView',
        data() {
            return {
                offices: null
            }
        },
        components: {
            OfficeMap
        },
        async beforeMount() {
            const url = '/api/doctor_offices/'
            const res = await api.get(url)

            if (res.status === 200) this.offices = res.data
        }
    }
</script>