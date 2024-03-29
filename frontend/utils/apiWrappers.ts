import axios from 'axios';
import type { Filters } from './filtersInterface';

axios.defaults.baseURL = 'http://localhost:8000/api';

export interface OverviewData {
	total_msg_count: number[];
	total_calls_count: number[];
	total_calls_duration_s: number[];
	total_media_count: number[];
	favourite_chat: string[];
	most_active_day: string[];
}

export interface DatetimeActivityStat {
	datetime_key: string[];
	value: number[];
}

export interface DateChatStat extends DatetimeActivityStat {
	chat_name: string[];
}

export interface ChatStat {
	chat_name: string[];
	value: number[];
}

export interface ChatStreakStat extends ChatStat {
	count: number[];
}

/**
 * @returns Path to compacted data if saved, otherwise an empty string.
 */
export async function loadData(
	dataPath: string,
	purgeContents: boolean,
	replaceNames: boolean,
	saveCompactedData: boolean
): Promise<string> {
	const response = await axios.put('/setup', {
		data_path: dataPath,
		purge_contents: purgeContents,
		replace_names: replaceNames,
		save_compact: saveCompactedData,
	});
	return response.data.path_to_compact;
}

/**
 * @returns Whether or not the data is loaded.
 */
export async function getIsDataLoaded(): Promise<boolean> {
	const response = await axios.get('/setup');
	return response.data.is_data_loaded;
}

export async function genericGet<T>(endpoint: string, filters: Filters): Promise<T> {
	const params = {
		timestamp_ms_from: filters.timestampMsFrom,
		timestamp_ms_to: filters.timestampMsTo,
		chat_type: filters.chatType,
		message_type: filters.messageType,
	};
	const response = await axios.get(endpoint, { params });
	return response.data as T;
}
