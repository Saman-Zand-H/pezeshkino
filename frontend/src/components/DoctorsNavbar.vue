<template>
    <header class="w-full shadow-md bg-white z-[100] top-0 inset-x-0 transition-all duration-300">
        <div class="items-center flex flex-row justify-between">
            <div class="relative flex align-baseline items-center justify-between ms-12">
                <div class="flex space-x-3 items-center text-sky-800">
                    <img src="@/assets/logo.png" alt="logo" class="h-8 w-auto">
                </div>
            </div>

            <nav>
                <ul class="md:flex hidden lg:gap-14 gap-12 mx-5 flex-row-reverse flex-wrap items-center ms-20">
                    <li v-if="Authenticated" class="relative">
                        <Menu as="div" class="relative inline-block text-right">
                            <div>
                                <MenuButton class="inline-flex w-full justify-center gap-x-1.5 rounded-lg bg-white px-3 py-2">
                                    <i class="fa fa-user text-lg"></i>
                                </MenuButton>
                            </div>

                            <transition 
                                enter-active-class="transition duration-200" 
                                enter-form-class="transform opacity-0 scale-95" 
                                enter-to-class="transform opacity-100 scale-100" 
                                leave-active-class="transition ease-in duration-75" 
                                leave-from-class="transform opacity-100 scale-100" 
                                leave-to-class="transform opacity-0 scale-95"
                                >
                                <MenuItems class="absolute right-0 z-50 mt-2 w-60 origin-top-right rounded-md bg-white shadow-sm ring-1 ring-slate-400">
                                    <div class="py-3 text-center">
                                        <MenuItem v-slot="{ dropdownActive }" class="py-4">
                                            <router-link
                                                :to="{ name: 'profile_edit' }"
                                                :class="[dropdownActive ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-3 text-sm']"
                                                >
                                                تغییر مشخصات
                                                <i class="fas fa-pencil px-2"></i>
                                            </router-link>
                                        </MenuItem>
                                        <MenuItem v-slot="{ dropdownActive }" class="py-4">
                                            <router-link
                                                :to="{ name: 'profile_appointments' }"
                                                :class="[dropdownActive ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-3 text-sm']"
                                                >
                                                نوبت های من
                                                <i class="fa fa-calendar-days px-2"></i>
                                            </router-link>
                                        </MenuItem>
                                        <MenuItem v-if="user.user_type === 'D'" v-slot="{ dropdownActive }" class="py-4">
                                            <router-link
                                                :to="{ name: 'doctor_dashboard_home' }"
                                                :class="[dropdownActive ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-3 text-sm']"
                                                >
                                                داشبورد
                                                <i class="fa fa-dashboard px-2"></i>
                                            </router-link>
                                        </MenuItem>
                                        <MenuItem v-slot="{ dropdownActive }" class="py-4">
                                            <button
                                                type="button"
                                                @click.prevent="logOut"
                                                :class="[dropdownActive ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'inline-block px-4 py-3 text-sm']"
                                                >
                                                خروج
                                                <i class="fa fa-sign-out px-2"></i>
                                            </button>
                                        </MenuItem>
                                    </div>
                                </MenuItems>
                            </transition>
                        </Menu>
                    </li>
                    <li v-else>
                        <router-link :to="{ name: 'login' }" class="border py-2 px-4 rounded-2xl hover:border-gray-400 transition-colors duration-200 ease-in">
                            ورود / ثبت نام
                        </router-link>
                    </li>
                    <li>
                        <router-link 
                            :to="{ name: 'home' }" 
                            class="navbar-link rounded-3xl text-black transition-colors duration-200 hover:bg-gray-200 p-4"
                        >
                            صفحه نخست
                        </router-link>
                    </li>
                    <li>
                        <router-link 
                            :to="{ name: 'doctors' }" 
                            class="navbar-link rounded-3xl text-black transition-colors duration-200 hover:bg-gray-200 p-4"
                        >
                            پزشکان
                        </router-link>
                    </li>
                </ul>
                <ul class="md:hidden flex justify-end">
                    <li class="flex">
                        <button type="button" class="" @click.prevent="navCollapsed = !navCollapsed">
                            <i class="fas fa-bars text-xl"></i>
                        </button>
                    </li>
                </ul>
            </nav>
        </div>
        <ul :class="[navCollapsed ? 'h-0 overflow-hidden' : 'w-full px-12 py-10', 'bg-white transition-all duration-300 ease-out flex md:hidden flex-col']">
            <li v-if="Authenticated" class="border-y border-transparent hover:border-black hover:cursor-pointer transition-colors duration-200 ease-in py-8">
                <button type="button" @click="profileNavCollapsed = !profileNavCollapsed" class="w-full">
                    {{ user.first_name }} {{ user.last_name }}
                    <i class="fa fa-user text-lg mx-2"></i> 
                </button>
                <ul :class="[profileNavCollapsed ? 'h-0 overflow-hidden' : 'w-full px-12 py-10', 'bg-white transition-all duration-300 ease-out text-sm flex flex-col']">
                    <li class="border-y border-transparent hover:border-gray-300 hover:cursor-pointer transition-colors duration-200 ease-in py-8">
                        <router-link :to="{ name: 'home' }" class="w-full">
                            تغییر مشخصات
                            <i class="fas fa-pen mx-2"></i>
                        </router-link>
                    </li>
                    <li class="border-y border-transparent hover:border-gray-300 hover:cursor-pointer transition-colors duration-200 ease-in py-8">
                        <router-link :to="{ name: 'home' }" class="w-full">
                            نوبت های من
                            <i class="fa fa-calendar-days mx-2"></i>
                        </router-link>
                    </li>
                    <li v-if="user.user_type === 'D'" class="border-y border-transparent hover:border-gray-300 hover:cursor-pointer transition-colors duration-200 ease-in py-8">
                        <router-link :to="{ name: 'doctor_dashboard_home' }" class="w-full">
                            داشبورد
                            <i class="fa fa-dashboard mx-2"></i>
                        </router-link>
                    </li>
                    <li class="border-y border-transparent hover:border-gray-300 hover:cursor-pointer transition-colors duration-200 ease-in py-8">
                        <button type="button" @click="logOut" class="w-full">
                            خروج
                            <i class="fa fa-sign-out mx-2"></i>
                        </button>
                    </li>
                </ul>
            </li>
            <li v-else class="border-y border-transparent hover:border-black hover:cursor-pointer transition-colors duration-200 ease-in py-8">
                <router-link 
                    :to="{ name: 'login' }" 
                    class="navbar-link text-teal-950 font-bold w-full h-full"
                >
                    ورود / ثبت نام
                </router-link>
            </li>
            <li class="border-y border-transparent hover:border-black hover:cursor-pointer transition-colors duration-200 ease-in py-8">
                <router-link 
                    :to="{ name: 'home' }" 
                    class="navbar-link text-teal-950 font-bold"
                >
                    صفحه نخست
                </router-link>
            </li>
            <li class="border-y border-transparent hover:border-black hover:cursor-pointer transition-colors duration-300 ease-in py-8">
                <router-link 
                    :to="{ name: 'doctors' }" 
                    class="navbar-link text-teal-950 font-bold"
                >
                    پزشکان
                </router-link>
            </li>
        </ul>
    </header>
