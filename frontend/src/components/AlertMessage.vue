<template>
    <div :class="[
        styles.bg, styles.border, styles.text,
        'lg:fixed absolute ease-out border-2 transform-gpu transition-all', 
        'rounded-md md:w-[27%] w-full md:left-auto container text-right z-40 duration-300',
        'flex-row-reverse w-full items-center px-8 py-4', 
        'top-24 right-10 flex justify-between opacity-90']"
        role="alert"
        id="alertContainer"
       >
        <div :class="[styles.highlightLine, 'px-4 py-2 container font-semibold border-e-4 flex-wrap']"
            id="alertDiv"
           >
            <div style="direction:rtl">
                <i :class="['fas', icon, 'text-lg']"></i>
                {{ msg }}
            </div>
        </div>
        <div>
            <button type="button" @click.prevent="closeAlert">
                <i class="fas fa-close"></i>
            </button>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'AlertMessage',
        props: {
            msg: {
                type: String,
                default: 'درسته!'
            },
            alertType: {
                type: String,
                default: 'danger'
            },
            colorsMap: {
                type: Object,
                default: {
                    danger: {
                        bg: 'bg-red-700/90',
                        border: 'border-red-900',
                        highlightLine: 'border-e-red-900',
                        text: 'text-red-950'
                    },
                    success: {
                        bg: 'bg-emerald-500/90',
                        border: 'border-emerald-800',
                        highlightLine: 'border-e-emerald-800',
                        text: 'text-emerald-900'
                    },
                    warning: {
                        bg: 'bg-yellow-400',
                        border: 'border-yellow-900',
                        highlightLine: 'border-e-yellow-900',
                        text: 'text-yellow-900'
                    }
                }
            },
            iconsMap: {
                type: Object,
                default: {
                    success: 'fa-award text-emerald-900',
                    danger: 'fa-ban text-red-950',
                    warning: 'fa-warning text-amber-950'
                }
            },
            ttl: {
                type: Number,
                default: 0
            }
        },
        computed: {
            styles() {
                return this.$props.colorsMap[this.$props.alertType]
            },
            icon() {
                return this.$props.iconsMap[this.$props.alertType]
            }
        },
        watch: {
            isVisible(newState, oldState) {
                const ttl = this.$props.ttl
                if (newState && ttl !== 0) {
                    setTimeout(() => {
                        const elem = document.getElementById('alertContainer')
                        elem.classList.add("animate__animated", "animate__fadeOutRight")
                    }, ttl * 1000)
                }
            }
        },
        methods: {
            closeAlert(e) {
                document.getElementById('alertContainer').remove()
            }
        }
    }
</script>
