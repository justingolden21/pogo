<script>
	import pokedex from '../data/pokedex.json';

	let id = 0;
	$: pokemon = pokedex[id];
</script>

<svelte:head>
	<title>{pokemon.name}</title>
</svelte:head>

<p class="mt-4 text-left">#{id}</p>
<h1>{pokemon.name}</h1>
<button on:click={() => (id = id + 1)}>Next</button>
