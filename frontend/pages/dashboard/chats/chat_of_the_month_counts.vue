<template>
	<DashboardGenericChatRanking
		dashboard-element-id="chat_of_the_month_counts"
		ranking-description="Ranking of chats based on how many times a chat was the chat of the month, i.e. had the most
			messages of all chats in a month."
		values-label="'Chat of the month' count"
	/>
</template>

<script setup lang="ts">
definePageMeta({
	layout: 'dashboard',
});
</script>
