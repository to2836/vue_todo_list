<template>
    <div class="todo_list">
        <header class="todo_list_header">
            <div class="date_group">
                <h5 class="date"><span>Monday</span>,<span>10th</span></h5>
                <h6 class="day">December</h6>   
            </div>
            <div class="task_count_group">
                <h7><span class="task_count">12</span> Tasks</h7>
            </div>
        </header>
        <div class="add_btn_group">
            <div class="top">
             <img v-b-modal.modal-center @click="beforeOpenCreateModal" class="add_btn" src="../../assets/add_btn.png" alt="add button">
            </div>
            <div class="bottom"></div>
        </div>

        <div class="list-group" style="width:100%;backgroundColor:white;">
            <div class="items" v-for="(task, index) in tasks" v-bind:key="task.id"> 
                <div class="left">
                    <b-form-checkbox
                        v-if="tasks[index].complete"
                        class="check"
                        checked="true"
                        style="float:left;"
                        :ref="'checkbox'+index"
                        :id="'checkbox-'+index"
                        :name="'checkbox-'+index"
                        @change="handleCheckbox($event, index)"
                        value="true"
                        unchecked-value="false">
                        <span v-if="tasks[index].complete" style="text-decoration:line-through;" class="list-group-item">{{task.name}}</span>
                        <span v-else class="list-group-item">{{task.name}}</span>
                    </b-form-checkbox>
                    <b-form-checkbox
                        v-else
                        class="check"
                        checked="false"
                        style="float:left;"
                        :ref="'checkbox'+index"
                        :id="'checkbox-'+index"
                        :name="'checkbox-'+index"
                        @change="handleCheckbox($event, index)"
                        value="true"
                        unchecked-value="false">
                        <span v-if="tasks[index].complete" style="text-decoration:line-through;" class="list-group-item">{{task.name}}</span>
                        <span v-else class="list-group-item">{{task.name}}</span>
                    </b-form-checkbox> 
                </div>
               
                <div class="right">
                    <b-icon-pencil-square @click="beforeOpenModifyModal(index)" v-b-modal.modal-center style="cursor:pointer;marginRight:5px;"></b-icon-pencil-square>
                    <b-icon-trash @click="removeTask(index)" style="cursor:pointer;marginLeft:10px;"></b-icon-trash>
                </div>
                
            </div>
            
        </div>
        
        <TaskModal v-bind:get_task_data="passData"></TaskModal>
        
        
        
    
    </div>

  
</template>

<script>
// import { mapGetters } from 'vuex';
import TaskModal from '../Layout/TaskModal'

export default {
    name:'TodoList',
    data:function(){
        return{
            tasks:[],
            passData:{}
        }
    },
    beforeCreate(){
        this.$store.dispatch('getTaskList').then(res=>{
            // console.log(res)
            // for(var obj in res){
            //     // alert(res[obj]
            //     this.tasks.push(res[obj])
            // }
            this.tasks=res
            console.log(this.tasks)
        })
    },
    methods:{
        addTask:()=>{
           
        },
        removeTask:function(i){
            console.log(this.tasks[i].id)
            if(confirm('Are you sure you want to remove this task?')){
                
                this.$store.dispatch('removeTask',{
                    'id':this.tasks[i].id
                }).then(()=>{
                    this.tasks.splice(i, 1);
                })
            }

        },
        handleCheckbox:function(e,i){
            if(e=="true") this.tasks[i].complete=true
            else this.tasks[i].complete=false    
            this.$store.dispatch('updateTaskComplete',{
                'complete':this.tasks[i].complete,
                'id':this.tasks[i].id
            })
        },
        beforeOpenModifyModal:function(i){
            this.passData = {data:this.tasks[i], modify:true}
        },
        beforeOpenCreateModal:function(){
            this.passData = {data:[], modify:false}
        }
    },

    components:{
        TaskModal
    }
}
</script>

<style scoped>
    .todo_list{
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        margin: 0 auto;
        width:40%;
        background-color: rgb(173, 211, 211);
        height:100%;
        border-radius: 30px;
    }
    .todo_list_header{
        width:100%;
        height: 50px;
        /* text-align: center; */
        padding:70px;
        
    }
    .list-group{
        border-radius: 0px 0px 30px 30px;
    }
    .date_group{
        width:100%;
        height: 100%;;
    }
    .date{
        text-align: left;
    }
    .day{
        text-align: left;
    }
    .task_count_group{
        color: rgb(102, 99, 99);
        text-align: right;
        font-weight: 900;
    }
    .add_btn_group{
        background-color: white;
        text-align: right;
        /* padding-right:30px;   */
    }
    .add_btn_group > .top{
        background-color: rgb(173, 211, 211);
        height: 35px;
    }
    .add_btn_group > .bottom{
        background-color: rgb(252, 253, 253);
        height: 40px;
    }
    .add_btn{
        width: 70px;
        height: 70px;
        margin-right: 40px;
        cursor: pointer;
        outline:none;
    }
   
    .items{
        display: flex;
        justify-content: space-between;
        border-bottom:0.1px solid #bcbcbc;
        word-wrap:break-word;
    }
    .items > .left{
    }

    .items > .right{
        display: flex;
        justify-content: space-between;
        margin:30px 15px 10px 15px;
    }

    .items:last-child{
        border:none;
    }
    .check{
        margin-left: 20px;
        margin-top: 25px;
    }
    .list-group-item{
        border:none;
        word-break: break-all;
        padding:0px 0px 20px 10px;
        
    }
   

   
    
   
   

</style>