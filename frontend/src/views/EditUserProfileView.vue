<template>
    <Teleport to="body">
        <AlertMessage 
                :isVisible="alert.alertVisible" 
                :alertType="alert.alertType" 
                :ttl="alert.alertTTL" 
                :msg="alert.alertMsg" />
    </Teleport>
    <div class="my-8 mx-5 px-3">
        <h1 class="text-3xl text-right">تغییر مشخصات</h1>
        <div>
            <div class="w-fit mx-auto">
                <input  @change="onImageChange" class="hidden absolute" id="picture_input" type="file">
                <label for="picture_input" class="hover:cursor-pointer w-fit z-0 relative mx-auto">
                    <div class="w-44 h-44 absolute flex items-center justify-center bg-slate-400/40 rounded-full z-0 hover:z-20">
                        <i class="text-white fa fa-pen text-3xl"></i>
                    </div>
                    <img 
                        v-if="user.picture" 
                        class="w-44 h-44 relative rounded-full z-10 hover:-z-20 overflow-hidden my-10" 
                        alt="profile picture" 
                        id="picture_image"
                        :src="picture.url"
                    >
                    <div v-else class="w-44 h-44 bg-lime-900/80 rounded-full z-10 hover:-z-20 overflow-hidden text-white">
                        <span v-if="user.first_name && user.last_name" class="flex justify-center items-center text-3xl">
                            {{ user.first_name[0] }} {{ user.last_name[0] }}
                        </span>
                    </div>
                </label>
            </div>
            <div class="px-3">
                <div class="flex flex-col md:flex-row gap-4 py-2 mt-4">
                    <div class="text-right w-full flex flex-col gap-2">
                        <label for="first_name_input">نام</label>
                        <input 
                                type="text"
                                v-model="formData.first_name"
                                id="first_name_input" 
                                class="w-full text-right rounded-lg outline-none focus:ring-sky-700 focus:ring-2 ring-1 ring-gray-400 h-14 px-5"
                            >
                    </div>
                    <div class="text-right w-full flex flex-col gap-2">
                        <label for="last_name_input">نام خانوادگی</label>
                        <input 
                                type="text" 
                                v-model="formData.last_name"
                                id="last_name_input" 
                                class="w-full text-right rounded-lg outline-none focus:ring-sky-700 focus:ring-2 ring-1 ring-gray-400 h-14 px-5"
                            >
                    </div>
                </div>

                <div class="flex flex-col md:flex-row gap-4 py-2 my-2">
                    <div class="text-right w-full flex flex-col gap-2">
                        <label for="username_input">نام کاربری</label>
                        <input 
                                type="text"
                                v-model="formData.username"
                                id="username_input" 
                                class="w-full text-right rounded-lg outline-none focus:ring-sky-700 focus:ring-2 ring-1 ring-gray-400 h-14 px-5"
                            >
                    </div>
                    <div class="text-right w-full flex flex-col gap-2">
                        <label for="gender_input">جنسیت</label>
                        <div class="select-container relative">
                            <select v-model="formData.gender" class="w-full h-14 hover:cursor-pointer rounded-lg px-5 text-right" id="gender_input">
                                <option value="female" :checked="user.gender === 'female' || true">زن</option>
                                <option :checked="user.gender === 'male'" value="male">مرد</option>
                                <option :checked="user.gender === 'justStupid'" value="justStupid">ترجیح میدهم نگویم</option>
                            </select>
                        </div>
                    </div>
                </div>

                <div class="flex flex-col md:flex-row-reverse gap-4 py-2 my-2 text-right">
                    <div class="text-right w-full flex flex-col gap-2">
                        <label for="provinceInput">انتخاب استان</label>
                        <div class="relative select-container w-full">
                            <select 
                                    @change="selectProvince"
                                    v-model="province" 
                                    id="provinceInput" 
                                    class="w-full h-14 hover:cursor-pointer rounded-lg px-5 text-right"
                                   >
                                <option value="">
                                    نامشخص
                                </option>
                                <option :value="ostan.id" v-for="ostan in getProvinces" :key="ostan.id">
                                    {{ ostan.name }}
                                </option>
                            </select>
                        </div>
                    </div>

                    <div class="text-right w-full flex flex-col gap-2">
                        <label for="cityInput">انتخاب شهر</label>
                        <div class="relative select-container w-full">
                            <select 
                                    id="cityInput" 
                                    v-model="formData.city_id"
                                    class="w-full h-14 hover:cursor-pointer rounded-lg px-5 text-right" 
                                   >
                                <option v-if="user.city" :value="user.city.id">{{ user.city.name }}</option>
                                <option v-else value="">نامشخص</option>
                            </select>
                        </div>
                    </div>
                </div>
                <button @click.prevent="onSubmit" class="w-full bg-sky-600 text-white rounded-xl text-xl mt-9 mb-4 py-3 shadow-md">
                    ذخیره
                </button>
            </div>
        </div>
    </div>
