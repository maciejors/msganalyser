<template>
	<span class="block border-gray-50 rounded-[100%] border-b-transparent animate-spin" />
</template>

<script setup lang="ts">
const props = defineProps({
	size: { type: String, required: true },
	width: { type: String, required: true },
});
</script>

<style scoped>
span {
	height: v-bind('props.size');
	width: v-bind('props.size');
	border-width: v-bind('props.width');
}
</style>
