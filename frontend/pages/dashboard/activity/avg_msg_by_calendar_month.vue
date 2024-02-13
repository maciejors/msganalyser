<template>
	<GenericDashboard :dashboardElement="meta">
		<template v-slot:description>
			<p>
				This plot shows how many messages on average have been sent and/or received in each calendar
				month.
			</p>
		</template>
		<Bar :options="chartOptions" :data="chartData" />
	</GenericDashboard>
</template>

<script setup lang="ts">
import { Bar } from 'vue-chartjs';
import { dashboardElementsData, defaultChartColour } from '../../../utils/dashboardMeta';
import { getAvgMsgByCalendarMonth } from '../../../utils/apiWrappers';

definePageMeta({
	layout: 'dashboard',
});

const meta = dashboardElementsData.get('avg_msg_by_calendar_month')!;
const data = await getAvgMsgByCalendarMonth();

const chartData = {
	labels: data.key,
	datasets: [
		{
			data: data.value,
			label: 'Average messages count',
			backgroundColor: defaultChartColour,
		},
	],
};
const chartOptions = {};
</script>
