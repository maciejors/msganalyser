<template>
	<DashboardBaseWrapper :dashboardElement="meta">
		<template v-slot:description>
			<p>
				The ranking of chats based on the longest streak of days with at least one message. Only
				chats with the longest streak of at least 2 are included. As a tie-breaker, the longest
				streak count is used.
			</p>
		</template>
		<TableChatRanking
			:keys="data.chat_name"
			:valuesNumericSorted="data.value"
			:valuesDisplayed="valuesDisplayed"
			valuesLabel="The longest streak length (count)"
		/>
	</DashboardBaseWrapper>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { dashboardElementsData } from '../../../utils/dashboardMeta';
import { genericGet } from '../../../utils/apiWrappers';
import type { ChatStreakStat } from '../../../utils/apiWrappers';
import { useFiltersStore } from '../../../stores/filters';

definePageMeta({
	layout: 'dashboard',
});

const filtersStore = useFiltersStore();

const meta = dashboardElementsData.get('longest_streaks')!;
const data = await genericGet<ChatStreakStat>(
	`${meta.group}${meta.routeRelative}`,
	filtersStore.getFilters
);
const valuesDisplayed = computed(() => data.value.map((len, i) => `${len} (${data.count[i]})`));
</script>
