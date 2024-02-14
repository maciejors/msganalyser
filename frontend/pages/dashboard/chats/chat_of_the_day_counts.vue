<template>
	<GenericDashboard :dashboardElement="meta">
		<template v-slot:description>
			<p>
				Ranking of chats based on how many times a chat was the chat of the day, i.e. had the most
				messages of all chats on a day.
			</p>
		</template>
		<RankingTable
			:keys="data.chat_name"
			:valuesNumericSorted="data.value"
			valuesLabel="'Chat of the day' count"
		/>
	</GenericDashboard>
</template>

<script setup lang="ts">
import { dashboardElementsData } from '../../../utils/dashboardMeta';
import { getChatOfTheDayCounts } from '../../../utils/apiWrappers';
import { useFiltersStore } from '../../../stores/filters';

definePageMeta({
	layout: 'dashboard',
});

const filtersStore = useFiltersStore();

const meta = dashboardElementsData.get('chat_of_the_day_counts')!;
const data = await getChatOfTheDayCounts(filtersStore.getFilters);
</script>
