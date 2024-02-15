<template>
	<DashboardGenericActivity
		dashboard-element-id="avg_msg_by_calendar_month"
		plot-description="This plot shows how many messages on average have been sent and/or received in each calendar
	month."
		bar-values-label="Average messages count"
	/>
</template>

<script setup lang="ts">
definePageMeta({
	layout: 'dashboard',
});
</script>
