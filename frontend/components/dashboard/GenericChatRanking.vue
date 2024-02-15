<template>
	<DashboardBaseWrapper :dashboardElement="meta">
		<template v-slot:description>
			<p>{{ props.rankingDescription }}</p>
		</template>
		<TableChatRanking
			:keys="data.chat_name"
			:valuesNumericSorted="data.value"
			:valuesDisplayed="valuesDisplayed"
			:valuesLabel="valuesLabel"
		/>
	</DashboardBaseWrapper>
</template>

<script setup lang="ts">
import { dashboardElementsData } from '../../utils/dashboardMeta';
import { genericGet } from '../../utils/apiWrappers';
import type { ChatStat } from '../../utils/apiWrappers';
import { useFiltersStore } from '../../stores/filters';

const props = defineProps({
	dashboardElementId: {
		type: String,
		required: true,
	},
	rankingDescription: {
		type: String,
		required: true,
	},
	valuesLabel: {
		type: String,
		required: true,
	},
	valuesDisplayedMapper: {
		type: Function,
		required: false,
		default: <T extends ChatStat>(data: T) => data.value,
	},
});

const filtersStore = useFiltersStore();

const meta = dashboardElementsData.get(props.dashboardElementId)!;
const data = await genericGet<ChatStat>(
	`${meta.group}${meta.routeRelative}`,
	filtersStore.getFilters
);
const valuesDisplayed = props.valuesDisplayedMapper(data);
</script>
