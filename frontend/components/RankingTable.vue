<template>
	<ol class="flex flex-col gap-4 w-full">
		<div class="ranking-tile-layout">
			<p class="col-span-1">No.</p>
			<p class="col-span-4">Chat name</p>
			<p class="col-span-7">{{ valuesLabel }}</p>
		</div>
		<li v-for="item in items" class="ranking-tile">
			<p class="col-span-1">{{ item.position }}</p>
			<p class="col-span-4">{{ item.key }}</p>
			<p class="col-span-1">{{ item.valueDisplayed }}</p>
			<div
				class="col-span-6 bar"
				:style="`width: ${(item.valueNumeric / valuesNumericSorted[0]) * 100}%;`"
			></div>
		</li>
	</ol>
</template>

<script setup lang="ts">
import { computed } from 'vue';

const props = defineProps({
	keys: {
		type: Array<String>,
		required: true,
	},
	valuesLabel: {
		type: String,
		required: true,
	},
	valuesNumericSorted: {
		type: Array<number>,
		required: true,
	},
	valuesDisplayed: {
		type: Array<string>,
		required: false,
	},
});

const items = computed(() => {
	return props.keys.map((key, i) => ({
		position: i + 1,
		key,
		valueNumeric: props.valuesNumericSorted[i],
		valueDisplayed: props.valuesDisplayed ? props.valuesDisplayed[i] : props.valuesNumericSorted[i],
	}));
});
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
