<template>
	<NuxtLink
		:to="props.href"
		class="block w-full my-2 pl-3 border-l border-gray-800 hover:text-gray-300 hover:border-gray-300 -translate-x-[1px]"
		:class="{ active: active[0] }"
	>
		<p>{{ props.name }}</p>
	</NuxtLink>
</template>

<script setup lang="ts">
import { reactive } from 'vue';

const props = defineProps({
	href: {
		type: String,
		required: true,
	},
	name: {
		type: String,
		required: true,
	},
});

const route = useRoute();
let active = reactive([false]);

watch(
	() => route.name,
	() => {
		const elementHrefMerged = props.href.replaceAll('/', '');
		const routeNameMerged = route.name!.toString().replaceAll('-', '');
		active[0] = elementHrefMerged === routeNameMerged;
	},
	{ immediate: true }
);
</script>

<style scoped>
.active {
	@apply border-primaryLight text-primaryLight;
}
</style>
