<template>
    <div class="text-right flex flex-col gap-4 my-3">
        <button @click.prevent="this.isVisible = !this.isVisible" class="w-full md:cursor-default text-right text-xl underline underline-offset-[1.4rem]">
            فیلتر ها
        </button>
        <div class="w-full border-b border-cyan-950/50 me-3"></div>
        <Form @submit="performSearch" :validation-schema="formSchema" :class="[isVisible ? 'w-full max-h-[50rem] md:h-fit' : 'max-h-0 md:max-h-fit', 'duration-700 overflow-hidden transition-all']">
            <div class="mt-5 text-gray-600">
                <div class="relative select-container my-3">
                    <label for="provinceInput" class="text-sm">انتخاب استان</label>
                    <select
                            v-model="province" 
                            id="provinceInput" 
                            class="rounded-lg text-right w-full h-14 mt-1.5 shadow-lg hover:cursor-pointer"
                           >
                        <option value="">همه</option>
                        <option :value="ostan.id" v-for="ostan in getProvinces" :key="ostan.id">
                            {{ ostan.name }}
                        </option>
                    </select>
                </div>

                <div class="relative select-container my-3">
                    <label for="cityInput" class="text-sm">انتخاب شهر</label>
                    <Field as="select" 
                           name="city"
                           class="rounded-lg w-full h-14 mt-1.5 shadow-lg hover:cursor-pointer" 
                           >
                        <option :value="city.id" v-for="city in cities">
                            {{ city.name }}
                        </option>
                    </Field>
                    <ErrorMessage name="city" />
                </div>

                <div class="relative select-container my-3">
                    <label for="specialtyInput" class="text-sm">انتخاب تخصص</label>
                    <Field as="select"
                           name="specialty"
                           id="specialtyInput" 
                           class="rounded-lg w-full h-14 mt-1.5 shadow-lg hover:cursor-pointer" 
                           >
                        <option 
                                v-for="spec in doctors.specialties" 
                                :key="spec"
                                :value="spec.code_name"
                               >
                            {{ spec.display_name }}
                        </option>
                    </Field>
                    <ErrorMessage name="specialty" />
                </div>

                <div class="relative my-3">
                    <label for="searchTermInput" class="text-sm">نام پزشک</label>
                    <Field 
                           type="text" 
                           name="search"
                           class="rounded-lg bg-white w-full px-4 h-14 mt-1.5 shadow-lg hover:cursor-text"
                           id="searchTermInput"
                          />
                          <ErrorMessage name="search" />
                </div>

                <button 
                        class="bg-cyan-950 hover:bg-cyan-950/90 text-white rounded-xl w-full py-3 flex justify-center gap-3 my-8" 
                        type="submit"
                       >
                    <div>
                        <i class="fa fa-search"></i>
                    </div>
                    <div>
                        جستجو
                    </div>
                </button>
            </div>
        </Form>
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
        top: 45px;
        left: .8rem
    }
</style>

<script>
    import * as yup from 'yup'
    import { Form, Field, ErrorMessage } from 'vee-validate'
    import { mapState, mapGetters, mapActions } from 'vuex'

    export default {
        name: 'DoctorsSearchForm',
        data() {
            return {
                province: "",
                city: "",
                specialty: "",
                searchTerm: "",
                isVisible: true
            }
        },
        components: {
            Form,
            Field,
            ErrorMessage
        },
        computed: {
            ...mapState(["locations", "doctors"]),
            ...mapGetters(
                { 
                    getProvinces: "locations/getProvinces",
                }
            ),
            formSchema() {
                return {
                    search: yup.string(),
                    city: yup.string(),
                    specialty: yup.string().oneOf(this.doctors.specialties.map(v => v.code_name))
                }
            },
            cities() {
                if (!this.province) return []
                return this.locations.provinces_cities.find(v => v.id == this.province).cities
            }
        },
        async beforeMount() {
            await this.updateLocations()
            await this.updateSpecialties()
        },
        methods: {
            ...mapActions({fetchLocations: "locations/fetchLocation",
                           fetchSpecialties: "doctors/fetchSpecialties",
                           searchDoctors: "doctors/searchDoctors"}),
            async updateLocations() {
                if (this.locations.provinces_cities.length === 0) {
                    await this.fetchLocations()
                }
            },
            async updateSpecialties() {
                if (this.doctors.specialties.length === 0) {
                    await this.fetchSpecialties()
                }
            },
            performSearch(values) {
                this.searchDoctors(values)
            }
        },
    }
</script>