<template>
	<DashboardGenericActivity
		dashboard-element-id="msg_by_day"
		plot-description="This plot shows how many messages have been sent and/or received on each day."
		bar-values-label="Messages count"
	/>
</template>

<script setup lang="ts">
definePageMeta({
	layout: 'dashboard',
});
</script>
