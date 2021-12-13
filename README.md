# svelte-tailwind-boilerplate

### Code

A svelte kit boilerplate using tailwind css with eslint / prettier / airbnb formatting and styling. It supports netlify as a backend. It is also meant to support multiple page websites and PWAs. Supports i18n. Supports dark mode. Set up to use svg icons; currently using hero icons.

### Setup

`npm i`

##### Styling:

VS Code Extensions:

- Auto Rename Tag

- ESLint

- Path Intellisense

- PostCSS Language Support

- Prettier

- Svelte 3 Snippets

- Svelte for VS Code

- Tailwind CSS Intellisense

- Tailwind Docs

Set up VS code to auto format on save

1. Open preferences (ctrl+shift+P)

2. Preferences: Open Settings (JSON)

3. Add the following:

```json
{
	"prettier.singleQuote": true,
	"prettier.tabWidth": 4,
	"prettier.useTabs": true,
	"editor.formatOnSave": true,
	"[html]": {
		"editor.defaultFormatter": "vscode.html-language-features"
	},
	"[javascript]": {
		"editor.defaultFormatter": "esbenp.prettier-vscode"
	},
	"[svelte]": {
		"editor.defaultFormatter": "svelte.svelte-vscode"
	},
	"eslint.alwaysShowStatus": true
}
```

### Development

First time setup: `npm i`

Generate Assets: `npm run generate-assets`

Development: `npm run dev`

Build: `npm run build`

Preview: `npm run preview`

Note that `build` and `preview` must be run once before having service worker working for `dev`

### Info

Primary red: #DC2626 (red-600)

Primary gray: #27272A (gray-800)

Note that if a bug appears and doesn't go away even after deleting build folders and node modules etc, it may be in local storage and can be reset by `localStorage.clear()` in the console
