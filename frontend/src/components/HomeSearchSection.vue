<template>
    <section class="h-screen aspect-square">
        <div class="flex flex-col w-2/3 h-screen items-center justify-center mx-auto gap-8">
            <div class="text-slate-800">
                <h1 class="md:text-6xl text-5xl font-mono font-semibold">
                    Pezeshkino
                </h1>
            </div>
            <div class="flex flex-nowrap flex-col lg:flex-row w-full">
                <button
                    class="bg-slate-800 shadow-md rounded-t-xl lg:rounded-s-xl lg:rounded-e-none border border-slate-800 w-full lg:w-1/4 flex items-center justify-center gap-2 text-white hover:bg-slate-800/90 py-4"
                    @click="searchAll">
                    <i class="fas fa-search text-xl"></i>
                    جستجو
                </button>
                <select
                    class="shadow-md border-x lg:border-x-0 lg:border-y border-slate-800 p-4 bg-white w-full lg:w-1/4 hover:cursor-pointer"
                    @change="selectProvince" v-model="province" name="province">
                    <option class="text-right" value="">استان</option>
                    <option v-for="ostan in getProvinces" :value="ostan.id" :key="ostan.id" class="text-right">
                        {{ ostan.name }}
                    </option>
                </select>
                <select id="shahrSelect"
                    class="text-right border-x shadow-md lg:border-x-0 lg:border-y w-full lg:w-1/4 border-slate-800 p-4 bg-white hover:cursor-pointer"
                    v-model="city" name="city">
                    <option value="">شهر</option>
                </select>
                <input
                    class="text-right p-4 border shadow-md lg:border-e-0 lg:border-t border-t-0 w-full lg:w-1/4 rounded-xl rounded-t-none bg-white lg:rounded-s-xl lg:rounded-e-none border-slate-800"
                    type="text" style="direction: rtl;" placeholder="نام پزشک، تخصص..." name="searchText"
                    v-model="searchText">
            </div>
        </div>
    </section>
</template>

<style scoped>
    section {
        background-image: url('../assets/hhholographic.jpeg');
    }
</style>

<script>
    import { mapState, mapGetters } from 'vuex'

    export default {
        name: 'HomeSearchSection',
        data() {
            return {
                province: "",
                city: "",
                searchText: ""
            }
        },
        methods: {
            updateLocation() {
                if (this.locations.provinces_cities.length === 0) {
                    this.$store.dispatch("locations/fetchLocation")
                }
            },
            selectProvince(e) {
                const cities = this.locations.provinces_cities.find(v => v.id == e.target.value).cities
                const selectElement = document.getElementById("shahrSelect")
                selectElement.innerHTML = ""
                let node;
                for (let i = 0 ; i < cities.length ; i++) {
                    node = document.createElement("option")
                    node.text = cities[i].name
                    node.value = cities[i].id
                    selectElement.appendChild(node)
                }
            },
            searchAll() {
                const query = {}
                if (this.searchText) query["search"] = this.searchText
                if (this.city) query["city"] = this.city
                this.$router.push({
                    path: 'doctors',
                    query: query
                })
            }
        },
        computed: {
            ...mapState(["locations"]),
            ...mapGetters({getProvinces: "locations/getProvinces"})
        },
        beforeMount() {
            if (this.locations.provinces_cities.length === 0) {
                this.$store.dispatch("locations/fetchLocation")
            }
        }
    }
</script>