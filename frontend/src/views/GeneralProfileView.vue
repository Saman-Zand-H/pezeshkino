<template>
    <div class="w-full h-full relative">
        <DoctorsContainer :breadcrumb="[{title: 'صفحه کاربری', url: {name: 'user'}}]" />
        <main class="flex lg:flex-row flex-col-reverse py-8 px-9 gap-8 h-full bg-slate-100/70">
            <div class="lg:w-3/4 w-full rounded-lg bg-white shadow-md px-4 py-3">
                <router-view></router-view>
            </div>
            <aside class="lg:w-1/4 w-full lg:sticky rounded-lg bg-white shadow-md px-4 py-3 h-fit">
                <div class="my-5 mx-3">
                    <div class="flex flex-row-reverse gap-5">
                        <div class="">
                            <img v-if="user.picture" :src="user.picture" class="w-[4.5rem] h-[4.5rem] overflow-hidden shadow-md rounded-full" alt="profile picture">
                            <div v-else class="text-xs rounded-full flex items-center justify-center bg-lime-900/80 text-white w-[4.5rem] h-[4.5rem]">
                                <span v-if="user.first_name && user.last_name">{{ user.first_name[0] }} {{ user.last_name[0] }}</span>
                            </div>
                        </div>
                        <router-link :to="{ name: 'profile_edit' }" class="flex flex-col gap-1.5">
                            <div class="flex flex-row-reverse items-center gap-2.5">
                                <span class="flex text-xl" v-if="user.first_name && user.last_name">
                                    {{ user.first_name }} {{ user.last_name }}
                                </span>
                                <i class="fa fa-pencil"></i>
                            </div>
                            <div class="text-xs">{{ user.phonenumber || "بدون شماره" }}</div>
                        </router-link>
                    </div><hr class="my-5">
                    <ul class="my-2 px-4 text-lg flex flex-col gap-9 py-4">
                        <li>
                            <router-link :to="{ name: 'profile_appointments' }" class="flex gap-3 items-center justify-end">
                                نوبت های من
                                <i class="fa fa-calendar-days"></i>
                            </router-link>
                        </li>
                    </ul>
                </div>
            </aside>
        </main>
    </div>
</template>

<script>
    import DoctorsContainer from '@/components/DoctorsContainer.vue'
    import { mapState, mapActions } from 'vuex'

    export default {
        name: 'GeneralProfileView',
        components: {
            DoctorsContainer
        },
        beforeCreate() {
            this.$store.dispatch("updateUserInfo")
            this.$store.dispatch("locations/fetchLocation")
        }, 
        async created() {
            await this.updateUserInfo()
        },
        computed: {
            ...mapState(["user"])
        },
        methods: {
            ...mapActions(["updateUserInfo"])
        }
    }
</script>