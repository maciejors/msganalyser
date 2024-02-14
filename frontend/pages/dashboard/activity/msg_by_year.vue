<template>
	<DashboardGenericActivity
		dashboardElementId="msg_by_year"
		plotDescription="This plot shows how many messages have been sent and/or received in each year."
		barValuesLabel="Messages count"
	/>
</template>

<script setup lang="ts">
definePageMeta({
	layout: 'dashboard',
});
</script>
