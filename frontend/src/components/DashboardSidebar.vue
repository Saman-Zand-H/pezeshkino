<template>
    <aside :class="[sidebarActive ? 'md:w-1/5 w-full px-5' : 'lg:w-[8%] w-0 items-center' ,'bg-white transition-all duration-150 shadow-lg inset-y-0 left-0 py-24 fixed flex flex-col h-full overflow-hidden']">
        <ul>
            <router-link :to="{ name: 'home' }" class="rounded-xl hover:cursor-pointer flex items-center gap-4 hover:bg-slate-200 hover:text-gray-700 transition-colors duration-150 py-2 px-4">
                <span class="bg-white shadow-md p-3 rounded-xl">
                    <i class="fa fa-home"></i>
                </span>
                <span v-if="sidebarActive" class="text-sm text-slate-600">
                    خانه
                </span>
            </router-link>
            <router-link :to="{ name: 'doctor_dashboard_home' }" class="rounded-xl hover:cursor-pointer flex items-center gap-4 hover:bg-slate-200 hover:text-gray-700 transition-colors duration-150 py-2 px-4">
                <span class="bg-white shadow-md p-3 rounded-xl">
                    <i class="fa fa-dashboard"></i>
                </span>
                <span v-if="sidebarActive" class="text-sm text-slate-600">
                    داشبورد
                </span>
            </router-link>
            <router-link :to="{ name: 'doctor_dashboard_appointments'}" class="rounded-xl hover:cursor-pointer flex items-center gap-4 hover:bg-slate-200 hover:text-gray-700 transition-colors duration-150 py-2 px-4">
                <span class="bg-white shadow-md p-3 rounded-xl">
                    <i class="fa fa-calendar-check"></i>
                </span>
                <span v-if="sidebarActive" class="text-sm text-slate-600">
                    ملاقات ها
                </span>
            </router-link>
            <li class="rounded-xl hover:cursor-pointer flex items-center gap-4 hover:bg-slate-200 hover:text-gray-700 transition-colors duration-150 py-2 px-4">
                <span class="bg-white shadow-md p-3 rounded-xl">
                    <i class="fa fa-building"></i>
                </span>
                <span v-if="sidebarActive" class="text-sm text-slate-600">
                    مطب ها
                </span>
            </li>
            <!--todo:this feature will be added in the next update.-->
            <!-- <li class="rounded-xl hover:cursor-pointer flex items-center gap-4 hover:bg-slate-200 hover:text-gray-700 transition-colors duration-150 py-2 px-4">
                <span class="bg-white shadow-md p-3 rounded-xl">
                    <i class="fa fa-money-bill"></i>
                </span>
                <span v-if="sidebarActive" class="text-sm text-slate-600">
                    امور مالی
                </span>
            </li> -->
            <li class="rounded-xl hover:cursor-pointer flex items-center gap-4 hover:bg-slate-200 hover:text-gray-700 transition-colors duration-150 py-2 px-4">
                <span class="bg-white shadow-md p-3 rounded-xl">
                    <i class="fa fa-comment"></i>
                </span>
                <span v-if="sidebarActive" class="text-sm text-slate-600">
                    نظرات
                </span>
            </li>
            <li class="rounded-xl hover:cursor-pointer flex items-center gap-4 hover:bg-slate-200 hover:text-gray-700 transition-colors duration-150 py-2 px-4">
                <span class="bg-white shadow-md p-3 rounded-xl">
                    <i class="fa fa-sign-out"></i>
                </span>
                <span v-if="sidebarActive" class="text-sm text-slate-600">
                    خروج
                </span>
            </li>
        </ul>
    </aside>
</template>

<script>
    export default {
        name: 'DashbaordSidebar',
        props: {
            sidebarActive: Boolean
        }
    }
</script>