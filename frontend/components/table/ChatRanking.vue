<template>
	<TableBase
		keys-label="No."
		:keys="keys"
		:values-label="valuesLabel"
		:values-numeric-sorted="valuesNumericSorted"
		:values-displayed="valuesDisplayed"
	/>
</template>

<script setup lang="ts">
defineProps({
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
</script>
