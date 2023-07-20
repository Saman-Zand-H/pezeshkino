<template>
    <Teleport to="body">
        <AlertMessage :isVisible="alert.alertVisible" :alertType="alert.alertType" :ttl="alert.alertTTL" :msg="alert.alertMsg" />
    </Teleport>

    <div class="bg-slate-100 pb-3 relative w-full h-full">
        <DoctorsContainer
            :breadcrumb='[
                {title: "پزشکان", url: {name: "doctors"}}, 
                {title: `دکتر ${doctor.user.name}`, url: {name: "doctor", params: {username: this.$route.params.username}}},
                {title: "ثبت نظر", url: {name: "new_review", params: {username: this.$route.params.username}}}
            ]'
         />
        <div class="bg-white flex flex-col mx-auto gap-3 rounded-lg w-2/3 lg:w-1/2 my-8 py-7 px-6 shadow-lg">
            <span class="self-end">
                <h2 class="text-lg flex flex-row gap-5 items-center">
                    ثبت نظر برای دکتر {{ doctor.user.name }}
                    <i class="fa fa-user-doctor"></i>
                </h2>
            </span>
            <div class="text-right text-sm px-10" style="direction:rtl">
                <small>
                    نظر شما برای دیگر بیماران مهم است و به آن ها کمک می کند برای درمان بیماری خود، پزشک بهتری را انتخاب کنند.
                </small>
            </div>
            <div class="flex flex-col my-3 gap-5">
                <div style="direction:rtl" class="text-right px-2">
                    <span>1. آیا این پزشک را به دیگران پیشنهاد میدهید؟</span>
                    <div class="flex flex-row justify-center gap-3 my-6">
                        <input type="radio" name="suggests_doctor" :value="true" v-model="review.suggests_doctor" id="suggests_doctor_true" class="hidden">
                        <label for="suggests_doctor_true" class="rounded-lg hover:cursor-pointer flex items-center gap-2 border hover:border-slate-800 transition-colors duration-150 py-3 px-6">
                            بله
                            <i class="fa fa-thumbs-up"></i>
                        </label>
                        <input type="radio" name="suggests_doctor" :value="false" v-model="review.suggests_doctor" id="suggests_doctor_false" class="hidden">
                        <label for="suggests_doctor_false" class="rounded-lg hover:cursor-pointer flex items-center gap-2 border hover:border-slate-800 transition-colors duration-150 py-3 px-6">
                            خیر
                            <i class="fa fa-thumbs-down"></i>
                        </label>
                    </div>
                </div>
                <div style="direction:rtl" class="text-right px-2">
                    <span>2. برای درمان چه بیماری ای به پزشک مراجعه کردید؟</span>
                    <div class="my-3 mx-2">
                        <input v-model="review.illness" type="text" placeholder="نام بیماری" class="w-full text-sm focus:border-slate-800 focus:text-slate-800 border rounded-lg py-3 px-4">
                    </div>
                </div>
                <div style="direction:rtl" class="text-right px-2">
                    <span>3. نتیجه درمان شما چگونه بود؟</span>
                    <div class="my-3 mx-2">
                        <div class="my-2 flex flex-col gap-3 text-sm">
                            <label for="treatment_t" class="rounded-lg hover:cursor-pointer py-4 hover:border-slate-700 transition-colors duration-150 px-5 w-full inline-flex items-center gap-3 border">
                                <input v-model="review.treatment_result" name="treatment_result" type="radio" value="T" id="treatment_t">
                                درمان شدم
                            </label>
                            <label for="treatment_nt" class="rounded-lg hover:cursor-pointer py-4 hover:border-slate-700 transition-colors duration-150 px-5 w-full inline-flex items-center gap-3 border">
                                <input v-model="review.treatment_result" name="treatment_result" type="radio" value="NT" id="treatment_nt">
                                درمان نشدم
                            </label>
                            <label for="treatment_p" class="rounded-lg hover:cursor-pointer py-4 hover:border-slate-700 transition-colors duration-150 px-5 w-full inline-flex items-center gap-3 border">
                                <input v-model="review.treatment_result" name="treatment_result" type="radio" value="P" id="treatment_p">
                                درحال درمان هستم
                            </label>
                            <label for="treatment_c" class="rounded-lg hover:cursor-pointer py-4 hover:border-slate-700 transition-colors duration-150 px-5 w-full inline-flex items-center gap-3 border">
                                <input v-model="review.treatment_result" name="treatment_result" type="radio" value="C" id="treatment_c">
                                درمان را ناتمام گذاشتم
                            </label>
                            <label for="treatment_o" class="rounded-lg hover:cursor-pointer py-4 hover:border-slate-700 transition-colors duration-150 px-5 w-full inline-flex items-center gap-3 border">
                                <input v-model="review.treatment_result" name="treatment_result" type="radio" value="O" id="treatment_o">
                                سایر
                            </label>
                        </div>
                    </div>
                </div>
                <div style="direction:rtl" class="text-right px-2">
                    <span>4. لطفا تجربه درمان خود را از ویزیت پزشک بنویسید</span>
                    <div class="my-3 mx-2">
                        <textarea v-model="review.review" class="resize-y text-sm w-full py-3 px-4 rounded-xl border" style="direction:rtl" placeholder="اینجا بنویسید..."></textarea>
                    </div>
                </div>
                <div style="direction:rtl" class="text-right px-2">
                    <span>5. به موارد زیر بر اساس تجربیات خود پاسخ دهید</span>
                    <div class="my-3 mx-2">
                        <div class="flex flex-row-reverse justify-evenly my-3">
                            <span>5: بیشترین</span>
                            <span>1: کمترین</span>
                        </div>
                        <div class="my-8 flex flex-col items-center">
                            <h3 class="text-lg">برخورد مناسب پزشک</h3>
                            <div class="flex gap-3 my-3">
                                <input v-model="review.behavior_score" type="radio" name="behavior_score" class="hidden" value="1" id="behavior_score_1">
                                <label for="behavior_score_1" class="aspect-square hover:border-slate-700 transition-colors duration-150 hover:cursor-pointer rounded-full py-1 px-3 border">1</label>

                                <input v-model="review.behavior_score" type="radio" name="behavior_score" class="hidden" value="2" id="behavior_score_2">
                                <label for="behavior_score_2" class="aspect-square hover:border-slate-700 transition-colors duration-150 hover:cursor-pointer rounded-full py-1 px-3 border">2</label>

                                <input v-model="review.behavior_score" type="radio" name="behavior_score" class="hidden" value="3" id="behavior_score_3">
                                <label for="behavior_score_3" class="aspect-square hover:border-slate-700 transition-colors duration-150 hover:cursor-pointer rounded-full py-1 px-3 border">3</label>

                                <input v-model="review.behavior_score" type="radio" name="behavior_score" class="hidden" value="4" id="behavior_score_4">
                                <label for="behavior_score_4" class="aspect-square hover:border-slate-700 transition-colors duration-150 hover:cursor-pointer rounded-full py-1 px-3 border">4</label>

                                <input v-model="review.behavior_score" type="radio" name="behavior_score" class="hidden" value="5" id="behavior_score_5">
                                <label for="behavior_score_5" class="aspect-square hover:border-slate-700 transition-colors duration-150 hover:cursor-pointer rounded-full py-1 px-3 border">5</label>
                            </div>
                        </div>
                        <div class="my-8 flex flex-col items-center">
                            <h3 class="text-lg">توضیح پزشک در هنگام ویزیت</h3>
                            <div class="flex gap-3 my-3">
                                <input v-model="review.elaboration_score" type="radio" name="elaboration_score" class="hidden" value="1" id="elaboration_score_1">
                                <label for="elaboration_score_1" class="aspect-square hover:border-slate-700 transition-colors duration-150 hover:cursor-pointer rounded-full py-1 px-3 border">1</label>

                                <input v-model="review.elaboration_score" type="radio" name="elaboration_score" class="hidden" value="2" id="elaboration_score_2">
                                <label for="elaboration_score_2" class="aspect-square hover:border-slate-700 transition-colors duration-150 hover:cursor-pointer rounded-full py-1 px-3 border">2</label>

                                <input v-model="review.elaboration_score" type="radio" name="elaboration_score" class="hidden" value="3" id="elaboration_score_3">
                                <label for="elaboration_score_3" class="aspect-square hover:border-slate-700 transition-colors duration-150 hover:cursor-pointer rounded-full py-1 px-3 border">3</label>

                                <input v-model="review.elaboration_score" type="radio" name="elaboration_score" class="hidden" value="4" id="elaboration_score_4">
                                <label for="elaboration_score_4" class="aspect-square hover:border-slate-700 transition-colors duration-150 hover:cursor-pointer rounded-full py-1 px-3 border">4</label>

                                <input v-model="review.elaboration_score" type="radio" name="elaboration_score" class="hidden" value="5" id="elaboration_score_5">
                                <label for="elaboration_score_5" class="aspect-square hover:border-slate-700 transition-colors duration-150 hover:cursor-pointer rounded-full py-1 px-3 border">5</label>
                            </div>
                        </div>
                        <div class="my-8 flex flex-col items-center">
                            <h3 class="text-lg">مهارت و تخصص پزشک</h3>
                            <div class="flex gap-3 my-3">
                                <input v-model="review.skills_score" type="radio" name="skills_score" class="hidden" value="1" id="skills_score_1">
                                <label for="skills_score_1" class="aspect-square hover:border-slate-700 transition-colors duration-150 hover:cursor-pointer rounded-full py-1 px-3 border">1</label>

                                <input v-model="review.skills_score" type="radio" name="skills_score" class="hidden" value="2" id="skills_score_2">
                                <label for="skills_score_2" class="aspect-square hover:border-slate-700 transition-colors duration-150 hover:cursor-pointer rounded-full py-1 px-3 border">2</label>

                                <input v-model="review.skills_score" type="radio" name="skills_score" class="hidden" value="3" id="skills_score_3">
                                <label for="skills_score_3" class="aspect-square hover:border-slate-700 transition-colors duration-150 hover:cursor-pointer rounded-full py-1 px-3 border">3</label>

                                <input v-model="review.skills_score" type="radio" name="skills_score" class="hidden" value="4" id="skills_score_4">
                                <label for="skills_score_4" class="aspect-square hover:border-slate-700 transition-colors duration-150 hover:cursor-pointer rounded-full py-1 px-3 border">4</label>

                                <input v-model="review.skills_score" type="radio" name="skills_score" class="hidden" value="5" id="skills_score_5">
                                <label for="skills_score_5" class="aspect-square hover:border-slate-700 transition-colors duration-150 hover:cursor-pointer rounded-full py-1 px-3 border">5</label>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="flex justify-start px-3">
                    <button type="button" @click.prevent="onSubmit" class="border border-sky-700 text-sky-800 rounded-xl w-full py-2 hover:text-white hover:bg-sky-700 transition-colors duration-150">
                        ثبت
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
    label:has(> input[name="treatment_result"]:checked),
    input[type="radio"]:checked+label {
        border-color: rgb(30 41 59);
    }
