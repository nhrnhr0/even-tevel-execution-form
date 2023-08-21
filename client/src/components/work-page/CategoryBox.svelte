<script>
export let category;
export let index = -1;
export let selected_index = -1;
// trigger category selected event

const handleClick = () => {
  selected_index = index;
};
</script>

<div class="category-box" on:click={handleClick} class:selected={selected_index == index}>
  <div class="inner-wraper">
    <h3>{category.title}</h3>
    <img src={category.image} alt="" width="100%" height="100%" />
  </div>
</div>

<style lang="scss">
.category-box {
  padding-bottom: 10px;
  img {
    width: 100%;
    height: 100%;
  }
  h3 {
    margin: 0;
    padding: 0;
  }
}
.category-box.selected {
  color: white;
  background-color: #333;
}
</style>
