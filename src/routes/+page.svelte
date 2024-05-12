<script>
	import { onMount } from 'svelte';
	import { typewriter } from './transition.ts';

	const words = [
		'essay',
		'project',
		'presentation',
		'homework',
		'assignment',
		'paper',
		'work'
	];


	let i = -1;

	onMount(() => {
		const interval = setInterval(() => {
			i = (i + 1) % words.length;
		}, 2500);

		return () => clearInterval(interval);
	});

</script>

<svelte:head>
	<title>Research Tool</title>
	<meta name="description" content="Research faster with the power of AI" />
</svelte:head>

<section class=" relative w-full flex  items-center justify-center h-full">
	<div class=" mb-16 flex flex-col">
		<h1 class="text-5xl text-center font-bold w-full">Research <span class="underline decoration-wavy underline-offset-8 decoration-4 bg-gradient-to-r from-blue-600 via-green-500 to-indigo-400 inline-block text-transparent bg-clip-text decoration-blue-600">Faster</span></h1>

		<p class="text-center text-lg font-semibold mt-4">[name] helps you research for your
			{#key i}<span in:typewriter={{speed:4}} class="text-transparent bg-clip-text bg-gradient-to-r from-red-600 to-orange-400">{words[i] || ''}</span>{/key}
		</p>


	</div>

	<div class="absolute bottom-0 left-0 w-full p-4 h-20 text-xl font-bold text-black/50 flex items-center">
		<p class="text-center ">Created by </p>
		<div class="ml-1 underline  decoration-blue-500 hover:text-black/70">Neel P</div>
	</div>

	<div class="blur-2xl">
		<div class="absolute  bottom-0 left-0 w-full h-20 bg-gradient-to-r from-blue-600 via-green-500 to-indigo-400 opacity-50"></div>
	</div>



</section>

