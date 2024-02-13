<template>
	<aside class="flex flex-col gap-6 w-full">
		<section v-for="itemGroup in menuItemGroups" class="w-full">
			<h6>{{ itemGroup.name }}</h6>
			<div class="mt-2 border-l border-gray-800">
				<div v-for="itemId in itemGroup.elementIds">
					<MenuItem
						:href="`/dashboard${itemGroup.routeRelative}${dashboardElementsData.get(itemId)!.routeRelative}`"
						:name="dashboardElementsData.get(itemId)!.name"
					/>
				</div>
			</div>
		</section>
	</aside>
</template>

<script setup lang="ts">
import {
	dashboardGroupsOrder,
	dashboardGroupsData,
	dashboardElementsData,
} from '../utils/dashboardMeta';

const menuItemGroups = dashboardGroupsOrder.map((id) => dashboardGroupsData.get(id)!);
</script>

<style scoped></style>
