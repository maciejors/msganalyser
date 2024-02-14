<template>
	<GenericDashboard :dashboardElement="meta">
		<template v-slot:description>
			<p>The ranking of chats based on the number of days with at least one message.</p>
		</template>
		<RankingTable
			:keys="data.chat_name"
			:valuesNumericSorted="data.value"
			valuesLabel="Days with at least one message count"
		/>
	</GenericDashboard>
</template>

<script setup lang="ts">
import { dashboardElementsData } from '../../../utils/dashboardMeta';
import { getDaysWithMsgCounts } from '../../../utils/apiWrappers';
import { useFiltersStore } from '../../../stores/filters';

definePageMeta({
	layout: 'dashboard',
});

const filtersStore = useFiltersStore();

const meta = dashboardElementsData.get('days_with_msg_count')!;
const data = await getDaysWithMsgCounts(filtersStore.getFilters);
</script>
