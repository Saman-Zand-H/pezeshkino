<template>
    <div class="">
        <canvas id="income_chart"></canvas>
    </div>
</template>

<script>
    import Chart from 'chart.js/auto'
    import jmoment from 'moment-jalaali'
    import fa from 'moment/locale/fa'
    import moment from 'moment'

    export default {
        name: 'DashboardIncomeChart',
        props: {
            data: {
                type: Array,
                required: true
            }
        },
        mounted() {
            const chartData = {
                type: 'bar',
                
                data: {
                    labels: this
                                .$props
                                .data
                                .map(
                                    v => jmoment(v.datetime, "YYYY-MM-DTHH:mm:ss").format("dddd")
                                ),
                    datasets: [
                        {
                            data: this.$props.data.map(v => v.income),
                            borderColor: 'rgba(203,12,159,1)',
                            backgroundColor: 'rgba(203,12,159,1)',
                            barThickness: 5,
                            borderRadius: 100
                        }
                    ], 
                },
                options: {
                    responsive: true,
                    plugins: {
                        title: {
                            display: false
                        },
                        legend: {
                            display: false
                        }
                    },
                    scales: {
                        x: {
                            grid: {
                                display: false,
                            },
                            tick: {
                                display: false
                            },
                            display: false
                        },
                        y: {
                            grid: {
                                display: false,
                            },
                            tick: {
                                display: false
                            },
                            display: false
                        },
                    },
                }
            }
            const ctx = document.getElementById("income_chart")
            new Chart(ctx, chartData)
        },
    }
</script>