<script>
import { onMount } from "svelte";
import ProductRow from "./ProductRow.svelte";

export let userEnteredData;
onMount(() => {
  if (userEnteredData.length == 0) {
    insert_empty_product();
  }
});

function insert_empty_product() {
  //   console.log("insert_empty_product", userEnteredData[subcategory]);
  //   products = [...products, { title: "", quantity: 0, unit: "running_meter" }];
  userEnteredData = [...userEnteredData, { title: "", quantity: "", unit: "running_meter" }];
}
</script>

<!-- table with
מוצר
כמות
יח מידה
-->
<table>
  <thead>
    <tr>
      <th>מוצר</th>
      <th>יח מידה</th>
      <th>אורך</th>
      <th>רוחב</th>
      <th>עובי</th>
      <th>חומר גלם</th>
      <th>משקל</th>
    </tr>
  </thead>
  <tbody>
    {#each userEnteredData as product, i}
      <ProductRow bind:product {i} />
    {/each}
    <button on:click={insert_empty_product}>הוסף מוצר</button>
  </tbody>
</table>

<style>
/* :global(tr) {
  border: 1px solid black;
} */
:global(table tr) {
  box-shadow: 0 0 4px #000;
}
/*
table,
th,
:global(td) {
  border: 1px solid black;
} */
</style>
