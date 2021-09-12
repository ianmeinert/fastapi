<script>
    import SvelteTable from "svelte-table";
    import { onMount } from 'svelte';
    import { getTodoList } from "../services/api/todo"
   
    let data = [];

    let headers = [
    {
        key: "title",
        title: "Task title",
        value: v => v.title
    },
    {
        key: "completed",
        title: "Completed",
        value: v => v.completed
    }];


    // Get the data from the api, after the page is mounted.
    onMount(async () => {
        data = await getTodoList();
    });

</script>

<SvelteTable columns="{headers}" rows="{data}" />