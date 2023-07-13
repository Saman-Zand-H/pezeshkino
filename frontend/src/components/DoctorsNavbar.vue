<template>
    <header class="w-full shadow-md bg-white z-[100] top-0 inset-x-0 transition-all duration-300">
        <div class="items-center flex">
            <div class="relative flex align-baseline items-center justify-between ms-12">
                <div class="flex space-x-3 items-center text-sky-800">
                    <img src="@/assets/logo.png" alt="logo" class="h-8 w-auto">
                </div>
            </div>

            <div class="">
                <nav>
                    <ul class="flex flex-row flex-wrap items-baseline space-x-16 ms-20">
                        <li>
                            <router-link :to="{ name: 'home' }" class="navbar-link text-cyan-800 hover:text-cyan-950 transition-all duration-200 hover:underline underline-offset-4 font-semibold">Home</router-link>
                        </li>
                        <li>
                            <router-link :to="{ name: 'about' }" class="navbar-link text-cyan-800 hover:text-cyan-950 transition-all duration-200 hover:underline underline-offset-4 font-semibold">About</router-link>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>
</template>

<style scoped></style>

<script>
    export default {
        name: "DoctorNavbar"
    }
</script>