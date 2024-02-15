<template>
	<div
		class="h-full flex flex-col justify-start items-center gap-2 p-4 border border-gray-500 rounded-xl"
	>
		<p class="font-bold text-gray-50">{{ name }}</p>
		<div class="h-full flex flex-col justify-center">
			<p class="text-2xl font-light text-primaryLight text-center">{{ value }}</p>
		</div>
	</div>
</template>

<script setup lang="ts">
defineProps({
	name: {
		type: String,
		required: true,
	},
	value: {
		type: String,
		required: true,
	},
});
</script>
