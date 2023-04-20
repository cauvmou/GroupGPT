<script lang="ts">
	import type { IUser } from '$lib/types';

	export let user: IUser;
	export let content: string;
</script>

<div
	class="
    w-full
    flex justify-center items-center flex-col border-l-4
    p-3"
	style="background-color: #{user.color.toString(16)}0f; border-color: #{user.color.toString(16)}"
>
	<span class="lg:w-[1010px] w-full capitalize" style="color: #{user.color.toString(16)}"
		><b><i>{user.name}</i></b></span
	>
	<div class="lg:w-[1010px] w-full py-1">
		<p>{content}</p>
	</div>
</div>
