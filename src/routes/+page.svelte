<script lang="ts">
	import Bubble from "$lib/components/Bubble.svelte";
    import { Role } from "$lib/types";

    const test_data = [
        {
            role: Role.ASSISTANT,
            content: "Hello, I am an assistant."
        },
        {
            role: Role.USER,
            content: "Hello, I am a user."
        }
    ]
</script>

<div class="w-full h-full overflow-hidden flex justify-center items-start">
    <div class="w-full h-full">
        {#each test_data as data}
            <Bubble role={data.role} content={data.content} />
        {/each}
    </div>
</div>