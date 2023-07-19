import api from '@/_helpers/api'
import AuthManager from '@/_helpers/auth'

export default {
    state: {
        username: "",
        first_name: "",
        last_name: "",
        user_type: "",
        picture: "",
        city: "",
        gender: ""
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
        }
    },
    mutations: {
        UPDATE_USER(state, payload) {
            state.username = payload.username
            state.first_name = payload.first_name
            state.last_name = payload.last_name
            state.user_type = payload.user_type
            state.picture = payload.picture
            state.city = payload.city
            state.gender = payload.gender
        }
    },
    actions: {
        async login({ commit }, credentials) {
            try {
                const res = await AuthManager.login(credentials)
                commit("UPDATE_USER", JSON.parse(localStorage.getItem("user_info")))
                return res
            } catch {
                commit("UPDATE_USER")
                return Promise.reject()
            }
        },
        setUser({ commit }, data) {
            commit("UPDATE_USER", data)
            localStorage.setItem("user_info", JSON.stringify(data))
        },
        async updateUserInfo({ commit }) {
            const user_info = localStorage.getItem("user_info")
            if (user_info != null) {
                commit("UPDATE_USER", JSON.parse(user_info))
            } else {
                try {
                    const res = await api.get("/dj-rest-auth/user/")
                    commit("UPDATE_USER", res.data)
                    localStorage.setItem("user_info", JSON.stringify(res.data))
                } catch { commit("UPDATE_USER", {}) }
            }
        }
    }
}