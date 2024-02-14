<template>
	<DashboardGenericActivity
		dashboardElementId="avg_msg_by_calendar_month"
		plotDescription="This plot shows how many messages on average have been sent and/or received in each calendar
	month."
		barValuesLabel="Average messages count"
	/>
</template>

<script setup lang="ts">
definePageMeta({
	layout: 'dashboard',
});
</script>
