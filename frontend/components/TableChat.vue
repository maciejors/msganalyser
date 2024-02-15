<template>
	<ol class="flex flex-col gap-4 w-full">
		<div class="ranking-tile-layout">
			<p class="col-span-1">{{ keysLabel }}</p>
			<p class="col-span-4">Chat name</p>
			<p class="col-span-7">{{ valuesLabel }}</p>
		</div>
		<li v-for="item in items" class="ranking-tile">
			<p class="col-span-1">{{ item.key }}</p>
			<p class="col-span-4">{{ item.chatName }}</p>
			<p class="col-span-1">{{ item.valueDisplayed }}</p>
			<div class="col-span-6 bar" :style="`width: ${(item.valueNumeric / maxValue) * 100}%;`"></div>
		</li>
	</ol>
	<div class="flex flex-row justify-center">
		<button @click="showMoreItems" class="btn w-52 h-12" v-show="displayedItemsCount < keys.length">
			Show more
		</button>
	</div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';

const props = defineProps({
	keysLabel: {
		type: String,
		required: true,
	},
	keys: {
		type: Array<String>,
		required: true,
	},
	chatNames: {
		type: Array<String>,
		required: true,
	},
	valuesLabel: {
		type: String,
		required: true,
	},
	valuesNumeric: {
		type: Array<number>,
		required: true,
	},
	valuesDisplayed: {
		type: Array<string>,
		required: false,
	},
	initialMaxItems: {
		type: Number,
		required: false,
	},
});

const displayedItemsCount = ref(props.initialMaxItems ? props.initialMaxItems : props.keys.length);

function showMoreItems() {
	if (props.initialMaxItems) {
		displayedItemsCount.value += props.initialMaxItems;
	}
}

const items = computed(() => {
	return props.keys
		.map((key, i) => ({
			key,
			chatName: props.chatNames[i],
			valueNumeric: props.valuesNumeric[i],
			valueDisplayed: props.valuesDisplayed ? props.valuesDisplayed[i] : props.valuesNumeric[i],
		}))
		.slice(0, displayedItemsCount.value);
});

const maxValue = Math.max(...props.valuesNumeric);
</script>

<style scoped>
.ranking-tile-layout {
	@apply grid grid-cols-12 gap-2 px-4 items-center;
}

.ranking-tile {
	@apply bg-black border border-gray-700 rounded-lg py-4;
	@apply ranking-tile-layout;
}

.bar {
	@apply bg-primary h-3;
}
</style>
