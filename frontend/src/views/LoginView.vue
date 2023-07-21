<template>
    <Teleport to="body">
        <AlertMessage :isVisible="alert.alertVisible" :alertType="alert.alertType" :ttl="alert.alertTTL" :msg="alert.alertMsg" />
    </Teleport>

    <section class="block absolute top-48 left-0 right-0">
        <Form @submit="submitForm" :validation-schema="form_schema" class="flex justify-center items-center">
            <div class="bg-white mx-2 shadow-xl rounded-xl w-96 mb-48 lg:w-[38%] md:w-[50%] py-12 px-14 flex flex-col gap-10">
                <h1 class="text-4xl font-sans leading-10 font-semibold">ورود</h1>
                <div class="text-right">
                    <label form="username_field">نام کاربری</label>
                    <Field id="username_field" placeholder="نام کاربری خود را وارد کنید" class="border-2 text-right invalid:text-red-500 invalid:ring-red-500 invalid:ring-2 invalid:ring-offset-1 invalid:border-red-500 shadow-md focus:border-2 w-full border-gray-500 mt-3.5 py-3 px-6 rounded-lg focus:ring-4 focus:ring-black transition-all duration-200" name="username" type="text" />
                    <ErrorMessage class="text-xs text-red-500" name="username" />
                </div>
                <div class="text-right">
                    <label for="password_field">رمزعبور</label>
                    <Field id="password_field" placeholder="رمز عبور خود را وارد کنید" type="password" name="password" class="border-2 text-right invalid:text-red-500 invalid:ring-red-500 invalid:ring-2 invalid:ring-offset-1 invalid:border-red-500 shadow-md focus:border-2 mt-3.5 w-full border-gray-500 py-3 px-6 rounded-lg focus:ring-4 focus:ring-black transition-all duration-200" />
                    <ErrorMessage class="text-xs text-red-500" name="password" />
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
                    <router-link :to="{ name: 'signup' }" class="block w-full hover:text-slate-900">
                        حساب کاربری جدید
                    </router-link>
                </div>
            </div>
        </Form>
    </section>
</template>

<script>
    import { Field, Form, ErrorMessage } from 'vee-validate'
    import { mapActions } from 'vuex'
    import * as yup from 'yup'
    import AlertMessage from '@/components/AlertMessage.vue'

    export default {
        name: 'LoginView',
        components: {
            Field,
            Form,
            ErrorMessage,
            AlertMessage
        },
        data() {
            return {
                alert: {
                    alertType: 'success',
                    alertMsg: '',
                    alertTTL: 3,
                    alertVisible: false
                },
            }
        },
        methods: {
            ...mapActions(["login"]),
            async submitForm(values) {
                try {
                    await this.login(values)
                    this.fireAlert(
                        "شما با موفقیت وارد شدید! در حال انتقال...",
                        2,
                        "success"
                    )
                    setTimeout(
                        () => this.$router.push({ name: 'home' }),
                        (Number(this.alert.alertTTL) + .5) * 1000
                    )
                } catch {
                    this.$swal.fire({
                        title: '!ورود ناموفق',
                        text: 'نام کاربری یا رمزعبور اشتباه میباشد',
                        icon: 'error',
                        confirmButtonText: 'تلاش مجدد'
                    })
                }
            },
            fireAlert(msg, ttl = 3, type = "danger") {
                this.alert.alertVisible = true
                this.alert.alertTTL = ttl
                this.alert.alertType = type
                this.alert.alertMsg = msg                  
                setTimeout(
                    () => {
                        this.alert.alertVisible = false
                    },
                    ttl * 1000
                )
            },
        },
        setup() {
            return {
                form_schema: yup.object({
                    username: yup.string().required("پر کردن نام کاربری ضروری است").min(2).max(100).strict(),
                    password: yup.string().required("پر کردن رمزعبور ضروری است").min(8).max(128).strict()
                })
            }
        }
    }
</script>