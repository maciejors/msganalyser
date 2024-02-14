<template>
	<nav>
		<div class="col-start-2 col-span-10 flex flex-row justify-between items-center py-4">
			<h1>msganalyser</h1>
			<div class="flex flex-row items-center gap-8">
				<p>
					<NuxtLink to="/" class="link-btn text-lg">Go back to the setup page</NuxtLink>
				</p>
				<button @click="showFilters" class="btn"><filter-icon /> Filter input data</button>
			</div>
		</div>
	</nav>
	<Filters
		@hideFilters="hideFilters"
		:class="{ 'translate-x-96': !areFiltersVisible }"
		class="transition-transform ease-out"
	/>
	<main class="grid grid-cols-12 gap-2 mb-16">
		<Menu class="col-start-2 col-span-2" />
		<div class="col-span-8">
			<slot />
		</div>
	</main>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import FilterIcon from 'vue-material-design-icons/Filter.vue';
import { getIsDataLoaded } from '../utils/apiWrappers';

if (!(await getIsDataLoaded())) {
	await navigateTo('/');
}

const areFiltersVisible = ref(false);

function showFilters() {
	areFiltersVisible.value = true;
}

function hideFilters() {
	areFiltersVisible.value = false;
}
</script>

<style scoped>
nav {
	@apply grid grid-cols-12 gap-2;
	@apply sticky top-0 w-full z-40 mb-4;
	@apply border-b border-gray-900 bg-black bg-opacity-25 backdrop-blur;
}
</style>
