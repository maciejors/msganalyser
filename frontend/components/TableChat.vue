<template>
	<NoDataIndicator v-if="items.length === 0" />
	<div v-else>
		<ol class="flex flex-col gap-4 w-full">
			<div class="ranking-tile-layout text-gray-300 font-bold">
				<p class="key-col">{{ keysLabel }}</p>
				<p class="chat-name-col">Chat name</p>
				<p class="value-col">{{ valuesLabel }}</p>
			</div>
			<li v-for="item in items" class="ranking-tile">
				<p class="key-col">{{ item.key }}</p>
				<p class="chat-name-col">{{ item.chatName }}</p>
				<div class="value-col grid grid-cols-6 h-full items-center">
					<p class="col-span-1">{{ item.valueDisplayed }}</p>
					<div
						class="col-span-5 bar"
						:style="`width: ${(item.valueNumeric / maxValue) * 100}%;`"
					></div>
				</div>
			</li>
			<div class="flex flex-row justify-center">
				<button
					@click="showMoreItems"
					class="btn w-52 h-12"
					v-show="displayedItemsCount < keys.length"
				>
					Show more
				</button>
			</div>
		</ol>
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
			valueDisplayed: props.valuesDisplayed
				? props.valuesDisplayed[i]
				: props.valuesNumeric[i].toString(),
		}))
		.slice(0, displayedItemsCount.value);
});

const maxValue = Math.max(...props.valuesNumeric);
</script>

<style scoped>
.ranking-tile-layout {
	@apply grid grid-cols-10 gap-2 px-4 items-center;
}

.key-col {
	@apply col-span-2 xl:col-span-1;
}

.chat-name-col {
	@apply col-span-3;
}

.value-col {
	@apply col-span-5 xl:col-span-6;
}

.ranking-tile {
	@apply bg-black border border-gray-700 rounded-lg py-4;
	@apply ranking-tile-layout;
}

.bar {
	@apply bg-primary h-3;
}
</style>
