<template>
    <header id="homeNavHeader" class="fixed w-full overflow-hidden bg-transparent z-[100] top-0 inset-x-0 transition-all duration-300 text-black">
        <div class="w-full">
            <div class="items-center">
                <div class="relative flex align-baseline items-center justify-between ms-12">
                    <div class="flex space-x-3 items-center">
                        <img src="@/assets/logo.png" alt="logo" class="h-8 w-auto" />
                        <span class="text-sm leading-10 font-sans sr-only">Vue</span>
                    </div>

                    <div class="lg:block">
                        <nav id="homeNavbar">
                            <ul class="lg:flex flex-row flex-wrap items-baseline space-x-10 hidden">
                                <li>
                                    <router-link :to="{ name: 'home' }" class="navbar-link rounded-3xl text-black transition-colors duration-200 hover:bg-gray-300/40 p-2">
                                        صفحه نخست
                                    </router-link>
                                </li>
                                <li>
                                    <router-link :to="{ name: 'doctors' }" class="navbar-link rounded-3xl text-black transition-colors duration-200 hover:bg-gray-300/40 p-2">
                                        پزشکان
                                    </router-link>
                                </li>
                                <li v-if="!Authenticated">
                                    <router-link :to="{ name: 'doctor_signup' }" class="navbar-link rounded-3xl text-black transition-colors duration-200 hover:bg-gray-300/40 p-2">
                                        ثبت نام برای پزشکان
                                    </router-link>
                                </li>
                                <li v-if="!Authenticated">
                                    <router-link :to="{ name: 'login' }" class="navbar-link rounded-3xl text-black transition-colors duration-200 hover:bg-gray-300/40 p-2">
                                        ورود / ثبت نام
                                    </router-link>
                                </li>
                                <li v-else>
                                    <router-link :to="{ name: 'user' }" class="navbar-link rounded-3xl text-black transition-colors duration-200 hover:bg-gray-300/40 p-2">
                                        <i class="fa fa-user text-xl"></i>
                                    </router-link>
                                </li>
                                <li v-else>
                                    <button type="button" @click.prevent="logOut" class="navbar-link rounded-3xl text-black transition-colors duration-200 hover:bg-gray-300/40 p-2">
                                        خروج
                                        <i class="fa fa-sign-out text-xl"></i>
                                    </button>
                                </li>
                            </ul>
                            <ul class="lg:hidden flex flex-row flex-wrap items-baseline">
                                <li>
                                    <button id="navToggleMenuBtn" class="font-semibold hover:underline" type="button" @click="$emit('toggle-collapse')">
                                        <i id="navToggleBurger" class="fa fa-bars text-xl"></i>
                                    </button>
                                </li>
                            </ul>
                        </nav>
                    </div>
                </div>
            </div>
        </div>
        <div 
             id="navSidebar"
             v-show="isActive"
             class="w-full md:w-[400px] md:block lg:hidden fixed z-[100] bg-black transition-all ease-in-out duration-300 h-screen mr-0 overflow-hidden right-0 top-0 bottom-0">
            <div class="transition-all duration-500 h-full flex flex-col overflow-y-auto text-white">
                <div class="flex justify-end font-semibold mr-12 mt-7 hover:underline focus:underline">
                    <button @click="$emit('toggle-collapse')">Close</button>
                </div>
                
                <ul class="mt-[8rem] text-xl leading-9 font-semibold flex flex-col px-5 text-left">
                    <li class="border-t border-white py-2 ps-1 flex">
                        <router-link :to="{ name: 'home' }">
                            صفحه نخست
                        </router-link>
                        <div class="ml-auto"><i class="fas fa-long-arrow-right"></i></div>
                    </li>
                    <li class="border-t border-white py-2 ps-1 flex">
                        <router-link :to="{ name: 'doctors' }">
                            پزشکان
                        </router-link>
                        <div class="ml-auto"><i class="fas fa-long-arrow-right"></i></div>
                    </li>
                    <li v-if="Authenticated" class="border-t border-b border-white py-2 ps-1 flex">
                        <router-link :to="{ name: 'user' }">
                            {{ user.first_name }} {{ user.last_name }}
                            <i class="fa fa-user"></i> 
                        </router-link>
                        <div class="ml-auto"><i class="fas fa-long-arrow-right"></i></div>
                    </li>
                    <li v-if="!Authenticated" class="border-t border-b border-white py-2 ps-1 flex">
                        <router-link :to="{ name: 'doctor_signup' }">
                            ورود / ثبت ثبت نام برای پزشکان
                        </router-link>
                        <div class="ml-auto"><i class="fas fa-long-arrow-right"></i></div>
                    </li>
                    <li v-if="!Authenticated" class="border-t border-b border-white py-2 ps-1 flex">
                        <router-link :to="{ name: 'login' }">
                            ورود / ثبت نام
                        </router-link>
                        <div class="ml-auto"><i class="fas fa-long-arrow-right"></i></div>
                    </li>
                    <li v-else class="border-t border-b border-white py-2 ps-1 flex">
                        <button type="button" @click.prevent="logOut">
                            خروج
                            <i class="fa fa-sign-out"></i> 
                        </button>
                        <div class="ml-auto"><i class="fas fa-long-arrow-right"></i></div>
                    </li>
                </ul>
            </div>
        </div>
    </header>
</template>

<script>
    import { mapActions, mapState } from 'vuex'
    import AuthManager from '@/_helpers/auth'

    export default {
        name: 'HomeNavbar',
        data() {
            return {
                Authenticated: undefined
            }
        },
        computed: {
            ...mapState(["user"])
        },
        props: {
            isActive: Boolean
        },
        async beforeMount() {
            await this.updateUserInfo()
            this.Authenticated = await AuthManager.isAuthenticated()
        },
        async updated() {
            this.Authenticated = await AuthManager.isAuthenticated()
        },
        mounted() {
            window.addEventListener('scroll', this.navScrolled)
        },
        beforeUnmount() {
            window.removeEventListener('scroll', this.navScrolled)
        },
        emits: ["toggle-collapse"],
        methods: {
            ...mapActions(["updateUserInfo", "logout"]),
            navScrolled(e) {
                if (document.body.scrollTop >= 30 || document.documentElement.scrollTop >= 30) {
                    document.querySelector("#homeNavHeader").classList.remove("bg-transparent", "text-black")
                    document.querySelectorAll(".navbar-link").forEach(el => el.classList.remove("text-black"))
                    document.querySelectorAll(".navbar-link").forEach(el => el.classList.add("text-white"))
                    document.querySelector("#homeNavHeader").classList.add("bg-black", "text-white")
                }
                else {
                    document.querySelector("#homeNavHeader").classList.remove("bg-black", "text-white")
                    document.querySelectorAll(".navbar-link").forEach(el => el.classList.remove("text-white"))
                    document.querySelectorAll(".navbar-link").forEach(el => el.classList.add("text-black"))
                    document.querySelector("#homeNavHeader").classList.add("bg-transparent", "text-black")
                }
            },
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
                        this.Authenticated = false
                        this.$swal.fire({title: 'با موفقیت خارج شدید', icon: "success"})
                    }
                })
            }
        }
    }
</script>

<style scoped>
    .router-link-active.router-link-exact-active {
        color: white;
        background-color: black;
        padding: 9px 13px;
        border-radius: 5rem;
    }
</style>
