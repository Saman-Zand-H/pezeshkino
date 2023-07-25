<template>
    <nav class="bg-white z-20 w-full h-16 fixed flex justify-between">
        <ul class="px-2 flex items-center gap-7">
            <button type="button" @click="$emit('toggle-sidebar')">
                <i class="fa fa-bars text-xl text-slate-700"></i>
            </button>
            <li class="flex gap-2">
                <img src="@/assets/logo.png" class="w-6 aspect-square">
                <span class="font-semibold">Pezeshkino</span>
            </li>
        </ul>
        <ul class="px-4 flex flex-row-reverse items-center gap-7">
            <li class="w-fit border rounded-full overflow-hidden">
                <button type="button" class="flex rounded-full">
                    <span class="sr-only">Open user menu</span>
                    <img class="w-8 h-8 rounded-full" :src="user.piture ? user.picture : require('@/assets/blank-user.png')" alt="user photo">
                </button>
            </li>
            <!-- <li class="w-fit overflow-hidden">
                <button type="button" class="p-2 text-gray-500 rounded-2xl hover:text-gray-900 hover:bg-gray-100">
                    <span class="sr-only">View notifications</span>
                    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path></svg>
                </button>
            </li>
            <li class="w-fit overflow-hidden">
                <button type="button" class="p-2 text-gray-500 rounded-2xl hover:text-gray-900 hover:bg-gray-100">
                    <span class="sr-only">Options menu</span>
                    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M10 2a6 6 0 00-6 6v3.586l-.707.707A1 1 0 004 14h12a1 1 0 00.707-1.707L16 11.586V8a6 6 0 00-6-6zM10 18a3 3 0 01-3-3h6a3 3 0 01-3 3z"></path></svg>
                </button>
            </li> -->
        </ul>
    </nav>
</template>

<script>
    import { provide } from 'vue'

    export default {
        name: 'DashboardNavbar',
        data() {
            return {
                user: {}
            }
        },
        emits: ["toggle-sidebar"]
    }
</script>