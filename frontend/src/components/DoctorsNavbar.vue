<template>
    <header class="w-full shadow-md bg-white z-[100] top-0 inset-x-0 transition-all duration-300">
        <div class="items-center flex flex-row justify-between">
            <div class="relative flex align-baseline items-center justify-between ms-12">
                <div class="flex space-x-3 items-center text-sky-800">
                    <img src="@/assets/logo.png" alt="logo" class="h-8 w-auto">
                </div>
            </div>

            <div class="flex">
                <nav>
                    <ul class="md:flex hidden lg:gap-20 gap-12 mx-5 flex-row-reverse flex-wrap items-center ms-20">
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
                                                <a 
                                                    href="#" 
                                                    :class="[dropdownActive ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-3 text-sm']"
                                                    >
                                                    تغییر مشخصات
                                                    <i class="fas fa-pencil px-2"></i>
                                                </a>
                                            </MenuItem>
                                            <MenuItem v-slot="{ dropdownActive }" class="py-4">
                                                <a 
                                                    href="#" 
                                                    :class="[dropdownActive ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-3 text-sm']"
                                                    >
                                                    پزشکان نشانگذاری شده
                                                    <i class="fas fa-bookmark px-2"></i>
                                                </a>
                                            </MenuItem>
                                            <MenuItem v-slot="{ dropdownActive }" class="py-4">
                                                <a 
                                                    href="#" 
                                                    :class="[dropdownActive ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-3 text-sm']"
                                                    >
                                                    قرار های ملاقات من
                                                    <i class="fa fa-calendar-days px-2"></i>
                                                </a>
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
                                class="navbar-link text-black hover:text-black/80"
                            >
                                صفحه نخست
                            </router-link>
                        </li>
                        <li>
                            <router-link 
                                :to="{ name: 'about' }" 
                                class="navbar-link text-black hover:text-black/80"
                            >
                                درباره ما
                            </router-link>
                        </li>
                        <li>
                            <router-link 
                                :to="{ name: 'doctors' }" 
                                class="navbar-link text-black hover:text-black/80"
                            >
                                پزشکان
                            </router-link>
                        </li>
                    </ul>
                    <ul class="md:hidden flex justify-end">
                        <li class="flex">
                            <button type="button" class="" @click="navCollapsed = !navCollapsed">
                                <i class="fas fa-bars text-xl"></i>
                            </button>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
        <ul :class="[navCollapsed ? 'h-0 overflow-hidden' : 'w-full px-12 py-10', 'bg-white transition-all duration-300 ease-out flex md:hidden flex-col']">
            <li v-if="isAuthenticated" class="border-y border-transparent hover:border-black hover:cursor-pointer transition-colors duration-200 ease-in py-8">
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
                            پزشکان نشانگذاری شده
                            <i class="fas fa-bookmark mx-2"></i>
                        </router-link>
                    </li>
                    <li class="border-y border-transparent hover:border-gray-300 hover:cursor-pointer transition-colors duration-200 ease-in py-8">
                        <router-link :to="{ name: 'home' }" class="w-full">
                            قرار های ملافات من
                            <i class="fa fa-calendar-days mx-2"></i>
                        </router-link>
                    </li>
                </ul>
            </li>
            <li v-else class="border-y border-transparent hover:border-black hover:cursor-pointer transition-colors duration-200 ease-in py-8">
                <router-link 
                    :to="{ name: 'home' }" 
                    class="navbar-link text-teal-950 font-bold"
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
                    :to="{ name: 'about' }" 
                    class="navbar-link text-teal-950 font-bold"
                >
                    درباره ما
                </router-link>
            </li>
            <li class="border-y border-transparent hover:border-black hover:cursor-pointer transition-colors duration-300 ease-in py-8">
                <router-link 
                    :to="{ name: 'doctors' }" 
                    class="navbar-link text-teal-950 font-bold"
                >
                    دکتر ها
                </router-link>
            </li>
        </ul>
    </header>
</template>

<script>
    import api from '@/_helpers/api'
    import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
    import { mapState } from 'vuex'

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
        computed: {
            ...mapState(['user'])
        },
        async created() {
            this.Authenticated = await this.isAuthenticated()
            if (this.Authenticated) {
                const data = await api.get("/dj-rest-auth/user")
                this.$store.dispatch("setUser", data.data)
            }
        },
        methods: {
            async isAuthenticated() {
                let accessToken = localStorage.getItem("access_token")
                if (accessToken === null) {
                    accessToken = "random"
                }
                const data = { token: accessToken }
                const res = await api.post("/dj-rest-auth/token/verify/", data)
                return res.status === 200
            }
        }
    }
</script>