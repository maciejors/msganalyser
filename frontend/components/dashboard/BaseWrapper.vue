<template>
	<main class="w-full flex flex-col gap-8">
		<header class="flex flex-col gap-2">
			<h5>{{ dashboardGroupsData.get(dashboardElement.group)!.name }}</h5>
			<h2>{{ dashboardElement.name }}</h2>
		</header>
		<div class="flex flex-col gap-1 text-justify">
			<slot name="description" />
		</div>
		<slot />
	</main>
</template>

<script setup lang="ts">
import type { DashboardElement } from '../../utils/dashboardMeta';
import { dashboardGroupsData } from '../../utils/dashboardMeta';

const props = defineProps({
	dashboardElement: {
		required: true,
	},
});

const dashboardElement = props.dashboardElement as DashboardElement;
</script>
