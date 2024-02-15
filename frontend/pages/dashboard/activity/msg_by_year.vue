<template>
	<DashboardGenericActivity
		dashboard-element-id="msg_by_year"
		plot-description="This plot shows how many messages have been sent and/or received in each year."
		bar-values-label="Messages count"
	/>
</template>

<script setup lang="ts">
definePageMeta({
	layout: 'dashboard',
});
</script>