</template>

<script>
    import AuthManager from '@/_helpers/auth'
    import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
    import { mapState, mapActions } from 'vuex'

    export default {
        name: "DoctorNavbar",
        components: {
            Menu,
            MenuButton,
            MenuItem,
            MenuItems
        },
        data() {
            return {
                navCollapsed: true,
                Authenticated: undefined,
                profileNavCollapsed: true,
                dropdownActive: false
            }
        },
        methods: {
            ...mapActions(["logout", "updateUserInfo"]),
            logOut(e) {
                const swalConf = {
                    title: 'آیا اطمینان دارید که میخواهید از حساب کاربری خود خارج شوید؟',
                    showDenyButton: true,
                    confirmButtonText: 'بله',
                    denyButtonText: "خیر",
                    customClass: {
                        denyButton: "bg-red-500",
                        confirmButton: "bg-green-500"
                    }
                }
                const swalVal = this.$swal.fire(swalConf)
                swalVal.then(result => {
                    if (result.isConfirmed) {
                        this.logout()
                        this.$router.push({name: "home"})
                        this.Authenticated = false
                        this.$swal.fire({title: 'با موفقیت خارج شدید', icon: "success"})
                    }
                })
            }
        },
        computed: {
            ...mapState(['user'])
        },
        async created() {
            await this.updateUserInfo()
            this.Authenticated = await AuthManager.isAuthenticated()
        },
        async updated() {
            this.updateUserInfo()
            this.Authenticated = await AuthManager.isAuthenticated()
        }
    }
</script>