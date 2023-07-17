<template>
    <main 
          class="w-full h-screen relative after:bg-contain after:fixed after:w-full after:h-full after:-z-10 after:top-0 after:left-0 after:brightness-50"
         >
        <HomeNavbar :isActive="isActive" @toggle-collapse="toggleCollapse" />

        <AlertMessage :alertType="alertType" :ttl="alertTTL" :isVisible="isAlertVisible" :msg="alertMsg" />

        <div :class="[isActive ? 'brightness-50 transition-all duration-300' : '', 'relative']">
            <section class="block absolute top-48 left-0 right-0">
                <form @submit.prevent="submitForm" method="POST" class="flex justify-center items-center">
                    <div class="bg-white mx-2 shadow-xl rounded-xl w-96 mb-48 lg:w-[38%] md:w-[50%] py-12 px-14 flex flex-col gap-10">
                        <h1 class="text-4xl font-sans leading-10 font-semibold">ورود</h1>
                        <ul>
                            <li class="text-red-500" v-for="error in fieldsErrors.general">{{ error }} -</li>
                        </ul>
                        <div class="text-right">
                            <label for="usernameField" class="font-semibold px-3">نام کاربری</label>
                            <input 
                                   id="usernameField"
                                   name="username"
                                   @keydown.enter="submitForm"
                                   type="text" 
                                   v-model="fieldValues.username"
                                   placeholder="نام کاربری خود را وارد کنید" 
                                   class="border-2 text-right invalid:text-red-500 invalid:ring-red-500 invalid:ring-2 invalid:ring-offset-1 invalid:border-red-500 shadow-md focus:border-2 w-full border-gray-500 mt-3.5 py-3 px-6 rounded-lg focus:ring-4 focus:ring-black transition-all duration-200" 
                                  />
                                <ul class="my-2 mx-3">
                                    <li class="text-red-500" v-for="error in fieldsErrors.username">{{ error }} -</li>
                                </ul>
                        </div>
                        <div class="text-right">
                            <label class="font-semibold px-3" for="passwordField">رمز عبور</label>
                            <input 
                                   id="passwordField" 
                                   name="password"
                                   @keydown.enter="submitForm"
                                   v-model="fieldValues.password"
                                   type="password" 
                                   placeholder="رمز عبور خود را وارد کنید" 
                                   class="border-2 text-right invalid:text-red-500 invalid:ring-red-500 invalid:ring-2 invalid:ring-offset-1 invalid:border-red-500 shadow-md focus:border-2 mt-3.5 w-full border-gray-500 py-3 px-6 rounded-lg focus:ring-4 focus:ring-black transition-all duration-200" 
                                  />
                                <ul class="my-2 mx-3">
                                    <li class="text-red-500" v-for="error in fieldsErrors.password">{{ error }} -</li>
                                </ul>
                        </div>
                        <button 
                                class="bg-black text-white w-[97%] h-12 mx-auto hover:bg-black/90 px-4 block py-2 rounded-lg -mt-1 shadow-lg" 
                                type="submit"
                               >
                            ورود
                        </button>
                        <hr>
                        <div class="flex justify-center items-center flex-col gap-3 text-xs">
                            <a href="#" class="block w-full hover:text-slate-900">
                                فراموشی رمزعبور
                            </a>
                            <span class="block w-full">یا</span>
                            <a href="#" class="block w-full hover:text-slate-900">
                                حساب کاربری جدید
                            </a>
                        </div>
                    </div>
                </form>
            </section>
        </div>
    </main>
</template>

<style scoped>
    main::after {
        background-image: url('@/assets/auth-bg.webp');
    }
</style>

<script>
    import { mapMutations, mapState, mapActions } from 'vuex'
    import AlertMessage from '@/components/AlertMessage.vue'
    import HomeNavbar from '@/components/HomeNavbar.vue'
    import HomeFooter from '@/components/HomeFooter.vue'

    export default {
        name: 'LoginView',
        data() {
            return {
                isActive: false,
                isAlertVisible: false,
                alertType: undefined,
                alertMsg: undefined,
                alertTTL: 2,
                fieldValues: {
                    username: null,
                    password: null
                },
                fieldsErrors: {
                    username: new Set(),
                    password: new Set(),
                    general: new Set()
                }
            }
        },
        components: {
            HomeNavbar,
            HomeFooter,
            AlertMessage
        },
        computed: {
            ...mapState(['user'])
        },
        methods: {
            toggleCollapse() {
                this.isActive = !this.isActive
            },
            ...mapActions(["login"]),
            ...mapMutations(["UPDATE_USER"]),
            async submitForm(e) {
                this.fieldsErrors.general.clear()
                this.fieldsErrors.password.clear()
                this.fieldsErrors.username.clear()

                if (this.formIsValid) {
                    try {
                        this.login(this.fieldValues)
                        this.$data.alertMsg = 'شما با موفقیت وارد شدید! در حال انتقال...'
                        this.$data.alertType = 'success'
                        this.$data.isAlertVisible = true
                        setTimeout(
                            () => this.$router.push({name: 'home'}), 
                            (Number(this.$data.alertTTL)+.5)*1000
                        )
                    } catch (error) {
                        if (error.response.status === 400) {
                            this.fieldsErrors.general.add("نام کاربری یا رمزعبور اشتباه میباشد")
                            // raise sweetalert
                            this.$swal.fire({
                                title: 'ورود ناموفق!',
                                text: 'نام کاربری یا رمزعبور اشتباه میباشد',
                                icon: 'error',
                                confirmButtonText: 'تلاش مجدد'
                            })
                        }
                    }
                } 
            },
            formIsValid() {
                if (!this.fieldValues.username) {
                    const msg = "نام کاربری نمیتواند خالی باشد"
                    this.fieldsErrors.username.add(msg)
                    document.getElementById('usernameField').setCustomValidity(msg)
                } else {
                    this.fieldsErrors.username.delete("نام کاربری نمیتواند خالی باشد")
                }
                if (!this.fieldValues.password) {
                    const msg = "رمزعبور نمیتواند خالی باشد"
                    this.fieldsErrors.password.add(msg)
                    document.getElementById('passwordField').setCustomValidity(msg)
                } else {
                    this.fieldsErrors.password.delete("رمزعبور نمیتواند خالی باشد")
                }
                if (this.fieldValues.password.length < 8) {
                    const msg = "رمزعبور باید حداقل 8 کاراکتر داشته باشد"
                    this.fieldsErrors.password.add(msg)
                    document.getElementById('passwordField').setCustomValidity('رمزعبور باید حداقل 8 کاراکتر داشته باشد')
                } else {
                    this.fieldsErrors.password.delete("رمزعبور باید حداقل 8 کاراکتر داشته باشد")
                }
                return (this.fieldsErrors.password.size === 0 
                        && this.fieldsErrors.username.size === 0)
            },
            handleClick(e) {
                if (
                    !(document.querySelector("#navSidebar").contains(e.target) 
                    || e.target.id === "navToggleMenuBtn")
                ) {
                    this.isActive = !this.isActive
                }
            } 
        },
        created() {
            if (document.body.scrollTop >= 30 || document.activeElement.scrollTop >= 30) {
                this.isActive = true
            }
        },
        updated() {
            if (this.isActive) {
                window.addEventListener('click', this.handleClick)
            }
        },
        beforeUnmount() {
            window.removeEventListener('click', this.handleClick)
        }
    }
</script>