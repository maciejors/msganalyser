<template>
	<GenericDashboard :dashboardElement="meta">
		<template v-slot:description>
			<p>The ranking of chats based on the total number of calls.</p>
		</template>
		<RankingTable
			:keys="data.chat_name"
			:valuesNumericSorted="data.value"
			valuesLabel="Total number of calls"
		/>
	</GenericDashboard>
</template>

<script setup lang="ts">
import { dashboardElementsData } from '../../../utils/dashboardMeta';
import { getTopCallsCount } from '../../../utils/apiWrappers';
import { useFiltersStore } from '../../../stores/filters';

definePageMeta({
	layout: 'dashboard',
});

const filtersStore = useFiltersStore();

const meta = dashboardElementsData.get('top_calls_count')!;
const data = await getTopCallsCount(filtersStore.getFilters);
</script>
