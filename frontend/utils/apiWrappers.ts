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
export async function loadData(dataPath: string): Promise<boolean> {
	try {
		await axios.put('/setup', {
			data_path: dataPath,
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
