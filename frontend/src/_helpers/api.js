import axios from 'axios'

const api = axios.create({
    headers: { 'Content-Type': 'application/json' }
})

export const refreshToken = async() => {
    const refreshToken = localStorage.getItem('refresh_token')
    if (refreshToken) {
        const response = await axios.post('/dj-rest-auth/token/refresh/', {
            refresh: refreshToken
        })

        // if there exists the token, we consider the user authenticated
        if (response.status === 200) {
            localStorage.setItem('access_token', response.data.access)
            return Promise.resolve()
        } else if (response.status === 401) {
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
            // handling auth
        if (accessToken) {
            config.headers.Authorization = `Bearer ${accessToken}`
        }

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
            await refreshToken()
            const accessToken = localStorage.getItem("access_token")
            console.log(accessToken)
            error.response.config.headers["Authorization"] = `Bearer ${accessToken}`
            return api.request(error.response.config)
        } catch (error) {
            console.error(error)
            error.config.retry = false
            return Promise.reject(error)
        }
    }
)

export default api