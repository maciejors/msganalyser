<template>
	<GenericDashboard :dashboardElement="meta">
		<template v-slot:description>
			<p>This plot shows how many messages have been sent and/or received in each month.</p>
		</template>
		<Bar :options="chartOptions" :data="chartData" />
	</GenericDashboard>
</template>

<script setup lang="ts">
import { Bar } from 'vue-chartjs';
import { dashboardElementsData, defaultChartColour } from '../../../utils/dashboardMeta';
import { getMsgByMonth } from '../../../utils/apiWrappers';

definePageMeta({
	layout: 'dashboard',
});

const meta = dashboardElementsData.get('msg_by_month')!;
const data = await getMsgByMonth();

const chartData = {
	labels: data.key,
	datasets: [
		{
			data: data.value,
			label: 'Messages count',
			backgroundColor: defaultChartColour,
		},
	],
};
const chartOptions = {};
</script>
