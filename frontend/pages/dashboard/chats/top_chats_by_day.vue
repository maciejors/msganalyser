<template>
	<DashboardGenericDateChat
		dashboard-element-id="top_chats_by_day"
		ranking-description="Chats with the most messages on each day."
		values-label="Number of messages in this chat on that day"
		dates-label="Day"
	/>
</template>

<script setup lang="ts">
definePageMeta({
	layout: 'dashboard',
});
</script>
