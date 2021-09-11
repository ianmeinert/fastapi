import App from './App.svelte';

const app = new App({
	target: document.body,
	props: {
		name: 'Tasklist Organizer'
	}
});

export default app;