<template>
	<DashboardGenericChatRanking
		dashboardElementId="top_calls_count"
		rankingDescription="The ranking of chats based on the total number of calls."
		valuesLabel="Total number of calls"
	/>
</template>

<script setup lang="ts">
definePageMeta({
	layout: 'dashboard',
});
</script>
