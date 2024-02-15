<template>
	<DashboardBaseWrapper :dashboard-element="meta">
		<template v-slot:description>
			<p>
				Welcome to the dashboard! Feel free to browse various analysis by exploring different tabs
				listed on the left-hand side. You can also filter your data - filtering options can be
				viewed by pressing the "Filter input data" button in the top-right corner. If you wish to
				change data anonymisation options, or simply load completely different data, you can go back
				to the setup page by pressing the "Go back to the setup page" link on the navigation bar.
			</p>
			<p>Here are some general statistics to get you started:</p>
		</template>
		<div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-12">
			<OverviewStat name="Total message count" :value="data.totalMsgCount" class="col-span-1" />
			<OverviewStat name="Total media count" :value="data.totalMediaCount" class="col-span-1" />
			<OverviewStat name="Total calls count" :value="data.totalCallsCount" class="col-span-1" />
			<OverviewStat
				name="Total calls duration"
				:value="data.totalCallsDuration"
				class="col-span-1"
			/>
			<OverviewStat name="Favourite chat" :value="data.favouriteChat" class="col-span-1" />
			<OverviewStat name="Most active day" :value="data.mostActiveDay" class="col-span-1" />
		</div>
	</DashboardBaseWrapper>
</template>

<script setup lang="ts">
import type { OverviewData } from '~/utils/apiWrappers';
import { genericGet } from '~/utils/apiWrappers';
import { getPrettyDuration } from '~/utils/formatting';

definePageMeta({
	layout: 'dashboard',
});

const filtersStore = useFiltersStore();
const meta = dashboardElementsData.get('overview')!;

const data = {
	totalMsgCount: '-',
	totalCallsCount: '-',
	totalCallsDuration: '-',
	totalMediaCount: '-',
	favouriteChat: '-',
	mostActiveDay: '-',
};

if (!(await getIsDataLoaded())) {
	await navigateTo('/');
} else {
	const fetchedData = await genericGet<OverviewData>(
		`${meta.group}${meta.routeRelative}`,
		filtersStore.getFilters
	);
	data.totalMsgCount = fetchedData.total_msg_count[0].toString();
	data.totalMediaCount = fetchedData.total_media_count[0].toString();
	data.totalCallsCount = fetchedData.total_calls_count[0].toString();
	data.totalCallsDuration = getPrettyDuration(fetchedData.total_calls_duration_s[0]);
	data.favouriteChat = fetchedData.favourite_chat[0];
	data.mostActiveDay = fetchedData.most_active_day[0];
}
</script>
