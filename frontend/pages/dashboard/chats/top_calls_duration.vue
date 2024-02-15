<template>
	<DashboardGenericChatRanking
		dashboard-element-id="top_calls_duration"
		ranking-description="The ranking of chats based on the total duration of calls."
		values-label="Total duration of calls"
		:values-displayed-mapper="valuesDisplayedMapper"
	/>
</template>

<script setup lang="ts">
import type { ChatStat } from '~/utils/apiWrappers';
import { getPrettyDuration } from '~/utils/formatting';

definePageMeta({
	layout: 'dashboard',
});

function valuesDisplayedMapper(data: ChatStat): string[] {
	const prettyDurations = data.value.map(getPrettyDuration);
	return prettyDurations;
}
</script>
