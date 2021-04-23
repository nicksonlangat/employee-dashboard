<template>
  <div class="toolbar">
      <h2>Employees</h2>
      <div class="button-group">
          <div class="button">Add employee</div>
         <div class="button button-outline">Export employees</div>
      </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
.toolbar{
    padding: 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.toolbar h2{
    color: var(--dark);
    font-size: 32px;
    font-weight: 400;
    text-transform: uppercase;
}
</style>