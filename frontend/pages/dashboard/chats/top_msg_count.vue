<template>
	<GenericDashboard :dashboardElement="meta">
		<template v-slot:description>
			<p>The ranking of chats based on the total number of messages.</p>
		</template>
		<RankingTable
			:keys="data.chat_name"
			:valuesNumericSorted="data.value"
			valuesLabel="Total number of messages"
		/>
	</GenericDashboard>
</template>

<script setup lang="ts">
import { dashboardElementsData } from '../../../utils/dashboardMeta';
import { getTopMsgCount } from '../../../utils/apiWrappers';
import { useFiltersStore } from '../../../stores/filters';

definePageMeta({
	layout: 'dashboard',
});

const filtersStore = useFiltersStore();

const meta = dashboardElementsData.get('top_msg_count')!;
const data = await getTopMsgCount(filtersStore.getFilters);
</script>
