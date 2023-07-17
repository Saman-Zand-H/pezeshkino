import axios from 'axios'

export default {
    namespaced: true,
    state: {
        provinces_cities: []
    },
    getters: {
        getProvinces(state) {
            return state.provinces_cities.map(v => { return { name: v.name, id: v.id } })
        },
        getCities: (state) => (ostan_name) => {
            return state.provinces_cities.find(obj => obj.name === ostan_name)
        },
    },
    mutations: {
        updateLocations(state, payload) {
            state.provinces_cities = payload.data
        }
    },
    actions: {
        async fetchLocation({ commit }) {
            try {
                const res = await axios.get("/api/province")
                commit('updateLocations', { data: res.data })
            } catch {
                console.error("an error has happened while fetching data. refresh.")
            }
        }
    }
}