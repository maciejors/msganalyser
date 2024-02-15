export function getPrettyDuration(timeIsSeconds: number) {
	const fullHours = Math.floor(timeIsSeconds / 3600);
	const remainderFullMinutes = Math.floor(timeIsSeconds / 60) % 60;
	const remainderSeconds = timeIsSeconds % 60;
	let result = `${remainderSeconds}s`;
	if (remainderFullMinutes > 0) {
		result = `${remainderFullMinutes}m ${result}`;
	}
	if (fullHours > 0) {
		result = `${fullHours}h ${result}`;
	}
	return result;
}
