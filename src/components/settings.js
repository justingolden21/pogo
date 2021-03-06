import { localStore } from './localStore.js';

export const defaultSettings = {
	pokemonID: 1,

	darkMode: null // overridden in _layout onMount to user device's preference
};

// deep copy to preserve original defaultSettings
export const settings = localStore('settings', JSON.parse(JSON.stringify(defaultSettings)));
