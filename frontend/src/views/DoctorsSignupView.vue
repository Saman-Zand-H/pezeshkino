<template>
    <Teleport to="body">
        <AlertMessage :isVisible="alert.alertVisible" :alertType="alert.alertType" :ttl="alert.alertTTL" :msg="alert.alertMsg" />
    </Teleport>

    <section class="block absolute top-48 left-0 right-0">
        <Form @submit="submitForm" :validation-schema="form_schema" class="flex justify-center items-center">
            <div class="bg-white mx-2 shadow-xl rounded-xl w-2/3 mb-48 lg:w-[52%] py-12 px-14 flex flex-col gap-10">
                <h1 class="text-4xl font-sans leading-10 font-semibold">ثبت نام</h1>
                <div class="flex flex-col gap-4">
                    <div class="text-right">
                        <label form="username_field">نام کاربری</label>
                        <Field id="username_field" placeholder="نام کاربری خود را وارد کنید" class="border-2 text-right invalid:text-red-500 invalid:ring-red-500 invalid:ring-2 invalid:ring-offset-1 invalid:border-red-500 shadow-md focus:border-2 w-full border-gray-500 mt-3.5 py-3 px-6 rounded-lg focus:ring-4 focus:ring-black transition-all duration-200" name="username" type="text" />
                        <ErrorMessage style="direction: rtl" class="text-xs text-right text-red-500" name="username" />
                    </div>
                    <div class="flex flex-col md:flex-row-reverse gap-4">
                        <div class="text-right">
                            <label for="password_field">رمزعبور</label>
                            <Field id="password_field" placeholder="رمز عبور خود را وارد کنید" type="password" name="password1" class="border-2 text-right invalid:text-red-500 invalid:ring-red-500 invalid:ring-2 invalid:ring-offset-1 invalid:border-red-500 shadow-md focus:border-2 mt-3.5 w-full border-gray-500 py-3 px-6 rounded-lg focus:ring-4 focus:ring-black transition-all duration-200" />
                            <ErrorMessage class="text-xs text-red-500" name="password1" />
                        </div>
                        <div class="text-right">
                            <label for="password2_field">تایید رمزعبور</label>
                            <Field id="password2_field" placeholder="رمز عبور خود را وارد مجددا کنید" type="password" name="password2" class="border-2 text-right invalid:text-red-500 invalid:ring-red-500 invalid:ring-2 invalid:ring-offset-1 invalid:border-red-500 shadow-md focus:border-2 mt-3.5 w-full border-gray-500 py-3 px-6 rounded-lg focus:ring-4 focus:ring-black transition-all duration-200" />
                            <ErrorMessage class="text-xs text-red-500" name="password2" />
                        </div>
                    </div>
                    <div class="flex flex-col md:flex-row-reverse gap-4">
                        <div class="text-right">
                            <label for="first_name_field">نام</label>
                            <Field id="first_name_field" placeholder="نام خود را وارد مجددا کنید" type="text" name="first_name" class="border-2 text-right invalid:text-red-500 invalid:ring-red-500 invalid:ring-2 invalid:ring-offset-1 invalid:border-red-500 shadow-md focus:border-2 mt-3.5 w-full border-gray-500 py-3 px-6 rounded-lg focus:ring-4 focus:ring-black transition-all duration-200" />
                            <ErrorMessage class="text-xs text-red-500" name="first_name" />
                        </div>
                        <div class="text-right">
                            <label for="last_name_field">نام خانوادگی</label>
                            <Field id="last_name_field" placeholder="نام خانوادگی خود را وارد مجددا کنید" type="text" name="last_name" class="border-2 text-right invalid:text-red-500 invalid:ring-red-500 invalid:ring-2 invalid:ring-offset-1 invalid:border-red-500 shadow-md focus:border-2 mt-3.5 w-full border-gray-500 py-3 px-6 rounded-lg focus:ring-4 focus:ring-black transition-all duration-200" />
                            <ErrorMessage class="text-xs text-red-500" name="last_name" />
                        </div>
                    </div>
                    <div class="text-right">
                        <label for="upin_field">شماره نظام پزشکی</label>
                        <Field type="string" id="upin_field" name="upin" placeholder="شماره نظام پزشکی خود را وارد کنید" class="border-2 text-right invalid:text-red-500 invalid:ring-red-500 invalid:ring-2 invalid:ring-offset-1 invalid:border-red-500 shadow-md focus:border-2 mt-3.5 w-full border-gray-500 py-3 px-6 rounded-lg focus:ring-4 focus:ring-black transition-all duration-200" />
                        <ErrorMessage name="upin" class="text-xs text-red-500" />
                    </div>
                    <div class="text-right">
                        <label for="specialty_field">تخصص</label>
                        <Field as="select" name="specialty" id="specialty_field" class="rounded-xl border-slate-500 border-2 mt-3.5 text-right px-3 w-full h-12">
                            <option v-for="specialty in doctors.specialties" :value="specialty.code_name">
                                {{ specialty.display_name }}
                            </option>
                        </Field>
                        <ErrorMessage class="text-xs text-red-500" name="specialty" />
                    </div>
                    <div class="text-right">
                        <label for="gender_field">جنسیت</label>
                        <Field as="select" name="gender" id="gender_field" value="justStupid" class="rounded-xl border-slate-500 border-2 mt-3.5 text-right px-3 w-full h-12">
                            <option value="female">زن</option>
                            <option value="male">مرد</option>
                            <option value="justStupid">ترجیح میدهم نگویم</option>
                        </Field>
                        <ErrorMessage class="text-xs text-red-500" name="gender" />
                    </div>
                </div>
                <button 
                        class="bg-black text-white w-[97%] h-12 mx-auto hover:bg-black/90 px-4 block py-2 rounded-lg -mt-1 shadow-lg" 
                        >
                    ثبت نام
                </button>
                <hr>
                <div class="flex justify-center items-center flex-col gap-3 text-xs">
                    <a href="#" class="block w-full hover:text-slate-900">
                        فراموشی رمزعبور
                    </a>
                    <span class="block w-full">یا</span>
                    <router-link :to="{ name: 'login' }" class="block w-full hover:text-slate-900">
                        ورود
                    </router-link>
                </div>
            </div>
        </Form>
    </section>
