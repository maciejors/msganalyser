export interface DashboardElement {
	routeRelative: string;
	name: string;
	group: string;
}

export interface DashboardGroup {
	routeRelative: string;
	name: string;
	elementIds: string[];
}

export const dashboardElementsData = new Map<string, DashboardElement>([
	['overview', { name: 'Overview', routeRelative: '', group: 'overview' }],
	['msg_by_year', { name: 'Messages by year', routeRelative: '/msg_by_year', group: 'activity' }],
	[
		'msg_by_month',
		{ name: 'Messages by month', routeRelative: '/msg_by_month', group: 'activity' },
	],
	[
		'avg_msg_by_calendar_month',
		{
			name: 'Average messages by calendar month',
			routeRelative: '/avg_msg_by_calendar_month',
			group: 'activity',
		},
	],
	['msg_by_day', { name: 'Messages by day', routeRelative: '/msg_by_day', group: 'activity' }],
	[
		'msg_by_time_of_day',
		{ name: 'Messages by time of day', routeRelative: '/msg_by_time_of_day', group: 'activity' },
	],
	[
		'top_chats_by_year',
		{ name: 'Top chats by year', routeRelative: '/top_chats_by_year', group: 'chats' },
	],
	[
		'top_chats_by_month',
		{ name: 'Top chats by month', routeRelative: '/top_chats_by_month', group: 'chats' },
	],
	[
		'top_chats_by_day',
		{ name: 'Top chats by day', routeRelative: '/top_chats_by_day', group: 'chats' },
	],
	[
		'chat_of_the_day_counts',
		{ name: 'Chat of the day', routeRelative: '/chat_of_the_day_counts', group: 'chats' },
	],
	[
		'top_msg_count',
		{ name: 'Top messages count', routeRelative: '/top_msg_count', group: 'chats' },
	],
	[
		'top_media_count',
		{ name: 'Top media count', routeRelative: '/top_media_count', group: 'chats' },
	],
	[
		'top_calls_count',
		{ name: 'Top calls count', routeRelative: '/top_calls_count', group: 'chats' },
	],
	[
		'top_calls_duration',
		{ name: 'Top calls duration', routeRelative: '/top_calls_duration', group: 'chats' },
	],
	[
		'days_with_msg_count',
		{ name: 'Days with a message', routeRelative: '/days_with_msg_count', group: 'chats' },
	],
	[
		'longest_streaks',
		{ name: 'Longest streaks', routeRelative: '/longest_streaks', group: 'chats' },
	],
]);

export const dashboardGroupsData = new Map<string, DashboardGroup>([
	[
		'overview',
		{
			name: 'Overview',
			routeRelative: '',
			elementIds: ['overview'],
		},
	],
	[
		'activity',
		{
			name: 'Activity analysis',
			routeRelative: '/activity',
			elementIds: [
				'msg_by_year',
				'msg_by_month',
				'avg_msg_by_calendar_month',
				'msg_by_day',
				'msg_by_time_of_day',
			],
		},
	],
	[
		'chats',
		{
			name: 'Chat rankings',
			routeRelative: '/chats',
			elementIds: [
				'top_chats_by_year',
				'top_chats_by_month',
				'top_chats_by_day',
				'chat_of_the_day_counts',
				'top_msg_count',
				'top_media_count',
				'top_calls_count',
				'top_calls_duration',
				'days_with_msg_count',
				'longest_streaks',
			],
		},
	],
]);

export const dashboardGroupsOrder: string[] = ['overview', 'activity', 'chats'];
