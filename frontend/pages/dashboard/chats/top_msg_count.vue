<template>
	<DashboardGenericChatRanking
		dashboard-element-id="top_msg_count"
		ranking-description="The ranking of chats based on the total number of messages."
		values-label="Total number of messages"
	/>
</template>

<script setup lang="ts">
definePageMeta({
	layout: 'dashboard',
});
</script>
