<template>
	<GenericDashboard :dashboardElement="meta">
		<template v-slot:description>
			<p>
				This plot shows how many messages have been sent and/or received at each time of the day.
				The values on the x-axis represent hours on the clock. For example, a value of 13
				corresponds to the time period between 13:00 (inclusive) and 14:00 (exclusive).
			</p>
		</template>
		<Bar :options="chartOptions" :data="chartData" />
	</GenericDashboard>
</template>

<script setup lang="ts">
import { Bar } from 'vue-chartjs';
import { dashboardElementsData, defaultChartColour } from '../../../utils/dashboardMeta';
import { getMsgByTimeOfDay } from '../../../utils/apiWrappers';
import { useFiltersStore } from '../../../stores/filters';

definePageMeta({
	layout: 'dashboard',
});

const filtersStore = useFiltersStore();

const meta = dashboardElementsData.get('msg_by_time_of_day')!;
const data = await getMsgByTimeOfDay(filtersStore.getFilters);

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
