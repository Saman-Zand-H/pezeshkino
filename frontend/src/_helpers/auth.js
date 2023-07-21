import api from './api'
import axios from 'axios'

class AuthManager {
    async login(credentials) {
        localStorage.removeItem("user_info")
        localStorage.removeItem("access_token")
        localStorage.removeItem("refresh_token")

        const res = await axios.post(
            "/api/token/",
            credentials, {
                headers: {
                    'Accept-Language': 'fa-ir'
                }
            }
        )
        if (res.status === 200) {
            localStorage.setItem("access_token", res.data.access)
            localStorage.setItem("refresh_token", res.data.refresh)
            localStorage.setItem("user_info", JSON.stringify(res.data.user))
            return Promise.resolve(res)
        }
        return Promise.reject(res)
    }

    async signup(credentials) {
        localStorage.removeItem("user_info")
        localStorage.removeItem("access_token")
        localStorage.removeItem("refresh_token")

        const res = await axios.post(
            "/dj-rest-auth/registration/",
            credentials, {
                headers: {
                    'Accept-Language': 'fa-ir'
                }
            }
        )

        if (res.status !== 201) {
            return Promise.reject(res)
        }

        localStorage.setItem("access_token", res.data.access_token)
        localStorage.setItem("refresh_token", res.data.refresh_token)
        localStorage.setItem("user_info", JSON.stringify(res.data.user))
        return Promise.resolve(res)
    }

    async signupDoctor(credentials) {
        localStorage.removeItem("user_info")
        localStorage.removeItem("access_token")
        localStorage.removeItem("refresh_token")

        const res = await axios.post(
            "/api/register/doctor/",
            credentials, {
                headers: {
                    'Accept-Language': 'fa-ir'
                }
            }
        )

        if (res.status !== 201) {
            return Promise.reject(res)
        }

        localStorage.setItem("access_token", res.data.access_token)
        localStorage.setItem("refresh_token", res.data.refresh_token)
        localStorage.setItem("user_info", JSON.stringify(res.data.user))
        return Promise.resolve(res)
    }

    async isAuthenticated() {
        const access_token = localStorage.getItem("access_token")
        const refresh_token = localStorage.getItem("refresh_token")
        if (!access_token || !refresh_token) {
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