import axios from 'axios';

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

export async function getMsgByYear(): Promise<DatetimeActivityStat> {
	const response = await axios.get('/activity/msg_by_year');
	return response.data;
}
