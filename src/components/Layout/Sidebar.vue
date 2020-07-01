<template>
    <div>
        <b-sidebar id="sidebar-variant" title="Repository" bg-variant="dark" text-variant="light" shadow backdrop="true">
            <div class="px-3 py-2" style="height:250px; overflow-y:scroll;">
                <div v-for="item in repository" v-bind:key="item.id" class="repository">
                    
                    <div style="display:flex;justifyContent:spaceBetween;">
                    <b-icon-list-task></b-icon-list-task>
                    
                    <span v-if="modify=='bfore_modify'" @click="modifyRepositoryName" class="repository_name">{{item.name}}</span>
                    <b-form-input v-else-if="modify=='modify'" v-model="repository_name" @keyup.enter="addRepository" class="repository_input_name" placeholder=""></b-form-input>
                    <span v-else class="repository_name">{{item.name}}</span>
                    

                                
                    </div>
                    <span class="complete_cnt" style=""> 2/{{item.task_cnt}}</span>
                </div> 
                
            </div>
            
            <div class="menu">
                
                <div class="menu_item" @click="showRepositoryInput=!showRepositoryInput">
                    <div style="display:flex;justifyContent:spaceBetween;">
                        
                        <b-icon-dash-circle-fill v-if="showRepositoryInput"></b-icon-dash-circle-fill>
                        <b-icon-plus-circle-fill v-else></b-icon-plus-circle-fill>
                        <span v-if="showRepositoryInput" class="repository_name">Close</span>
                        <span v-else class="repository_name">New List</span>

                    </div>
                </div>
                <b-form-input v-model="repository_name" @keyup.enter="addRepository" v-if="showRepositoryInput" class="repository_input_name" placeholder=""></b-form-input>
                
                <div class="menu_item" @click="modify=true">
                    <div style="display:flex;justifyContent:spaceBetween;">
                        <b-icon-pencil-square></b-icon-pencil-square>
                        <span class="repository_name">Modify Repository Name</span>
                    </div>
                </div>

                <div class="menu_item" @click="showRepositoryInput=!showRepositoryInput">
                    <div style="display:flex;justifyContent:spaceBetween;">
                        <b-icon-trash></b-icon-trash>
                        <span class="repository_name">Remove Repository</span>
                    </div>
                </div>
                
            </div>

        </b-sidebar>
        
        
        
        
        
    </div>
</template>

<script>
export default {
    name:'Sidebar',
    data:()=>{
        return{
            showRepositoryInput:false,
            repository_name:"",
            repository:[],
            modify:null

        }
    },
    beforeCreate(){

        this.$store.dispatch('getRepository').then(res=>{
                this.repository=res   
        })
        
        
    },
    methods:{
        addRepository(){
            this.showRepositoryInput=false
            this.$store.dispatch('addRepository',{
                name:this.repository_name
            }).then(()=>{
                // console.log(res)
                this.repository_name=""
                
                this.$store.dispatch('getRepository').then(res=>{
                    this.repository=res   
                })
            })
        },
        modifyRepositoryName(){
            alert('modify!')
            

        }  
    }
    
}
</script>

<style scoped>
    .repository{
      display:flex;
      justify-content:space-between;
      cursor: pointer;
      margin-top:10px;
    }
    .repository > span{
      margin-top: -4px;
    }
    .repository_name{
      width: 220px;
      height: 20px;
      text-align: left;
      margin-top:-4px;
      margin-left:10px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .complete_cnt{
      float: right;
    }
    .menu{
      border-top:1px solid rgb(216, 213, 213);
    
    }
    .menu_item{
      display:flex;
      justify-content:space-between;
      cursor: pointer;
      margin-top:20px;
      margin-left:10px;
    }
    .repository_input_name{
        border:none;
        margin:10px;
        width: 300px;
        height: 25px;
    }


</style>