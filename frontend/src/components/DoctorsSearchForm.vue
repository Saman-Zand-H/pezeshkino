<template>
    <div class="text-right flex flex-col gap-4 my-3">
        <span class="w-full text-right text-xl underline underline-offset-[1.4rem]">
            فیلتر ها
        </span>
        <div class="w-full border-b border-cyan-950/50 me-3"></div>
        <fieldset>
            <div class="mt-5 text-gray-600">
                <div class="relative select-container my-3">
                    <label for="provinceInput" class="text-sm">انتخاب استان</label>
                    <select 
                            @change="selectProvince" 
                            v-model="province" 
                            id="provinceInput" 
                            class="rounded-lg text-right w-full h-14 mt-1.5 shadow-lg hover:cursor-pointer"
                           >
                        <option v-for="ostan in getProvinces" :key="ostan">
                            {{ ostan }}
                        </option>
                    </select>
                </div>

                <div class="relative select-container my-3">
                    <label for="cityInput" class="text-sm">انتخاب شهر</label>
                    <select 
                            v-model="city"
                            id="cityInput" 
                            class="rounded-lg w-full h-14 mt-1.5 shadow-lg hover:cursor-pointer" 
                           >
                        <option value="">همه</option>
                    </select>
                </div>

                <div class="relative select-container my-3">
                    <label for="cityInput" class="text-sm">انتخاب تخصص</label>
                    <select 
                            v-model="specialty" 
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
                    </select>
                </div>

                <div class="relative my-3">
                    <label for="searchTermInput" class="text-sm">نام پزشک</label>
                    <input 
                           type="text" 
                           v-model="searchTerm" 
                           class="rounded-lg bg-slate-200/60 w-full px-4 h-14 mt-1.5 shadow-lg hover:cursor-text"
                           id="searchTermInput"
                          >
                </div>

                <button 
                        class="bg-cyan-950 hover:bg-cyan-950/90 text-white rounded-xl w-full py-3 flex justify-center gap-3 my-8" 
                        @click="performSearch"
                       >
                    <div>
                        <i class="fa fa-search"></i>
                    </div>
                    <div>
                        جستجو
                    </div>
                </button>
            </div>
        </fieldset>
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
    import { mapState, mapGetters } from 'vuex'

    export default {
        name: 'DoctorsSearchForm',
        data() {
            return {
                province: "",
                city: "",
                specialty: "",
                searchTerm: ""
            }
        },
        computed: {
            ...mapState(["locations", "doctors"]),
            ...mapGetters(
                { 
                    getProvinces: "locations/getProvinces",
                }
            )
        },
        mounted() {
            this.updateLocations()
            this.updateSpecialties()
        },
        methods: {
            updateLocations() {
                if (this.locations.provinces_cities.length === 0) {
                    this.$store.dispatch("locations/fetchLocation")
                }
            },
            updateSpecialties() {
                if (this.doctors.specialties.length === 0) {
                    this.$store.dispatch("doctors/fetchSpecialties")
                }
            },
            selectProvince(e) {
                const cities = this.locations.provinces_cities.find(v => v.name == e.target.value).cities
                const selectElement = document.getElementById("cityInput")
                selectElement.innerHTML = ""
                let node;
                for (let i = 0; i < cities.length; i++) {
                    node = document.createElement("option")
                    node.text = cities[i].name
                    node.value = cities[i].id
                    selectElement.appendChild(node)
                }
                const allCitiesNode = document.createElement("option")
                allCitiesNode.text = "همه"
                allCitiesNode.value = ""
                selectElement.appendChild(allCitiesNode)
            },
            performSearch(e) {
                e.preventDefault()
                const data = {
                    page: this.$route.params.page,
                    searchObj: {
                        city: this.$data.city,
                        specialty: this.$data.specialty,
                        search: this.$data.searchTerm
                    }
                }
                this.$store.dispatch("doctors/searchDoctors", data)
            }
        }
    }
</script>