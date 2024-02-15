<template>
	<DashboardBaseWrapper :dashboard-element="meta">
		<template v-slot:description>
			<p>{{ props.rankingDescription }}</p>
		</template>
		<TableChat
			:keys-label="datesLabel"
			:keys="data.datetime_key.map((d) => d.toString())"
			:chat-names="data.chat_name"
			:values-numeric="data.value"
			:values-displayed="valuesDisplayed"
			:values-label="valuesLabel"
			:initial-max-items="20"
		/>
	</DashboardBaseWrapper>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { dashboardElementsData } from '../../utils/dashboardMeta';
import { genericGet } from '../../utils/apiWrappers';
import type { DateChatStat } from '../../utils/apiWrappers';
import { useFiltersStore } from '../../stores/filters';
import { getIsDataLoaded } from '../../utils/apiWrappers';

const props = defineProps({
	dashboardElementId: {
		type: String,
		required: true,
	},
	rankingDescription: {
		type: String,
		required: true,
	},
	datesLabel: {
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
		default: <T extends DateChatStat>(data: T) => data.value,
	},
});
const filtersStore = useFiltersStore();

const meta = dashboardElementsData.get(props.dashboardElementId)!;
let data: DateChatStat = {
	datetime_key: [],
	value: [],
	chat_name: [],
};
const valuesDisplayed = computed(() => props.valuesDisplayedMapper(data));

if (!(await getIsDataLoaded())) {
	await navigateTo('/');
} else {
	data = await genericGet<DateChatStat>(
		`${meta.group}${meta.routeRelative}`,
		filtersStore.getFilters
	);
}
</script>
