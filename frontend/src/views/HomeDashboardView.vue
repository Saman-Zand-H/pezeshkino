<template>
    <div>
        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-4">
            <div class="flex flex-row-reverse items-center gap-4 bg-white rounded-2xl p-4 shadow-sm">
                <div class="inline-flex flex-shrink-0 justify-center items-center w-12 h-12 text-white bg-gradient-to-br from-pink-500 to-purple-500 rounded-lg shadow-md shadow-gray-300">
                    <span><i class="fa fa-coins text-lg"></i></span>
                </div>
                <div class="flex flex-col items-end">
                    <!-- the data is in the descending order, so the first element is for the day -->
                    <span v-if="chartData.length > 0">{{ chartData[0].income }}</span>
                    <span v-else>0 تومان</span>
                    <span class="text-gray-500 text-sm">درآمد در روز</span>
                </div>
            </div>
            <div class="flex flex-row-reverse items-center gap-4 bg-white rounded-2xl p-4 shadow-sm">
                <div class="inline-flex flex-shrink-0 justify-center items-center w-12 h-12 text-white bg-gradient-to-br from-pink-500 to-purple-500 rounded-lg shadow-md shadow-gray-300">
                    <span><i class="fa fa-user-injured text-2xl"></i></span>
                </div>
                <div class="flex flex-col items-end">
                    <span>{{ numberOfPatients }}</span>
                    <span class="text-gray-500 text-sm">بیماران ویزیت شده</span>
                </div>
            </div>
            <div class="flex flex-row-reverse items-center gap-4 bg-white rounded-2xl p-4 shadow-sm">
                <div class="inline-flex flex-shrink-0 justify-center items-center w-12 h-12 text-white bg-gradient-to-br from-pink-500 to-purple-500 rounded-lg shadow-md shadow-gray-300">
                    <span><i class="fa fa-building text-xl"></i></span>
                </div>
                <div class="flex flex-col items-end">
                    <span>{{ numberOfOffices }}</span>
                    <span class="text-gray-500 text-sm">مطب های ثبت شده</span>
                </div>
            </div>
            <div class="flex flex-row-reverse items-center gap-4 bg-white rounded-2xl p-4 shadow-sm">
                <div class="inline-flex flex-shrink-0 justify-center items-center w-12 h-12 text-white bg-gradient-to-br from-pink-500 to-purple-500 rounded-lg shadow-md shadow-gray-300">
                    <span><i class="fa fa-calendar-check text-lg"></i></span>
                </div>
                <div class="flex flex-col items-end">
                    <span>{{ numberOfAppointments }}</span>
                    <span class="text-gray-500 text-sm">ملاقات های امروز</span>
                </div>
            </div>
        </div>
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 my-4">
            <div class="bg-gradient-to-r shadow-md text-white from-slate-800 to-slate-950 rounded-2xl p-4">
                <div class="flex justify-between">
                    <div class="font-semibold text-lime-400 text-lg">
                        20% <i class="fa fa-arrow-up"></i>
                    </div>
                    <div class="flex flex-col gap-1 items-end">
                        <span class="text-xl font-semibold">{{ weeklyIncome }} تومان</span>
                        <span class="text-sm font-medium me-4">درآمد این هفته</span>
                    </div>
                </div>
                <DashboardIncomeChart :data="chartData" />
            </div>

            <div class="bg-white rounded-2xl p-4 shadow-md">
                <div class="flex flex-row-reverse justify-between items-center mb-4">
                    <div class="text-right">
                        <h1 class="text-xl font-semibold">نظرات کاربران</h1>
                        <span class="text-xs">این لیستی از جدید ترین نظرات کاربران است</span>
                    </div>
                    <div class="flex-shrink-0 text-sm font-medium">
                        مشاهده همه
                    </div>
                </div>
                <div class="flex flex-col mt-8">
                    <div class="overflow-x-auto rounded-2xl">
                        <div class="inline-block min-w-full align-middle">
                            <div class="overflow-hidden shadow-lg shadow-gray-200">
                                <table class="min-w-full divide-y divide-gray-200">
                                    <thead>
                                        <tr>
                                            <th class="p-4 text-xs font-medium tracking-wider text-right text-gray-500">
                                                میانگین نمره
                                            </th>
                                            <th class="p-4 text-xs font-medium tracking-wider text-right text-gray-500">
                                                علت مراجعه
                                            </th>
                                            <th class="p-4 text-xs font-medium tracking-wider text-right text-gray-500">
                                                پیشنهاد میدهد
                                            </th>
                                            <th class="p-4 text-xs font-medium tracking-wider text-right text-gray-500">
                                                نام کاربری
                                            </th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="comment in comments">
                                            <td class="p-4 text-xs font-medium tracking-wider text-right text-gray-500">
                                                {{ comment.average_score }}
                                            </td>
                                            <td class="p-4 text-xs font-medium tracking-wider text-right text-gray-500">
                                                {{ comment.illness }}
                                            </td>
                                            <td class="p-4 text-xs font-medium tracking-wider text-right text-gray-500">
                                                <i class="fa fa-thumbs-up text-lime-700 text-xl" v-if="comment.suggests_doctor"></i>
                                                <i class="fa fa-thumbs-down text-red-600 text-xl" v-else></i>
                                            </td>
                                            <td class="p-4 text-xs font-medium tracking-wider text-right text-gray-500">
                                                {{ comment.by_user.username }}
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import api from '@/_helpers/api'
    import DashboardIncomeChart from '@/components/DashboardIncomeChart.vue'

    export default {
        name: 'HomeDashboardView',
        components: {
            DashboardIncomeChart
        },
        data() {
            return {
                numberOfPatients: 0,
                numberOfAppointments: 0,
                numberOfOffices: 0,
                chartData: [{income: 50, datetime: '2023-01-01T20:20:20'}],
                weeklyIncome: 0,
                comments: []
            }
        },
        async beforeCreate() {
            try {
                const res = await api.get("/api/dashboard/home/")
    
                if (res.status === 200) {
                    this.numberOfAppointments = res.data.number_of_appointments
                    this.numberOfPatients = res.data.number_of_patients
                    this.numberOfOffices = res.data.number_of_offices
                    this.chartData = res.data.revenue_for_week
                    this.weeklyIncome = res.data.weekly_income
                    this.comments = res.data.comments
                }
            } catch (error) {
                console.error(error)
            }
        }
    }
</script>