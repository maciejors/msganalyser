<template>
	<DashboardBaseWrapper :dashboard-element="meta">
		<template v-slot:description>
			<p>
				The ranking of chats based on the longest streak of days with at least one message. Only
				chats with the longest streak of at least 2 are included. As a tie-breaker, the longest
				streak count is used.
			</p>
		</template>
		<TableChat
			keys-label="No."
			:keys="positions"
			:chat-names="data.chat_name"
			:values-numeric="data.value"
			:values-displayed="valuesDisplayed"
			values-label="The longest streak length (count)"
		/>
	</DashboardBaseWrapper>
</template>

<script setup lang="ts">
import { computed, reactive } from 'vue';
import { dashboardElementsData } from '../../../utils/dashboardMeta';
import { genericGet } from '../../../utils/apiWrappers';
import type { ChatStreakStat } from '../../../utils/apiWrappers';
import { useFiltersStore } from '../../../stores/filters';
import { getIsDataLoaded } from '../../../utils/apiWrappers';

definePageMeta({
	layout: 'dashboard',
});

const filtersStore = useFiltersStore();

const meta = dashboardElementsData.get('longest_streaks')!;
let data: ChatStreakStat = {
	chat_name: [],
	value: [],
	count: [],
};

const valuesDisplayed = computed(() => data.value.map((len, i) => `${len} (${data.count[i]})`));
const positions = computed(() =>
	Array.from({ length: data.chat_name.length }, (_, i) => i + 1).map((p) => p.toString())
);

if (!(await getIsDataLoaded())) {
	await navigateTo('/');
} else {
	data = await genericGet<ChatStreakStat>(
		`${meta.group}${meta.routeRelative}`,
		filtersStore.getFilters
	);
}
</script>
