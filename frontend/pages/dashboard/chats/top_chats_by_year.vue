<template>
	<DashboardGenericDateChat
		dashboard-element-id="top_chats_by_year"
		ranking-description="Chats with the most messages in each year."
		values-label="Number of messages in this chat in that year"
		dates-label="Year"
	/>
</template>

<script setup lang="ts">
definePageMeta({
	layout: 'dashboard',
});
</script>
