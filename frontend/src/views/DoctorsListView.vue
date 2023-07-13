<template>
    <div class="relative">
        <DoctorsContainer :breadcrumb='["پزشکان"]' />
        <DoctorsListBody />
    </div>
    
</template>

<script>
    import DoctorsContainer from '@/components/DoctorsContainer.vue'
    import DoctorsListBody from '@/components/DoctorsListBody.vue'

    export default {
        name: "DoctorsListView",
        components: { 
            DoctorsContainer,
            DoctorsListBody
        }
    }
</script>