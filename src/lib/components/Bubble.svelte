<script lang="ts">
    import { Role } from "$lib/types";

    export let role: Role;
    export let content: string;
</script>

<div class="
    w-full 
    {role != Role.USER ? "bg-surface-600" : ""} 
    flex justify-center items-center flex-col
    p-3">
    <span class="lg:w-[1010px] w-full text-surface-400 capitalize"><b><i>{role}</i></b></span>
    <div class="lg:w-[1010px] w-full py-1">
        <p>{content}</p>
    </div>
</div>