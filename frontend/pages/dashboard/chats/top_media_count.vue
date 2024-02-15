<template>
	<DashboardGenericChatRanking
		dashboard-element-id="top_media_count"
		ranking-description="The ranking of chats based on the total number of media (photos, videos and files)."
		values-label="Total number of media"
	/>
</template>

<script setup lang="ts">
definePageMeta({
	layout: 'dashboard',
});
</script>
