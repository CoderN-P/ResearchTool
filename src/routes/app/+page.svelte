<svelte:head>
	<title>About</title>
	<meta name="description" content="About this app" />
</svelte:head>

<script>
	import { Icon, MagnifyingGlass, PaperAirplane } from "svelte-hero-icons";
	import {fetchSummary} from "./fetchSummary.ts";

	let prompt = '';
	let input = '';
	let summaryData = null;

	function setPrompt(){
		prompt = input;
		summaryData = fetchSummary(input);
	}
</script>

<div class:items-center={!prompt} class:justify-center={!prompt} class="w-[calc(100%-64px)] flex flex-col h-[calc(100%-64px)] m-8 border border-gray-200 rounded-xl bg-white" >
	{#if prompt}
		{#await summaryData}
			<p class="text-2xl text-center">Loading...</p>
		{:then data}
			{#if data}
				{#each Object.keys(data) as key}
					{#if data[key] && data[key] !== "Failed to summarize article"}

					<div class="rounded-xl bg-gray-100 p-4 m-4">
						<div class="flex flex-row justify-between">
							<h2 class="text-2xl font-bold ">{data[key]["title"]}</h2>
							<h2 class="text-base font-bold text-blue-500 hover:text-blue-400">{data[key]["url"]}</h2>
						</div >
						<p class="text-lg ">{data[key]["summary"]}</p>
					</div>
					{/if}
				{/each}
			{:else}
				<p class="text-2xl text-center">No data found</p>
			{/if}
		{:catch error}
				<p class="text-2xl text-center">Error: {error.message}</p>
		{/await}
	{:else}
		<div class="w-full p-8 flex justify-center">
			<div class="w-full md:w-2/3   bg-gradient-to-r from-orange-400 to-red-500 rounded-full p-0.5">
				<div class="flex items-center justify-start bg-white rounded-full  p-4">
					<Icon src="{MagnifyingGlass}" class="w-6 h-6 text-gray-500"/>
					<input bind:value={input} placeholder="What do you want to research?" class="flex-grow mx-4"/>
					<button on:click={setPrompt}>
						<Icon src="{PaperAirplane}"  class="w-6 h-6 text-green-500 hover:fill-green-500"/>
					</button>

				</div>

			</div>
		</div>

	{/if}
</div>
