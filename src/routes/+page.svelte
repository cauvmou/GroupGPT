<script lang="ts">
	import Bubble from "$lib/components/Bubble.svelte";
    import type { IUser } from "$lib/types";

    const test_data: Array<{user: IUser, content: string}> = [
        {
            user: {
                name: "Funny Turtle",
                description: "Likes turtles",
                color: 0xc9a2fe,
            },
            content: "Hello, I like turtles!",
        },
        {
            user: {
                name: "Animal Lover",
                description: "Likes all animals equally",
                color: 0x8ebf8a,
            },
            content: "Turtles are so cool man!",
        }
    ]
</script>

<div class="w-full h-full overflow-hidden flex justify-center items-start">
    <div class="w-full h-full">
        {#each test_data as data}
            <Bubble user={data.user} content={data.content} />
        {/each}
    </div>
</div>