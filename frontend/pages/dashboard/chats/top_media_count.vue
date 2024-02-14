<template>
	<GenericDashboard :dashboardElement="meta">
		<template v-slot:description>
			<p>The ranking of chats based on the total number of media (photos, videos and files).</p>
		</template>
		<RankingTable
			:keys="data.chat_name"
			:valuesNumericSorted="data.value"
			valuesLabel="Total number of media"
		/>
	</GenericDashboard>
</template>

<script setup lang="ts">
import { dashboardElementsData } from '../../../utils/dashboardMeta';
import { getTopMediaCount } from '../../../utils/apiWrappers';
import { useFiltersStore } from '../../../stores/filters';

definePageMeta({
	layout: 'dashboard',
});

const filtersStore = useFiltersStore();

const meta = dashboardElementsData.get('top_media_count')!;
const data = await getTopMediaCount(filtersStore.getFilters);
</script>
