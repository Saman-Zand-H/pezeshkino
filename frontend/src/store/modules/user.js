import axios from 'axios'

export default {
    state: {
        username: null,
        first_name: null,
        last_name: null,
        user_type: null
    },
    getters: {
        get_usertype_display(state) {
            if (state.user_type === "D") {
                return "پزشک"
            } else if (state.user_type === "S") {
                return "منشی"
            } else {
                return "بیمار"
            }
        },
        async isAuthenticated(state) {
            if (localStorage.getItem("access_token") == null) {
                return false
            }
            const data = { token: localStorage.getItem("access_token") }
            try {
                const res = await axios.post("/dj-rest-auth/token/verify/", data)
                return res.status === 200
            } catch {
                return false
            }
        }
    },
    mutations: {
        UPDATE_USER(state, payload) {
            state.username = payload.username
            state.first_name = payload.first_name
            state.last_name = payload.last_name
            state.user_type = payload.user_type
        }
    },
    actions: {
        async login({ commit }, credentials) {
            const res = await axios.post('/dj-rest-auth/login/', credentials)
            if (res.status === 200) {
                const payload = res.data.user
                commit('UPDATE_USER', payload)
                localStorage.setItem('access_token', res.data.access_token)
                localStorage.setItem('refresh_token', res.data.refresh_token)
                return Promise.resolve()
            } else {
                localStorage.removeItem("access_token")
                localStorage.removeItem("refresh_token")
                commit('UPDATE_USER')
                return Promise.reject(`status: ${res.status}, error: ${res.data}`)
            }
        }
    }
}