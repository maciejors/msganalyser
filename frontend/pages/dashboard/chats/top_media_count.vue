<template>
	<DashboardGenericChatRanking
		dashboardElementId="top_media_count"
		rankingDescription="The ranking of chats based on the total number of media (photos, videos and files)."
		valuesLabel="Total number of media"
	/>
</template>

<script setup lang="ts">
definePageMeta({
	layout: 'dashboard',
});
</script>
