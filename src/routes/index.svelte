<script>
	import pokedex from '../data/pokedex.json';

	import { settings } from '../components/settings';

	import AutoComplete from 'simple-svelte-autocomplete';

	$: id = $settings.pokemonID;
	$: pokemon = pokedex.filter((p) => p.dex === id)[0];

	let pokemonNames = pokedex.map((key) => key.name);
</script>

<svelte:head>
	<title>{pokemon.name}</title>
</svelte:head>

<!-- todo: autofocus, onclick select all, css updates -->
<AutoComplete
	items={pokemonNames}
	hideArrow
	selectedItem={pokemon.name}
	onChange={(val) => ($settings.pokemonID = pokedex.filter((p) => p.name === val)[0].dex)}
/>

<img
	src={`https://img.pokemondb.net/sprites/home/normal/${pokemon.name
		.replace('East Sea', 'East')
		.replace('West Sea', 'West')
		.replace('Cherrim Sunny', 'Cherrim Sunshine')
		.replace('Alola', 'Alolan')
		.replace('Galar', 'Galarian')
		.replace(' ', '-')
		.replace('.', '')
		.toLowerCase()}.png`}
	alt={pokemon.name}
/>

<p class="mt-4 text-left">#{id}</p>
<h1>{pokemon.name}</h1>
<button on:click={() => $settings.pokemonID--}>Prev</button>
<button on:click={() => $settings.pokemonID++}>Next</button>
