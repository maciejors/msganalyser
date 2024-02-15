<template>
	<DashboardBaseWrapper :dashboard-element="meta">
		<template v-slot:description>
			<p>{{ props.rankingDescription }}</p>
		</template>
		<TableChat
			keys-label="No."
			:keys="positions"
			:chat-names="data.chat_name"
			:values-numeric="data.value"
			:values-displayed="valuesDisplayed"
			:values-label="valuesLabel"
			:initial-max-items="30"
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
const positions = Array.from({ length: data.chat_name.length }, (_, i) => i + 1).map((p) =>
	p.toString()
);
</script>
