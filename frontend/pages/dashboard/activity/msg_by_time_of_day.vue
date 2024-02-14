<template>
	<DashboardGenericActivity
		dashboardElementId="msg_by_time_of_day"
		plotDescription="This plot shows how many messages have been sent and/or received at each time of the day.
				The values on the x-axis represent hours on the clock. For example, a value of 13
				corresponds to the time period between 13:00 (inclusive) and 14:00 (exclusive)."
		barValuesLabel="Messages count"
	/>
</template>

<script setup lang="ts">
definePageMeta({
	layout: 'dashboard',
});
</script>
