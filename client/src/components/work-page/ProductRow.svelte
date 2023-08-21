<script>
import { createEventDispatcher } from "svelte";
import { page } from "$app/stores";

const dispatch = createEventDispatcher();
export let product;
export let i;

function delete_row() {
  dispatch("delete-row", i);
}

const UNIT_OPTIONS = {
  running_meter: "מטר רץ",
  square_meter: "מטר רבוע",
  unit: "יחידה",
  pack: "חבילה",
};

function recalculate_material() {
  debugger;
  // product.material = product.height * product.width * product.depth;
  if (product.unit == "running_meter") {
    // product.running_meter_cut = 12
    // product.width = 15
    // product.height = 10
    // product.material = 24 * 10
    // 24 is Math.ceil(15 / 12)
    product.material = Math.ceil(product.width / product.running_meter_cut) * product.height;
  } else if (product.unit == "square_meter") {
    product.material = product.height * product.width;
  } else if (product.unit == "unit") {
    product.material = product.quantity * product.height * product.width;
  } else if (product.unit == "pack") {
    product.material = product.quantity * product.pack_size;
  }
  recalculate_weight();
}

function recalculate_weight() {
  if (product.depth != null && product.depth != -1) {
    product.weight = product.material * $page.data.weights[product.depth].weight;
  }
}
</script>

<tr>
  <td>
    <input type="text" bind:value={product.title} />
  </td>
  <td>
    <select bind:value={product.unit} on:change={recalculate_material}>
      {#each Object.keys(UNIT_OPTIONS) as unit}
        <option value={unit} selected={product.unit == unit}>{UNIT_OPTIONS[unit]}</option>
      {/each}
    </select>
    {#if product.unit == "running_meter"}
      <br />
      <label for="running_meter_cut"
        >רוחב חתיכה
        {#if product.running_meter_cut > 0 && product.width > 0}
          (מטר רץ: {Math.ceil(product.width / product.running_meter_cut) * product.running_meter_cut})
        {/if}
        <!-- {Math.ceil(product.width / product.running_meter_cut) * product.running_meter_cut} -->
      </label>
      <input type="number" id="running_meter_cut" bind:value={product.running_meter_cut} />
    {:else if product.unit == "square_meter"}
      <!-- <span>מטר רבוע</span> -->
      <br /><br /><br />
    {:else if product.unit == "unit"}
      <!-- <span>יחידה</span> -->
      <label for="quantity">כמות</label>
      <input type="number" bind:value={product.quantity} on:input={recalculate_material} name="quantity" />
    {:else if product.unit == "pack"}
      <div class="wraper" style="display: grid;grid-template-columns: 1fr 1fr;grid-template-rows: 1fr 1fr;">
        <label for="pack_size">כמות בחבילה</label>
        <label for="qyantity">כמות חבילות</label>

        <input type="number" id="qyantity" bind:value={product.quantity} on:input={recalculate_material} />
        <input type="number" id="pack_size" bind:value={product.pack_size} on:input={recalculate_material} />
      </div>
    {/if}
  </td>
  <td>
    <input type="number" bind:value={product.height} on:input={recalculate_material} />
  </td>
  <td>
    <input type="number" bind:value={product.width} on:input={recalculate_material} />
  </td>
  <td>
    <!-- <input type="number" bind:value={product.depth} on:input={recalculate_material} /> -->
    <!-- $page.data.weights -->
    <select bind:value={product.depth} on:change={recalculate_weight}>
      {#each $page.data.weights as weight, inx}
        <option value={inx}>{weight.depth}</option>
      {/each}
    </select>
    <!-- {product.depth} -->
    {#if product.depth != null && product.depth != -1}
      <span>{$page.data.weights[product.depth].weight} ק"ג למ"ר</span>
    {/if}
  </td>
  <td>
    {#if product.unit == "running_meter"}
      <span>מטר רץ x אורך</span>
    {:else if product.unit == "square_meter"}
      <span>אורך x רוחב </span>
    {:else if product.unit == "unit"}
      <span>כמות x אורך x רוחב = </span>
    {:else if product.unit == "pack"}
      <span>כמות בחבילה x כמות חבילות</span>
    {/if}
    <input type="number" step="0.01" bind:value={product.material} on:change={recalculate_weight} />
  </td>
  <td>
    <span>חומר גלם x משקל לעובי</span>
    <input type="number" step="0.01" bind:value={product.weight} />
  </td>
  <td>
    <button on:click={delete_row}>מחק</button>
  </td>
</tr>
