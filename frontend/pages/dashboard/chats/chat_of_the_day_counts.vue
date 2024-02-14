<template>
	<DashboardGenericChatRanking
		dashboardElementId="chat_of_the_day_counts"
		rankingDescription="Ranking of chats based on how many times a chat was the chat of the day, i.e. had the most
			messages of all chats on a day."
		valuesLabel="'Chat of the day' count"
	/>
</template>

<script setup lang="ts">
definePageMeta({
	layout: 'dashboard',
});
</script>
