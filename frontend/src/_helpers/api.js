import axios from 'axios'

const api = axios.create({
    headers: { 'Content-Type': 'application/json' }
})

export const refreshToken = async() => {
    const refreshToken = localStorage.getItem('refresh_token')
    if (refreshToken) {
        try {
            const response = await axios.post('/api/token/refresh/', {
                refresh: refreshToken
            })
            if (response.status === 200) {
                return Promise.resolve(response.data.access)
            }
        } catch {
            // if the token is invalid we remove the token so we can tell 
            // they're not authenticated
            localStorage.removeItem("refresh_token")
            localStorage.removeItem("access_token")
            console.error("Invalid refresh token was used.")
            return Promise.reject("invalid refresh token.")
        }
    }
}

api.interceptors.request.use(
    config => {
        const accessToken = localStorage.getItem("access_token")
        config.headers.Authorization = `Bearer ${accessToken}`
        return config
    },
    error => Promise.reject(error)
)

const responseInterceptor = api.interceptors.response.use(
    response => response,
    async error => {
        if (error.response.status !== 401 || error.response.data.code !== "token_not_valid") {
            return Promise.reject(error)
        }

        api.interceptors.response.eject(responseInterceptor)

        try {
            const access = await refreshToken()
            localStorage.setItem('access_token', access)
            error.response.config.headers["Authorization"] = `Bearer ${access}`
            return api.request(error.response.config)
        } catch (error) {
            console.error(error)
            error.config.retry = false
            return Promise.reject(error)
        }
    }
)

export default api