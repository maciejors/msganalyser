<template>
	<DashboardBaseWrapper :dashboard-element="meta">
		<template v-slot:description>
			<p>{{ props.plotDescription }}</p>
		</template>
		<Bar v-if="chartData.labels.length > 0" :options="chartOptions" :data="chartData" />
		<NoDataIndicator v-else />
	</DashboardBaseWrapper>
</template>

<script setup lang="ts">
import { Bar } from 'vue-chartjs';
import { dashboardElementsData, defaultChartColour } from '../../utils/dashboardMeta';
import { genericGet } from '../../utils/apiWrappers';
import type { DatetimeActivityStat } from '../../utils/apiWrappers';
import { useFiltersStore } from '../../stores/filters';
import { getIsDataLoaded } from '../../utils/apiWrappers';

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

const chartData = {
	labels: [''],
	datasets: [
		{
			data: [0],
			label: props.barValuesLabel,
			backgroundColor: defaultChartColour,
		},
	],
};
const chartOptions = {};

if (!(await getIsDataLoaded())) {
	await navigateTo('/');
} else {
	const data = await genericGet<DatetimeActivityStat>(
		`${meta.group}${meta.routeRelative}`,
		filtersStore.getFilters
	);
	chartData.labels = data.datetime_key;
	chartData.datasets[0].data = data.value;
}
</script>
