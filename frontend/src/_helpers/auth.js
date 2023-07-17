import api from './api'
import axios from 'axios'

class AuthManager {
    async login(credentials) {
        localStorage.removeItem("user_info")
        localStorage.removeItem("access_token")
        localStorage.removeItem("refresh_token")

        try {
            const res = await axios.post("/api/token/", credentials)

            localStorage.setItem("access_token", res.data.access)
            localStorage.setItem("refresh_token", res.data.refresh)
            localStorage.setItem("user_info", JSON.stringify(res.data.user))
            return Promise.resolve(res)
        } catch {
            return Promise.reject()
        }
    }

    async isAuthenticated() {
        const access_token = localStorage.getItem("access_token")
        const refresh_token = localStorage.getItem("refresh_token")
        if (access_token == null || refresh_token == null) {
            return false
        }
        try {
            const res = await api.post(
                "/api/token/verify/", {
                    token: access_token
                }
            )
            return res.status === 200
        } catch {
            return false
        }
    }
}

export default new AuthManager()