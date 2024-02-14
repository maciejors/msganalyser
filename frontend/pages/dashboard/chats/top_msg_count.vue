<template>
	<DashboardGenericChatRanking
		dashboardElementId="top_msg_count"
		rankingDescription="The ranking of chats based on the total number of messages."
		valuesLabel="Total number of messages"
	/>
</template>

<script setup lang="ts">
definePageMeta({
	layout: 'dashboard',
});
</script>
