<template>
  <div class="home">
    <TodoList/>
    <!-- <b-sidebar  class="" id="sidebar-footer" title="Tasks" shadow backdrop > -->
      
        <Sidebar/>
      

     <!-- </b-sidebar> -->
  

  </div>
  
</template>
<script>
import TodoList from '../Layout/TodoList'
import Sidebar from '../Layout/Sidebar'
export default {
    name:'Home',  
    components:{
      TodoList,
      Sidebar
    }
}
</script>
<style scoped>
    .home{
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        background: #f5f5f5;
    }
    


</style>