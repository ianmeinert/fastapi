<script>
    import SvelteTable from "svelte-table";

    const data = [
        { id: 1, name: 'Finish this website', days_until_alert: '1', date_added: '9/11/2021' },
        { id: 2, name: 'Run the demo', days_until_alert: '6', date_added: '9/11/2021' }
    ];

    const headers = [{
        key: "id",
        title: "ID",
        value: v => v.id
    },
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

</script>

<SvelteTable columns="{headers}" rows="{data}" />