import axios from 'axios'

export default {
    namespaced: true,
    state: {
        specialties: [],
        doctors: [],
        loading: false
    },
    getters: {
        getDisplayNames(state) {
            return state.specialties.map(v => { return v.display_name })
        }
    },
    mutations: {
        UPDATE_SPECIALTIES(state, data) {
            state.specialties = data
        },
        UPDATE_DOCTORS(state, data) {
            state.doctors = data
        },
        UPDATE_LOADING(state, data) {
            state.loading = data
        }
    },
    actions: {
        async fetchSpecialties({ commit }) {
            try {
                const res = await axios.get("/api/specialties")
                commit("UPDATE_SPECIALTIES", res.data)
            } catch {
                console.error("an error has happened while fetching data. refresh")
            }
        },
        async fetchDoctors({ commit }) {
            commit("UPDATE_LOADING", true)
            try {
                const res = await axios.get(
                    `/api/doctor?page=1&name_order=a`)
                commit("UPDATE_DOCTORS", res.data.results)
            } catch {
                console.error("something has gone wrong. please refresh.")
            }
            commit("UPDATE_LOADING", false)
        },
        async searchDoctors({ commit }, payload) {
            commit("UPDATE_LOADING", true)
            const searchStr = new URLSearchParams(payload.searchObj).toString()
            const page = payload.page ? payload.page : 1
            try {
                const res = await axios.get(`/api/doctor?page=${page}&${searchStr}`)
                commit('UPDATE_DOCTORS', res.data.results)
            } catch {
                console.error("something went wrong while fetching data. please refresh.")
            }
            commit("UPDATE_LOADING", false)
        }
    }
}