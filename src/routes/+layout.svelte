<script lang='ts'>
	// The ordering of these imports is critical to your app working properly
	import '@skeletonlabs/skeleton/themes/theme-crimson.css';
	// If you have source.organizeImports set to true in VSCode, then it will auto change this ordering
	import '@skeletonlabs/skeleton/styles/all.css';
	// Most of your app wide CSS should be put in this file
	import '../app.postcss';
	import { AppShell, AppBar } from '@skeletonlabs/skeleton';
	import MdSettings from 'svelte-icons/md/MdSettings.svelte';
	import MdPlayArrow from 'svelte-icons/md/MdPlayArrow.svelte';
	import MdPause from 'svelte-icons/md/MdPause.svelte';
</script>

<!-- App Shell -->
<AppShell>
	<svelte:fragment slot="header">
		<!-- App Bar -->
		<AppBar class="drop-shadow-sm">
			<svelte:fragment slot="lead">
				<strong class="text-xl">GroupGPT</strong>
			</svelte:fragment>
			<svelte:fragment slot="trail">
				<a
					class="btn btn-sm variant-ghost-surface"
					href="https://github.com/cauvmou/GroupGPT"
					target="_blank"
					rel="noreferrer"
				>
					GitHub
				</a>
			</svelte:fragment>
		</AppBar>
	</svelte:fragment>
	<svelte:fragment slot="sidebarLeft">
		<!-- Hidden below Tailwind's large breakpoint -->
		<div id="sidebar-left" class="hidden lg:block h-full flex justify-center items-center drop-shadow-md">

		</div>
	</svelte:fragment>
	<!-- Page Route Content -->
	<slot />
	<svelte:fragment slot="footer">
		<div class="w-full h-20 drop-shadow-sm z-50 flex flex-row items-center justify-between px-3">
			<button type="button" class="btn-icon variant-filled"><div class="w-[24px] h-[24px]"><MdSettings /></div></button>
			<input class="input" type="text" placeholder="Discuss the color of bananas..." />
			<button type="button" class="btn-icon variant-filled"><div class="w-[24px] h-[24px]"><MdPlayArrow /></div></button>
		</div>
	</svelte:fragment>
</AppShell>
