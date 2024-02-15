<template>
	<DashboardGenericDateChat
		dashboard-element-id="top_chats_by_month"
		ranking-description="Chats with the most messages in each month."
		values-label="Number of messages in this chat in that month"
		dates-label="Month"
	/>
</template>

<script setup lang="ts">
definePageMeta({
	layout: 'dashboard',
});
</script>
