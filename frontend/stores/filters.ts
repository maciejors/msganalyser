import { defineStore } from 'pinia';
import type { Filters } from '../utils/filtersInterface';

function dateStrToTimestampMs(dateStr: string): number {
	if (dateStr === '') {
		return -1;
	}
	const date = new Date(dateStr);
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
				timestampMsFrom: dateStrToTimestampMs(this.dateFrom),
				timestampMsTo: dateStrToTimestampMs(this.dateTo),
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
