<template>
    <div>
        <CommentSection :reviews="comments" />
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
                comments: []
            }
        },
        components: {
            CommentSection
        },
        methods: {
            ...mapActions(["updateUserInfo"])
        },
        async beforeMount() {
            await this.updateUserInfo()
            const url = `/api/review?doctor_username=${this.user.username}`
            const res = await api.get(url)
            // todo: handle pagination
            if (res.status === 200) this.comments = res.data
        }
    }
</script>