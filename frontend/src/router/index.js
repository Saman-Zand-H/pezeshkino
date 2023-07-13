import { createRouter, createWebHistory } from 'vue-router'
import DoctorsListView from '../views/DoctorsListView.vue'
import DoctorView from '../views/DoctorView.vue'
import LoginView from '../views/LoginView.vue'
import HomeView from '../views/HomeView.vue'
// import SignupView from '../views/SignupView.vue'

const routes = [{
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ( /* webpackChunkName: "about" */ '../views/AboutView.vue')
    },
    {
        path: '/login',
        name: 'login',
        component: LoginView
    },
    {
        path: '/doctors',
        name: 'doctors',
        component: DoctorsListView,
    },
    {
        path: '/doctors/:username',
        name: "doctor",
        component: DoctorView
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router