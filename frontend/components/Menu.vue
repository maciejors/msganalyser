<template>
	<aside class="flex flex-col gap-6 w-full">
		<section v-for="itemGroup in menuData" class="w-full">
			<h5>{{ itemGroup.name }}</h5>
			<div class="mt-2 border-l border-gray-800">
				<div v-for="menuItem in itemGroup.items">
					<MenuItem
						:href="`/dashboard${itemGroup.baseLink}${menuItem.link}`"
						:name="menuItem.name"
					/>
				</div>
			</div>
		</section>
	</aside>
</template>

<script setup lang="ts">
interface MenuItemData {
	name: string;
	link: string; // relative to /dashboard/[baseLink]
}

interface MenuItemGroupData {
	name: string;
	baseLink: string; // relative to /dashboard
	items: MenuItemData[];
}

const menuData: MenuItemGroupData[] = [
	{
		name: 'Overview',
		baseLink: '',
		items: [{ name: 'Overview', link: '' }],
	},
	{
		name: 'Activity analysis',
		baseLink: '/activity',
		items: [
			{ name: 'Messages by year', link: '/msg_by_year' },
			{ name: 'Messages by month', link: '/msg_by_month' },
			{ name: 'Average messages by calendar month', link: '/avg_msg_by_calendar_month' },
			{ name: 'Messages by day', link: '/msg_by_day' },
			{ name: 'Messages by time of day', link: '/msg_by_time_of_day' },
		],
	},
	{
		name: 'Chat rankings',
		baseLink: '/chats',
		items: [
			{ name: 'Top chats by year', link: '/top_chats_by_year' },
			{ name: 'Top chats by month', link: '/top_chats_by_month' },
			{ name: 'Top chats by day', link: '/top_chats_by_day' },
			{ name: 'Chat of the day', link: '/chat_of_the_day_counts' },
			{ name: 'Top messages count', link: '/top_msg_count' },
			{ name: 'Top media count', link: '/top_media_count' },
			{ name: 'Top calls count', link: '/top_calls_count' },
			{ name: 'Top calls duration', link: '/top_calls_duration' },
			{ name: 'Days with a message', link: '/days_with_msg_count' },
			{ name: 'Longest streaks', link: '/longest_streaks' },
		],
	},
];
</script>

<style scoped></style>
