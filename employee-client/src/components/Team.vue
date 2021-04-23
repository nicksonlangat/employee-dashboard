<template>
  <div class="team">
     <div class="team-members table">
         <div class="table-header table-row">
             <div class="table-col">Name</div>
             <div class="table-col">Email</div>
             <div class="table-col">Phone</div>
             <div class="table-col">Department</div>
             <div class="table-col">Salary</div>
             <div class="table-col table-actions">Actions</div>
         </div>
         <div class="table-row">
             <div class="table-col name">Nicky Adams</div>
             <div class="table-col email">realnickyadams@gmail.com</div>
             <div class="table-col name">0713754946</div>
             <div class="table-col name">Software Dept</div>
             <div class="table-col name">Kshs 100,000</div>
             <div class="table-col actions">
                 <div class="button-group group-end">
                     <div class="button button-small">update</div>
                     <div class="button button-small button-alert">delete</div>
                 </div>
             </div>
         </div>
         <div class="table-row">
             <div class="table-col name">Nicky Adams</div>
             <div class="table-col email">realnickyadams@gmail.com</div>
             <div class="table-col name">0713754946</div>
             <div class="table-col name">Software Dept</div>
             <div class="table-col name">Kshs 100,000</div>
             <div class="table-col actions">
                 <div class="button-group group-end">
                     <div class="button button-small">update</div>
                     <div class="button button-small button-alert">delete</div>
                 </div>
             </div>
         </div>
     </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
.team{
    padding: 16px;

}
.table-row{
    display: flex;
    align-items: center;
}
.table-col{
    flex: 1 1 33.333%;
    padding: 16px;
    color: var(--grey);
}
.table-row{
    background-color: #FFFFFF;
}
.table-row:nth-child(2n+1){
    background-color: var(--light-alt);
}
.table .table-header{
    background-color: var(--dark);
}
.table .table-header .table-col{
    color: var(--light);
}
.table-actions{
    text-align: right;
}
</style>