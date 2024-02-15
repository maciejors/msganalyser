<template>
	<aside class="fixed top-0 right-0 bg-black z-40 h-full w-96 p-6 border-l border-gray-800">
		<form @submit.prevent="onSubmit" class="flex flex-col gap-8">
			<nav class="flex flex-row justify-between">
				<p @click="$emit('hideFilters')" class="btn"><close-icon /></p>
				<button @click="onClearFilters" class="text-red-500 hover:text-red-400">
					Clear filters
				</button>
			</nav>
			<section>
				<h4>Date range (inclusive):</h4>
				<ul class="flex flex-col gap-2">
					<li class="datepicker-container">
						<p>From:</p>
						<input type="date" v-model="dateFrom" />
					</li>
					<li class="datepicker-container">
						<p>To:</p>
						<input type="date" v-model="dateTo" />
					</li>
				</ul>
			</section>
			<section>
				<h4>Chat type:</h4>
				<div class="radio-container">
					<input type="radio" id="chatTypeAll" value="all" v-model="chatType" />
					<label for="chatTypeAll" class="pl-2 cursor-pointer">All</label>
				</div>
				<div class="radio-container">
					<input type="radio" id="chatTypePrivate" value="private" v-model="chatType" />
					<label for="chatTypePrivate" class="pl-2 cursor-pointer">Private</label>
				</div>
				<div class="radio-container">
					<input type="radio" id="chatTypeGroup" value="group" v-model="chatType" />
					<label for="chatTypeGroup" class="pl-2 cursor-pointer">Group</label>
				</div>
			</section>
			<section>
				<h4>Message type:</h4>
				<div class="radio-container">
					<input type="radio" id="messageTypeAll" value="all" v-model="messageType" />
					<label for="messageTypeAll" class="pl-2 cursor-pointer">All</label>
				</div>
				<div class="radio-container">
					<input type="radio" id="messageTypeSent" value="sent" v-model="messageType" />
					<label for="messageTypeSent" class="pl-2 cursor-pointer">Sent</label>
				</div>
				<div class="radio-container">
					<input type="radio" id="messageTypeReceived" value="received" v-model="messageType" />
					<label for="messageTypeReceived" class="pl-2 cursor-pointer">Received</label>
				</div>
			</section>
			<button @click="onApplyFilters" class="btn">Apply filters</button>
		</form>
	</aside>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import CloseIcon from 'vue-material-design-icons/Close.vue';
import { useFiltersStore } from '../stores/filters';

const filtersStore = useFiltersStore();

const dateFrom = ref(filtersStore.dateFrom);
const dateTo = ref(filtersStore.dateTo);
const chatType = ref(filtersStore.chatType);
const messageType = ref(filtersStore.messageType);

const emit = defineEmits(['hideFilters']);

function onClearFilters() {
	filtersStore.$reset();
}

function onApplyFilters() {
	filtersStore.setFilters(dateFrom.value, dateTo.value, chatType.value, messageType.value);
}

function onSubmit() {
	location.reload();
}
</script>

<style scoped>
form h4 {
	@apply mb-1;
}

.datepicker-container {
	@apply flex flex-row items-center gap-2 pl-1;
}

.radio-container {
	@apply flex flex-row items-center pl-1;
}
</style>
