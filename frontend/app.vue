<template>
	<div>
		<NuxtLayout>
			<NuxtPage />
		</NuxtLayout>
	</div>
</template>

<script setup lang="ts">
import {
	Chart as ChartJS,
	Title,
	Tooltip,
	Legend,
	BarElement,
	CategoryScale,
	LinearScale,
} from 'chart.js';
import resolveConfig from 'tailwindcss/resolveConfig';
import tailwindConfig from './tailwind.config.js';

const twFullConfig = resolveConfig(tailwindConfig);

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);
ChartJS.defaults.plugins.legend.display = false;
ChartJS.defaults.color = twFullConfig.theme.colors['gray'][400];
</script>
