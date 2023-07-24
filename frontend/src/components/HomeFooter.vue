<template>
    <div class="top-[26rem] py-12 bg-black text-white w-full">
        <div class="flex justify-center items-center mb-6">
            <button class="hover:underline" @click="scrollToTop">
                Back to top
                <i class="fas fa-arrow-up"></i>
            </button>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5 px-24">
            <span>
                <a href="github.com/saman-zand-h/" class="flex items-center gap-2">
                    <i class="fab fa-github text-2xl text-cyan-950"></i>
                    Saman-Zand-H
                </a>
            </span>
            <span>
                <a href="telegram.me/RobSaman" class="flex items-center gap-2">
                    <i class="fab fa-telegram text-cyan-600 text-2xl"></i>
                    RobSaman
                </a>
            </span>
            <span>
                <a href="instagram.com/t.n.saman" class="flex items-center gap-2">
                    <i class="fab fa-instagram text-white text-2xl"></i>
                    t.n.saman
                </a>
            </span>
            <span>
                <a href="linkedin.com/saman-zand-h" class="flex items-center gap-2">
                    <i class="fab fa-linkedin text-cyan-900 text-2xl"></i>
                    Saman-Zand-H
                </a>
            </span>
        </div>
    </div>
    <div class="top-[26rem] w-full">
        <div class="block h-6 bg-black border-b-[1px] border-white"></div>
        <div class="block h-6 bg-black border-b-[2px] border-white"></div>
        <div class="block h-6 bg-black border-b-[3px] border-white"></div>
        <div class="block h-6 bg-black border-b-[4px] border-white"></div>
        <div class="block h-6 bg-black border-b-[5px] border-white"></div>
        <div class="block h-6 bg-black border-b-[6px] border-white"></div>
        <div class="block h-6 bg-black border-b-[7px] border-white"></div>
        <div class="block h-6 bg-black border-b-[8px] border-white"></div>
        <div class="block h-6 bg-black border-b-[9px] border-white"></div>
        <div class="block h-6 bg-black border-b-[10px] border-white"></div>
        <div class="block h-6 bg-black border-b-[11px] border-white"></div>
        <div class="block h-6 bg-black border-b-[12px] border-white"></div>
        <div class="block h-6 bg-black border-b-[13px] border-white"></div>
        <div class="block h-6 bg-black border-b-[14px] border-white"></div>
        <div class="block h-6 bg-black border-b-[15px] border-white"></div>
        <div class="block h-6 bg-black border-b-[16px] border-white"></div>
        <div class="block h-6 bg-black border-b-[17px] border-white"></div>
        <div class="block h-6 bg-black border-b-[18px] border-white"></div>
        <div class="block h-6 bg-black border-b-[19px] border-white"></div>
        <div class="block h-6 bg-black border-b-[20px] border-white"></div>
        <div class="block h-6 bg-black border-b-[21px] border-white"></div>
        <div class="block h-6 bg-black border-b-[22px] border-white"></div>
        <div class="block h-6 bg-black border-b-[23px] border-white"></div>
        <div class="block h-6 bg-black border-b-[24px] border-white"></div>
        <div class="block h-[3rem] bg-white"></div>
    </div>
</template>

<script>
    export default {
        name: 'HomeFooter',
        methods: {
            scrollToTop() {
                scrollTo(0, 0)
            }
        }
    }
</script>
