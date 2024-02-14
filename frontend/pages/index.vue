<template>
	<main class="flex flex-col items-center pt-4 gap-4 px-2">
		<h2>Welcome to <span class="app-name">msganalyser</span></h2>
		<form @submit.prevent="onConfirm">
			<h3>Setup</h3>
			<section>
				<h4>Path to the folder with Facebook data:</h4>
				<input type="text" v-model="pathToData" />
			</section>
			<section>
				<h4>Data anonymisation options:</h4>
				<div v-for="anonOpt in anonOptionsDetails">
					<div class="flex flex-row items-center">
						<input
							type="checkbox"
							:id="anonOpt.value"
							:value="anonOpt.value"
							v-model="selectedAnonOptions"
						/>
						<label :for="anonOpt.value" class="pl-2 cursor-pointer">{{ anonOpt.title }}</label>
					</div>
					<p class="text-gray-500 ml-6">{{ anonOpt.description }}</p>
				</div>
			</section>
			<div class="flex flex-col items-center gap-1">
				<button class="btn font-bold h-16 w-36" :disabled="isDataLoading">
					<Spinner v-if="isDataLoading" size="32px" width="4px" />
					<span v-else>Load your data</span>
				</button>
				<p class="text-red-400">
					<span :class="{ 'text-transparent': !isLoadingDataFailed }">
						Facebook data not found at the specified location
					</span>
				</p>
			</div>
		</form>
		<div v-if="isDataLoaded" class="flex flex-col items-center gap-1">
			<h4>
				Your data is now loaded!
				<NuxtLink to="/dashboard" class="link-btn font-bold">
					Click here to go to the analysis dashboard
				</NuxtLink>
			</h4>
		</div>
	</main>
</template>

<script lang="ts">
import { loadData, getIsDataLoaded } from '../utils/apiWrappers';

interface AnonymisationOptionDetails {
	value: string;
	title: string;
	description: string;
}

export default {
	mounted() {
		getIsDataLoaded().then((v) => (this.isDataLoaded = v));
	},

	data() {
		return {
			isDataLoading: false,
			isDataLoaded: false,
			isLoadingDataFailed: false,
			pathToData: './data',
			selectedAnonOptions: ['purgemsg'] as string[],
			anonOptionsDetails: [
				{
					value: 'purgemsg',
					title: 'Purge messages contents',
					description:
						'Replaces all messages contents with a blank text. ' +
						'This will reduce the size of the data once it is extracted. ' +
						'Messages contents are not used anywhere in this app, so it is ' +
						'recommended to select this option.',
				},
				{
					value: 'chatnames',
					title: 'Reset chat names',
					description:
						'Replaces all chat and sender names with random names. ' +
						'This will make the results significanlty more anonymous, ' +
						'however it makes chat analysis useless, so select this option ' +
						'if you are only interested in activity analysis.',
				},
			] as AnonymisationOptionDetails[],
		};
	},

	methods: {
		async onConfirm() {
			this.isDataLoading = true;
			const purgeContents = this.selectedAnonOptions.includes('purgemsg');
			const replaceNames = this.selectedAnonOptions.includes('chatnames');
			const isSuccess = await loadData(this.pathToData, purgeContents, replaceNames);
			console.log('hello');
			if (isSuccess) {
				this.isLoadingDataFailed = false;
				this.isDataLoaded = true;
			} else {
				this.isLoadingDataFailed = true;
			}
			this.isDataLoading = false;
		},
	},
};
</script>

<style scoped>
.app-name {
	@apply font-normal;
}

form {
	@apply border border-gray-400 rounded-xl px-4 pt-4 pb-2 mt-4 max-w-4xl;
	@apply flex flex-col gap-6;
}

form section {
	@apply w-full flex flex-col gap-1;
}
</style>
