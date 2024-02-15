<template>
	<DashboardGenericChatRanking
		dashboard-element-id="top_calls_count"
		ranking-description="The ranking of chats based on the total number of calls."
		values-label="Total number of calls"
	/>
</template>

<script setup lang="ts">
definePageMeta({
	layout: 'dashboard',
});
</script>
