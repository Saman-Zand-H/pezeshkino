import { createStore } from 'vuex'
import locations from '@/store/modules/locations'
import user from '@/store/modules/user'
import doctors from '@/store/modules/doctors'

export default createStore({
    state: {},
    getters: {},
    mutations: {},
    actions: {},
    modules: {
        locations,
        user,
        doctors
    }
})