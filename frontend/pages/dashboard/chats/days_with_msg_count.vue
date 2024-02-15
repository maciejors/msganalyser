<template>
	<DashboardGenericChatRanking
		dashboard-element-id="days_with_msg_count"
		ranking-description="The ranking of chats based on the number of days with at least one message."
		values-label="Number of days with at least one message"
	/>
</template>

<script setup lang="ts">
definePageMeta({
	layout: 'dashboard',
});
</script>
