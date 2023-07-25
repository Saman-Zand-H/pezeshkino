<template>
    <div v-if="!loading">
        <CommentSection :reviews="comments" />
    </div>
    <div class="h-screen animate-pulse" v-else>
        <div class="rounded-xl shadow-sm bg-gray-200 w-full h-3/4"></div>
    </div>
</template>

<script>
    import api from '@/_helpers/api'
    import CommentSection from '@/components/CommentSection.vue'
    import { mapState, mapActions } from 'vuex'

    export default {
        name: 'CommentsDashboardView',
        computed: {
            ...mapState(["user"])
        },
        data() {
            return {
                comments: [],
                loading: false
            }
        },
        components: {
            CommentSection
        },
        methods: {
            ...mapActions(["updateUserInfo"])
        },
        async beforeMount() {
            this.loading = true
            await this.updateUserInfo()
            try {
                const url = `/api/review?doctor_username=${this.user.username}`
                const res = await api.get(url)
                // todo: handle pagination
                if (res.status === 200) this.comments = res.data
            } catch (error) {console.error(error)}
            this.loading = false
        }
    }
</script>