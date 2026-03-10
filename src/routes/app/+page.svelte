<svelte:head>
	<title>Research Tool</title>
	<meta name="description" content="Research faster with the power of AI" />
</svelte:head>

<script lang="ts">
	import { Icon, MagnifyingGlass, PaperAirplane } from "svelte-hero-icons";
	import {fetchSummary} from "./fetchSummary.ts";

	let input = '';
	let summaryData: Promise<any> | null = null;

	function submitSearch() {
		if (!input.trim()) return;
		summaryData = fetchSummary(input);
	}

	function handleKeydown(event: KeyboardEvent) {
		if (event.key === 'Enter') {
			submitSearch();
		}
	}

	function formatDate(dateStr: string | null): string | null {
		if (!dateStr) return null;
		try {
			const d = new Date(dateStr);
			if (isNaN(d.getTime())) return null;
			return d.toLocaleDateString();
		} catch {
			return null;
		}
	}
</script>

<div class="w-[calc(100%-64px)] flex flex-col h-[calc(100%-64px)] m-8 border border-gray-200 rounded-xl bg-white">
	<!-- Search bar always visible at the top -->
	<div class="w-full p-6 border-b border-gray-100">
		<div class="w-full md:w-2/3 mx-auto bg-gradient-to-r from-orange-400 to-red-500 rounded-full p-0.5">
			<div class="flex items-center justify-start bg-white rounded-full p-4">
				<Icon src="{MagnifyingGlass}" class="w-6 h-6 text-gray-500"/>
				<input bind:value={input} on:keydown={handleKeydown} placeholder="What do you want to research?" class="flex-grow mx-4 outline-none"/>
				<button on:click={submitSearch}>
					<Icon src="{PaperAirplane}" class="w-6 h-6 text-green-500 hover:fill-green-500"/>
				</button>
			</div>
		</div>
	</div>

	<!-- Results area -->
	<div class="flex-grow overflow-y-auto p-4">
		{#if summaryData}
			{#await summaryData}
				<div class="flex items-center justify-center h-full">
					<p class="text-2xl text-center text-gray-500">Loading articles...</p>
				</div>
			{:then data}
				{#if data && Array.isArray(data) && data.length > 0}
					{#each data as article}
						<div class="rounded-xl bg-gray-100 p-4 m-4">
							<div class="flex flex-row justify-between items-start mb-2">
								<h2 class="text-xl font-bold">{article.title}</h2>
								<a href="{article.url}" target="_blank" rel="noopener noreferrer"
								   class="text-sm font-semibold text-blue-500 hover:text-blue-400 ml-4 shrink-0 underline">
									Visit Article
								</a>
							</div>
							<p class="text-base text-gray-700 mb-3">{article.summary}</p>
							{#if article.keywords && article.keywords.length > 0}
								<div class="flex flex-wrap gap-2 mb-2">
									{#each article.keywords as keyword}
										<span class="bg-blue-100 text-blue-700 text-xs px-2 py-1 rounded-full">{keyword}</span>
									{/each}
								</div>
							{/if}
							{#if article.authors && article.authors.length > 0}
								<p class="text-xs text-gray-500">By {article.authors.join(', ')}</p>
							{/if}
							{#if article.publish_date && formatDate(article.publish_date)}
								<p class="text-xs text-gray-400 mt-1">{formatDate(article.publish_date)}</p>
							{/if}
						</div>
					{/each}
				{:else}
					<div class="flex items-center justify-center h-full">
						<p class="text-2xl text-center text-gray-400">No results found</p>
					</div>
				{/if}
			{:catch error}
				<div class="flex items-center justify-center h-full">
					<p class="text-2xl text-center text-red-500">Error: {error.message}</p>
				</div>
			{/await}
		{:else}
			<div class="flex items-center justify-center h-full">
				<p class="text-gray-400 text-lg">Enter a topic above to start researching</p>
			</div>
		{/if}
	</div>
</div>
