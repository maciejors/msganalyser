<template>
	<nav>
		<div class="col-start-2 col-span-10 flex flex-row justify-between items-center py-4">
			<h1>msganalyser</h1>
			<p>
				<NuxtLink to="/" class="link-btn text-lg">Go back to the setup page</NuxtLink>
			</p>
		</div>
	</nav>
	<main class="grid grid-cols-12 gap-2">
		<Menu class="col-start-2 col-span-2" />
		<div class="col-span-8">
			<slot />
		</div>
	</main>
</template>

<script setup lang="ts">
import { getIsDataLoaded } from '../utils/apiWrappers';

if (!(await getIsDataLoaded())) {
	await navigateTo('/');
}
</script>

<style scoped>
nav {
	@apply grid grid-cols-12 gap-2;
	@apply sticky top-0 w-full z-40 mb-4;
	@apply border-b border-gray-900 bg-black bg-opacity-25 backdrop-blur;
}
</style>
