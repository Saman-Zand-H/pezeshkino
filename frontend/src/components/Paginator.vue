<template>
    <nav>
        <ul class="flex items-center -space-x-px text-base">
            <li>
                <button @click.prevent="$emit('page-changed', page-1)" v-if="count > 1 && page > 1"
                    class="flex items-center justify-center px-4 h-12 ml-0 leading-tight text-gray-500 bg-white border border-gray-300 rounded-l-lg hover:bg-gray-100 hover:text-gray-700">
                    <span class="sr-only">قبلی</span>
                    <svg class="w-2.5 h-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                        viewBox="0 0 6 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M5 1 1 5l4 4" />
                    </svg>
                </button>
            </li>
            <li v-for="p in count" :key="p">
                <button @click.prevent="$emit('page-changed', p)"
                    :class="[p === page ? 'bg-blue-50 text-blue-600' : 'bg-white text-gray-500', 'flex items-center justify-center px-4 h-12 leading-tight border border-gray-300 hover:bg-gray-100 hover:text-gray-700 ']">
                    {{ p }}
                </button>
            </li>
            <li>
                <button @click.prevent="$emit('page-changed', page+1)" v-if="count > 1 && page < count"
                    class="flex items-center justify-center px-4 h-12 leading-tight text-gray-500 bg-white border border-gray-300 rounded-r-lg hover:bg-gray-100 hover:text-gray-700 ">
                    <span class="sr-only">بعدی</span>
                    <svg class="w-2.5 h-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                        viewBox="0 0 6 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="m1 9 4-4-4-4" />
                    </svg>
                </button>
            </li>
        </ul>
    </nav>
</template>

<script>
export default {
    name: 'Paginator',
    props: {
        page: {
            type: Number,
            default: 1
        },
        count: {
            type: Number,
            default: 0
        }
    },
    emits: ["page-changed"]
}
</script>