</template>

<style scoped>
    select {
        display: inline-flex;
        box-sizing: border-box;
        justify-content: space-between;
        appearance:inherit ;
        -moz-appearance: none;
        -webkit-appearance: none;
        text-align: right;
        padding-inline-end: 1.5rem;
        padding-inline-start: 2.5rem;
    }
    .select-container:after {
        content: "⮟";
        position:absolute;
        top: 16px;
        left: .8rem
    }
</style>

<script>
    import api from '@/_helpers/api'
    import AlertMessage from '@/components/AlertMessage.vue'
    import { mapState, mapGetters, mapActions } from 'vuex'
    
    export default {
        name: 'EditUserProfileView',
        components: {
            AlertMessage
        },
        beforeCreate() {
            this.$store.dispatch("updateUserInfo")
            this.$store.dispatch("locations/fetchLocation")
        },
        data() {
            const user = this.$store.state.user
            return {
                province: user.city ? user.city.province : null,
                picture: {url: user.picture},
                formData: {
                    first_name: user.first_name,
                    last_name: user.last_name,
                    gender: user.gender || "justStupid",
                    city_id: user.city ? user.city.id : null,
                    username: user.username,
                    picture: null
                },
                alert: {
                    alertType: 'danger',
                    alertMsg: '',
                    alertTTL: 3,
                    alertVisible: false
                }
            }
        },
        computed: {
            ...mapState(["locations", "user"]),
            ...mapGetters({getProvinces: "locations/getProvinces"}),
        },
        methods: {
            ...mapActions(["setUser"]),
            selectProvince(e) {
                const cities = this.locations.provinces_cities.find(v => v.id === Number.parseInt(e.target.value)).cities
                const selectElement = document.getElementById("cityInput")
                selectElement.innerHTML = ""
                let node;
                for (let i = 0; i < cities.length; i++) {
                    node = document.createElement("option")
                    node.text = cities[i].name
                    node.value = cities[i].id
                    this.formData.city_id = parseInt(node.value)
                    selectElement.appendChild(node)
                }
            },
            async onSubmit() {
                try {
                    if (!this.picture.file) {
                        console.log("it is null")
                        this.formData.picture = null
                    } else {
                        this.formData.picture = this.picture.file
                        console.log(this.formData.picture)
                    }
                    const formData = new FormData()

                    formData.append("first_name", this.formData.first_name)
                    formData.append("last_name", this.formData.last_name)
                    formData.append("username", this.formData.username)
                    formData.append("city_id", this.formData.city_id)
                    formData.append("gender", this.formData.gender)
                    formData.append("picture", this.formData.picture)
                    
                    const res = await api.patch("/dj-rest-auth/user/", formData, {
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'multipart/form-data'
                        }
                    })
                    this.setUser(res.data)
                    this.fireAlert("مشخصات شما با موفقیت تغییر یافت.", 3, "success")
                } catch {
                    this.fireAlert("مشکلی حین انجام عملیات پیش آمده‌است.")
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
            onImageChange(e) {
                const files = e.target.files
                if (files.length) {
                    const url = URL.createObjectURL(files[0])
                    this.picture = {
                        file: files[0],
                        url: url
                    }
                }
            }
        }
    }
</script>