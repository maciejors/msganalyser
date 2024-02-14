<template>
	<DashboardGenericActivity
		dashboardElementId="msg_by_day"
		plotDescription="This plot shows how many messages have been sent and/or received on each day."
		barValuesLabel="Messages count"
	/>
</template>

<script setup lang="ts">
definePageMeta({
	layout: 'dashboard',
});
</script>
