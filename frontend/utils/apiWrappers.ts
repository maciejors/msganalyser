import axios from 'axios';
import type { Filters } from './filtersInterface';

axios.defaults.baseURL = 'http://localhost:8000/api';

export interface DatetimeActivityStat {
	key: string[] | number[];
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
