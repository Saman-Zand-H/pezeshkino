<template>
    <router-link 
                 class="flex flex-col relative card rounded-lg border max-w-none border-slate-200 overflow-hidden shadow-lg w-80 h-80 pb-3 gap-5 transition-all duration-300 hover:ring-sky-900/50 hover:scale-105" 
                 :to="{ 'name': 'doctor', 'params': { 'username': username } }" 
                 @mouseover="mouseoverCard" 
                 @mouseout="mouseoutCard"
                >
        <div class="-z-50 relative">
            <img :src="picture_link" :alt="['dr.', name, 'picture']" class="w-full aspect-square relative -z-50 overflow-hidden opacity-85 shadow-lg rounded-t-md self-center">
        </div>
        <div class="flex flex-col bg-white z-50 h-40 absolute inset-x-0 w-full -bottom-20 shadow-sm card-body transition-all duration-500">
            <span class="flex flex-row-reverse items-center justify-center gap-4">
                <h1 class="text-sky-600 font-semibold text-lg">{{ name }} دکتر</h1>
                <i v-if="verified" class="fa fa-check bg-sky-500 rounded-full py-[.34rem] px-1.5 text-white"></i>
            </span>
            <span>
                <small class="text-cyan-950">{{ specialty_display }}</small>
            </span>
        </div>
    </router-link>
</template>

<script>
    export default {
        name: 'DoctorCard',
        props: {
            name: String,
            username: String,
            specialty_display: String,
            specialty: String,
            picture_link: String,
            verified: Boolean
        },
        methods: {
            mouseoverCard(e) {
                const cardBody = e.target.closest(".card").querySelector(".card-body")
                cardBody.classList.add("-translate-y-14", "rounded-t-md", "pt-4")
            },
            mouseoutCard(e) {
                const cardBody = e.target.closest(".card").querySelector(".card-body")
                cardBody.classList.remove("-translate-y-14", "rounded-t-md", "pt-4")
            }
        }
    }
</script>