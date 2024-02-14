import axios from 'axios';
import type { Filters } from './filtersInterface';

axios.defaults.baseURL = 'http://localhost:8000/api';

interface DatetimeActivityStat {
	key: string[] | number[];
	value: number[];
}

interface DateChatStat extends DatetimeActivityStat {
	chat_name: string[];
}

interface ChatStat {
	chat_name: string[];
	value: number[];
}

interface ChatStreakStat extends ChatStat {
	count: number[];
}

/**
 * @returns Whether or not the data has been loaded successfully.
 */
export async function loadData(
	dataPath: string,
	purgeContents: boolean,
	replaceNames: boolean
): Promise<boolean> {
	try {
		await axios.put('/setup', {
			data_path: dataPath,
			purge_contents: purgeContents,
			replace_names: replaceNames,
		});
	} catch (_) {
		return false;
	}
	return true;
}

/**
 * @returns Whether or not the data is loaded.
 */
export async function getIsDataLoaded(): Promise<boolean> {
	try {
		await axios.get('/setup');
	} catch (_) {
		return false;
	}
	return true;
}

function apiWrapperFactory<T>(endpoint: string): (filters: Filters) => Promise<T> {
	const wrapper = async (filters: Filters) => {
		const params = {
			timestamp_ms_from: filters.timestampMsFrom,
			timestamp_ms_to: filters.timestampMsTo,
			chat_type: filters.chatType,
			message_type: filters.messageType,
		};
		const response = await axios.get(endpoint, { params });
		return response.data as T;
	};
	return wrapper;
}

export const getMsgByYear = apiWrapperFactory<DatetimeActivityStat>('/activity/msg_by_year');
export const getMsgByMonth = apiWrapperFactory<DatetimeActivityStat>('/activity/msg_by_month');
export const getAvgMsgByCalendarMonth = apiWrapperFactory<DatetimeActivityStat>(
	'/activity/avg_msg_by_calendar_month'
);
export const getMsgByDay = apiWrapperFactory<DatetimeActivityStat>('/activity/msg_by_day');
export const getMsgByTimeOfDay = apiWrapperFactory<DatetimeActivityStat>(
	'/activity/msg_by_time_of_day'
);

export const getTopMsgCount = apiWrapperFactory<ChatStat>('/chats/top_msg_count');
export const getTopMediaCount = apiWrapperFactory<ChatStat>('/chats/top_media_count');
export const getTopCallsCount = apiWrapperFactory<ChatStat>('/chats/top_calls_count');
export const getTopCallsDuration = apiWrapperFactory<ChatStat>('/chats/top_calls_duration');
export const getChatOfTheDayCounts = apiWrapperFactory<ChatStat>('/chats/chat_of_the_day_counts');
export const getDaysWithMsgCounts = apiWrapperFactory<ChatStat>('/chats/days_with_msg_count');
export const getLongestStreaks = apiWrapperFactory<ChatStreakStat>('/chats/longest_streaks');
