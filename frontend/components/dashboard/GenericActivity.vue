<template>
	<DashboardBaseWrapper :dashboardElement="meta">
		<template v-slot:description>
			<p>{{ props.plotDescription }}</p>
		</template>
		<Bar :options="chartOptions" :data="chartData" />
	</DashboardBaseWrapper>
</template>

<script setup lang="ts">
import { Bar } from 'vue-chartjs';
import { dashboardElementsData, defaultChartColour } from '../../utils/dashboardMeta';
import { genericGet } from '../../utils/apiWrappers';
import type { DatetimeActivityStat } from '../../utils/apiWrappers';
import { useFiltersStore } from '../../stores/filters';

const props = defineProps({
	dashboardElementId: {
		type: String,
		required: true,
	},
	plotDescription: {
		type: String,
		required: true,
	},
	barValuesLabel: {
		type: String,
		required: true,
	},
});

const filtersStore = useFiltersStore();

const meta = dashboardElementsData.get(props.dashboardElementId)!;
const data = await genericGet<DatetimeActivityStat>(
	`${meta.group}${meta.routeRelative}`,
	filtersStore.getFilters
);

const chartData = {
	labels: data.key,
	datasets: [
		{
			data: data.value,
			label: props.barValuesLabel,
			backgroundColor: defaultChartColour,
		},
	],
};
const chartOptions = {};
</script>
