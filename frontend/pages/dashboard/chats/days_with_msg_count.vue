<template>
	<DashboardGenericChatRanking
		dashboardElementId="days_with_msg_count"
		rankingDescription="The ranking of chats based on the number of days with at least one message."
		valuesLabel="Number of days with at least one message"
	/>
</template>

<script setup lang="ts">
definePageMeta({
	layout: 'dashboard',
});
</script>
