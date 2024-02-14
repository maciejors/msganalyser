<template>
	<GenericDashboard :dashboardElement="meta">
		<template v-slot:description>
			<p>The ranking of chats based on the total duration of calls.</p>
		</template>
		<RankingTable
			:keys="data.chat_name"
			:valuesNumericSorted="data.value"
			:valuesDisplayed="prettyDurations"
			valuesLabel="Total duration of calls"
		/>
	</GenericDashboard>
</template>

<script setup lang="ts">
import { dashboardElementsData } from '../../../utils/dashboardMeta';
import { getTopCallsDuration } from '../../../utils/apiWrappers';
import { useFiltersStore } from '../../../stores/filters';

definePageMeta({
	layout: 'dashboard',
});

const filtersStore = useFiltersStore();

const meta = dashboardElementsData.get('top_calls_duration')!;
const data = await getTopCallsDuration(filtersStore.getFilters);

const prettyDurations = data.value.map((timeIsSeconds) => {
	const fullHours = Math.floor(timeIsSeconds / 3600);
	const remainderFullMinutes = Math.floor(timeIsSeconds / 60) % 60;
	const remainderSeconds = timeIsSeconds % 60;
	let result = `${remainderSeconds}s`;
	if (remainderFullMinutes > 0) {
		result = `${remainderFullMinutes}m ${result}`;
	}
	if (fullHours > 0) {
		result = `${fullHours}h ${result}`;
	}
	return result;
});
</script>
