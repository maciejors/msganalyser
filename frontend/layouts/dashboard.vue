<template>
	<div class="max-h-full">
		<nav
			class="sticky top-0 w-full z-40 responsive-side-padding border-b border-gray-900 bg-black bg-opacity-25 backdrop-blur"
		>
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
		<main class="responsive-side-padding mb-16">
			<Menu class="fixed max-w-40 lg:max-w-64 overflow-y-auto pt-4 pb-12 pr-2" />
			<div class="pl-44 lg:pl-72 pt-4">
				<slot />
			</div>
		</main>
	</div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import FilterIcon from 'vue-material-design-icons/Filter.vue';

const areFiltersVisible = ref(false);

function showFilters() {
	areFiltersVisible.value = true;
}

function hideFilters() {
	areFiltersVisible.value = false;
}
</script>

<style scoped>
main aside {
	max-height: calc(100% - 5em);
}

.responsive-side-padding {
	@apply px-8 md:px-16 lg:px-24 xl:px-32;
}
</style>
