import axios from 'axios'

export default {
    namespaced: true,
    state: {
        specialties: [],
        doctors: [],
        loading: false,
        paginator: {}
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
        },
        UPDATE_PAGINATOR(state, data) {
            state.paginator = data
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
        async fetchDoctors({ commit }, page = 1) {
            commit("UPDATE_LOADING", true)
            try {
                const res = await axios.get(
                    `/api/doctor?page=${page}&name_order=a`)
                commit("UPDATE_DOCTORS", res.data.results)
                delete res.data.results
                commit("UPDATE_PAGINATOR", res.data)
            } catch {
                console.error("something has gone wrong. please refresh.")
            }
            commit("UPDATE_LOADING", false)
        },
        async searchDoctors({ commit }, payload) {
            commit("UPDATE_LOADING", true)
            for (let i in payload) {
                if (!payload[i]) delete payload[i]
            }
            const searchStr = new URLSearchParams(payload).toString()
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