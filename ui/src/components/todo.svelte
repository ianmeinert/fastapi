<script>
    import SvelteTable from "svelte-table";
    import { onMount } from 'svelte';
    import { getTodoList } from "../services/api/todo"
   
    let data = [];

    let headers = [
    {
        key: "name",
        title: "Task title",
        value: v => v.name
    },
    {
        key: "date_added",
        title: "Date added",
        value: v => v.date_added
    },
    {
        key: "days_until_alert",
        title: "Days until alert",
        value: v => v.days_until_alert
    }];


    // Get the data from the api, after the page is mounted.
    onMount(async () => {
        data = await getTodoList();
    });

</script>

<SvelteTable columns="{headers}" rows="{data}" />