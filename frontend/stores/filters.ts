import { defineStore } from 'pinia';
import type { Filters } from '../utils/filtersInterface';

function dateStrToTimestampMs(dateStr: string, endOfDay: boolean): number {
	if (dateStr === '') {
		return -1;
	}
	const date = new Date(dateStr);
	if (endOfDay) {
		date.setHours(23, 59, 59, 999);
	}
	const timestampMs = date.getTime();
	return timestampMs;
}

export const useFiltersStore = defineStore('filtersStore', {
	persist: true,
	state: () => ({
		dateFrom: '',
		dateTo: '',
		chatType: 'all',
		messageType: 'all',
	}),
	getters: {
		getFilters(): Filters {
			return {
				timestampMsFrom: dateStrToTimestampMs(this.dateFrom, false),
				timestampMsTo: dateStrToTimestampMs(this.dateTo, true),
				chatType: this.chatType,
				messageType: this.messageType,
			};
		},
	},
	actions: {
		setFilters(
			newDateFrom: string,
			newDateTo: string,
			newChatType: string,
			newMessageType: string
		) {
			this.dateFrom = newDateFrom;
			this.dateTo = newDateTo;
			this.chatType = newChatType;
			this.messageType = newMessageType;
		},
	},
});
