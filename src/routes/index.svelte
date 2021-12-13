<script>
	import pokedex from '../data/pokedex.json';

	let id = 1;
	$: pokemon = pokedex.filter((p) => p.dex === id)[0];
</script>

<svelte:head>
	<title>{pokemon.name}</title>
</svelte:head>

<img
	src={`https://img.pokemondb.net/sprites/home/normal/${pokemon.name
		.replace(' ', '-')
		.replace('.', '')
		.toLowerCase()}.png`}
	alt={pokemon.name}
/>

<p class="mt-4 text-left">#{id}</p>
<h1>{pokemon.name}</h1>
<button on:click={() => id--}>Prev</button>
<button on:click={() => id++}>Next</button>
