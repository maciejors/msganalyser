<template>
	<DashboardGenericChatTabular
		keys-label="No."
		:dashboard-element-id="dashboardElementId"
		:ranking-description="rankingDescription"
		:values-label="valuesLabel"
		:values-displayed-mapper="valuesDisplayedMapper"
	/>
</template>

<script setup lang="ts">
defineProps({
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
</script>
