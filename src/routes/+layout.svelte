<script>
	import Header from './Header.svelte';
	import './styles.css';
</script>

<div class="w-full h-screen flex flex-col">
	<Header />

	<main class="w-full flex-grow inset-0 bg-white bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px]">
		<slot />
	</main>

</div>

