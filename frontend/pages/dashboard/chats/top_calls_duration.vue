<template>
	<DashboardGenericChatRanking
		dashboard-element-id="top_calls_duration"
		ranking-description="The ranking of chats based on the total duration of calls."
		values-label="Total duration of calls"
		:values-displayed-mapper="valuesDisplayedMapper"
	/>
</template>

<script setup lang="ts">
import type { ChatStat } from '../../../utils/apiWrappers';

definePageMeta({
	layout: 'dashboard',
});

function valuesDisplayedMapper(data: ChatStat): string[] {
	const prettyDurations = data.value.map((timeIsSeconds) => {
		const fullHours = Math.floor(timeIsSeconds / 3600);
		const remainderFullMinutes = Math.floor(timeIsSeconds / 60) % 60;
		const remainderSeconds = timeIsSeconds % 60;
		let result = `${remainderSeconds}s`;
		if (remainderFullMinutes > 0) {
			result = `${remainderFullMinutes}m ${result}`;
		}
		if (fullHours > 0) {
			result = `${fullHours}h ${result}`;
		}
		return result;
	});
	return prettyDurations;
}
</script>
