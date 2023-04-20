<script lang="ts">
	import MdSettings from 'svelte-icons/md/MdSettings.svelte';
	import MdPlayArrow from 'svelte-icons/md/MdPlayArrow.svelte';
	import MdSend from 'svelte-icons/md/MdSend.svelte';
	import MdPause from 'svelte-icons/md/MdPause.svelte';
	import MdArrowBack from 'svelte-icons/md/MdArrowBack.svelte';

	import { onMount } from 'svelte';
	import type { LayoutServerData } from '../../routes/$types';

	export let data: LayoutServerData;
</script>

<div class="w-full h-24 flex flex-row justify-center">
	<div class="lg:w-[1010px] w-full drop-shadow-sm z-50 flex flex-row items-center justify-between">
		<!-- svelte-ignore a11y-click-events-have-key-events -->
		{#key data.pathname}
			{#if data.pathname == '/'}
				<a href="/settings" class="btn-icon variant-filled mx-2 w-[52px]"
					><div class="w-[24px] h-[24px]"><MdSettings /></div></a
				>
			{:else}
				<a href="/" class="btn-icon variant-filled mx-2 w-[52px]"
					><div class="w-[24px] h-[24px]"><MdArrowBack /></div></a
				>
			{/if}
		{/key}
		<input class="input mx-2" type="text" placeholder="Discuss the color of bananas..." />
		<button type="button" class="btn-icon variant-filled mx-2 w-[52px]"
			><div class="w-[24px] h-[24px]"><MdSend /></div></button
		>
		<button type="button" class="btn-icon variant-filled mx-2 w-[52px]"
			><div class="w-[28px] h-[28px]"><MdPlayArrow /></div></button
		>
	</div>
</div>
