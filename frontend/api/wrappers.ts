import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:8000/api';

/**
 * @returns Whether or not the data has been loaded successfully.
 */
export async function loadData(dataPath: string): Promise<boolean> {
	const response = await axios.put('/setup', {
		data_path: dataPath,
	});
	return response.status === 200;
}