</style>

<script>
    import axios from 'axios'
    import api from '@/_helpers/api'
    import AlertMessage from '@/components/AlertMessage.vue'
    import DoctorsContainer from '@/components/DoctorsContainer.vue'

    export default {
        name: 'ReviewView',
        components: {
            DoctorsContainer,
            AlertMessage
        },
        data() {
            return {
                doctor: {
                    user: {
                        name: ""
                    },
                },
                review: {
                    suggests_doctor: true,
                    illness: "",
                    treatment_result: "O",
                    review: "",
                    behavior_score: "5",
                    elaboration_score: "5",
                    skills_score: "5",
                    doctor: NaN
                },
                alert: {
                    alertType: 'success',
                    alertMsg: '',
                    alertTTL: 3,
                    alertVisible: false
                }
            }
        },
        async beforeCreate() {
            const username = this.$route.params.username
            try {
                const res = await axios.get(`/api/doctor/${username}`)
                this.$data.doctor = res.data
            } catch (error){
                console.error(error)
            }
        },
        methods: {
            async onSubmit(e) {
                try {                                    
                    this.review.doctor = this.doctor.id                                                
                    await api.post("/api/review/", this.review)
                    this.fireAlert("نظر شما با موفقیت ثبت شد", 3,"success")
                    this.$router.push({name: "doctor", params: {username: this.doctor.user.username}})
                } catch {
                    this.fireAlert("مشکلی حین ثبت نظر پیش آمد")
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
        }
    }
</script>