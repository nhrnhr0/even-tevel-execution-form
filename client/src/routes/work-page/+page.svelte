<script>
import { page } from "$app/stores";
import CategoryBox from "../../components/work-page/CategoryBox.svelte";
import EditProductTable from "../../components/work-page/EditProductTable.svelte";

let selected_category_index = -1;
let selected_subcategory_index = -1;
let userEnteredData = [];

function selected_category_changed(e) {
  selected_category_index = e.detail;
}
$: {
  selected_category_index;
  selected_subcategory_index = -1;
}
</script>

<!-- $page.data":{"categories":[{"id":2,"title":"444","image":"http://127.0.0.1:8000/media/category/%D7%97%D7%93%D7%A9_%D7%9C%D7%9C%D7%90_%D7%91%D7%A9%D7%A8.png","subcategories":[{"id":1,"title":"777","image":"http://127.0.0.1:8000/media/subcategory/Untitled.png"},{"id":2,"title":"bbbb","image":"http://127.0.0.1:8000/media/subcategory/Capture.PNG"}]},{"id":3,"title":"tttt","image":"http://127.0.0.1:8000/media/category/%D7%97%D7%98%D7%99%D7%A3_%D7%A2%D7%9D_%D7%A9%D7%99%D7%91%D7%95%D7%9C%D7%AA_%D7%A9%D7%95%D7%A2%D7%9C.jpg","subcategories":[{"id":3,"title":"bbn","image":"http://127.0.0.1:8000/media/subcategory/whatsapp_1_1.png"}]}]}} -->
<!-- prefech all categories and subcategories images -->
{#each $page.data.categories as category, i}
  {#each category.subcategories as subcategory, j}
    <prefetch href={subcategory.image} as="image" />
  {/each}
  <prefetch href={category.image} as="image" />
{/each}

<div class="page-wraper">
  <div class="categories-grid-wraper">
    {#each $page.data.categories as category, i}
      <CategoryBox {category} bind:selected_index={selected_category_index} index={i} />
    {/each}
  </div>
  <!-- {JSON.stringify(selected_category_index)} -->

  {#if selected_category_index != -1}
    <div class="subcategories-grid-wraper">
      {#each $page.data.categories[selected_category_index].subcategories as subcategory, i}
        <CategoryBox category={subcategory} index={i} bind:selected_index={selected_subcategory_index} />
      {/each}
    </div>
  {/if}

  {#if selected_subcategory_index != -1}
    <EditProductTable bind:userEnteredData />
  {/if}

  <!-- {JSON.stringify(userEnteredData)} -->
</div>

<style lang="scss">
.categories-grid-wraper,
.subcategories-grid-wraper {
  background-color: #eee;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 10px;
  margin: 10px;
}

.page-wraper {
  direction: rtl;
  max-width: 1000px;
  margin: auto;
  margin-top: 50px;
}
</style>