</template>

<script>
    import { Field, Form, ErrorMessage } from 'vee-validate'
    import { mapActions, mapState } from 'vuex'
    import * as yup from 'yup'
    import AlertMessage from '@/components/AlertMessage.vue'

    export default {
        name: 'SignupView',
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
            ...mapActions(["signupDoctor", "doctors/fetchSpecialties"]),
            async submitForm(values, actions) {
                values.user_type = "D"
                try {
                    await this.signupDoctor(values)
                    this.fireAlert(
                        "شما با موفقیت ثبت‌نام شدید! در حال انتقال...",
                        3,
                        "success"
                    )
                    setTimeout(
                        () => this.$router.push({ name: 'home' }),
                        (Number(this.alert.alertTTL) + .5) * 1000
                    )
                } catch (error) {
                    console.log(error)
                    actions.setErrors(error.response.data)
                    this.$swal.fire({
                        title: '!ثبت‌نام ناموفق',
                        text: 'مقادیر وارد شده نامعتبر اند',
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
        async beforeCreate() {
            await this.$store.dispatch("doctors/fetchSpecialties")
        },
        computed: {
            ...mapState(["doctors"]),
            form_schema() {
                return yup.object({
                    username: yup
                                .string()
                                .strict()
                                .required("پر کردن نام کاربری ضروری است")
                                .min(2)
                                .max(100),
                    password1: yup
                                .string()
                                .strict()
                                .required("پر کردن رمزعبور ضروری است")
                                .min(8).max(128),
                    password2: yup
                                .string()
                                .strict()
                                .required("پر کردن رمزعبور ضروری است")
                                .min(8).max(128).oneOf([yup.ref("password1")], "رمز ها با هم مطابت ندارند"),
                    first_name: yup
                                .string()
                                .strict()
                                .required("پر کردن نام ضروری است")
                                .min(2).max(20),
                    last_name: yup
                                .string()
                                .strict()
                                .required("پر کردن نام خانوادگی ضروری است")
                                .min(2).max(20),
                    gender: yup
                                .string()
                                .required("انتخاب جنسیت ضروری است")
                                .strict().oneOf(["male", "female", "justStupid"]),
                    upin: yup
                                .number()
                                .required("پر کردن شماره نظام پزشکی ضروری است"),
                    specialty: yup
                                .string()
                                .required("انتخاب تخصص ضروری است")
                                .oneOf(
                                    this.doctors.specialties.map(v => {return v.code_name}), 
                                    "تخصص مورد نظر یافت نشد"
                                )
                })
            }
        }
    }
</script>