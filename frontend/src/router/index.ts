import AppointmentsProfileView from '../views/AppointmentsProfileView.vue'
import EditUserProfileView from '../views/EditUserProfileView.vue'
import GeneralProfileView from '../views/GeneralProfileView.vue'
import PaymentStatusView from '@/views/PaymentStatusView.vue'
import DoctorsSignupView from '@/views/DoctorsSignupView.vue'
import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import ReviewView from '@/views/ReviewView.vue'
import DoctorsListView from '../views/DoctorsListView.vue'
import DoctorView from '../views/DoctorView.vue'
import SignupView from '../views/SignupView.vue'
import LoginView from '../views/LoginView.vue'
import AuthView from '../views/AuthView.vue'
import HomeView from '../views/HomeView.vue'
import AuthManager from '@/_helpers/auth'

const routes: RouteRecordRaw[] = [{
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
        path: '/authentication',
        name: 'auth',
        component: AuthView,
        children: [
            {
                path: 'login',
                name: 'login',
                component: LoginView
            }, {
                path: 'signup',
                name: 'signup',
                component: SignupView
            },
            {
                path: 'doctor',
                name: 'doctor_signup',
                component: DoctorsSignupView
            }
        ]
    },
    {
        path: '/doctors/',
        name: 'doctors',
        component: DoctorsListView,
    },
    {
        path: '/doctors/:username',
        name: "doctor",
        component: DoctorView
    },
    {
        path: '/doctors/:username/review',
        name: "new_review",
        component: ReviewView
    },
    {
        path: '/user',
        name: 'user',
        component: GeneralProfileView,
        children: [{
                path: 'edit',
                component: EditUserProfileView,
                name: 'profile_edit'
            },
            {
                path: 'appointments',
                component: AppointmentsProfileView,
                name: 'profile_appointments'
            }
        ],
    },
    {
        path: '/payment_status',
        name: 'payment_status',
        component: PaymentStatusView,
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

router.beforeEach(async(to, from) => {
    if (['user', 'profile_edit', 'profile_appointments'].indexOf(String(to.name)) !== -1) {
        const is_authenticated = await AuthManager.isAuthenticated()
        if (!is_authenticated) return { name: "login" }
    } else if (['auth', 'login', 'signup'].indexOf(String(to.name)) !== -1) {
        const is_authenticated = await AuthManager.isAuthenticated()
        if (is_authenticated) {
            return { name: 'home' }
        }
    }
})

export default router