<template>
    <div class="task_modal">
        <b-modal
            id="modal-center"
            centered title="Task"
            ok-title="Save"
            hide-header="true"
            @hide="resetTask"
            @cancel="resetTask"
            @show="openModal"
            @close="resetTask"
            @ok="sendTaskData">
        
            <!-- task -->
            <div class="modal_data task_name">
                <b-icon-arrow-right-square></b-icon-arrow-right-square>
                <!-- <font-awesome-icon style="width:20px;height:20px;" icon="sticky-note"/> -->
                <span>  Task Name</span>
                <b-form-input  v-if="!create_name" @blur="checkName" v-model="name" class="bv_input" id="desc" list="my-list-id"></b-form-input>
                <div v-if="create_name">
                    <div @click="removeTask()" style="width:20px;height:20px;float:right;cursor:pointer;">
                        <font-awesome-icon icon="times" style="marginLeft:4px;marginBottom:2px;"/> 
                    </div>
                    <b-form-checkbox
                        class="sub_task"
                        id='checkbox1'
                        name='checkbox1'
                        :checked="task_checked"
                        @change="handleTaskCheckbox($event)"
                        value="true"
                        unchecked-value="false">
                        <span v-if="create_name&&task_checked" style="word-wrap: break-word;display:inline-block;width:350px;text-decoration:line-through;">{{name}}</span>
                        <span v-else-if="create_name&&!task_checked" style="word-wrap: break-word;display:inline-block;width:350px;">{{name}}</span>

                    </b-form-checkbox>
                </div>
            
            </div>
            
            <!-- notes -->
            <div class="modal_data">
                <b-icon-chat-square ></b-icon-chat-square>
                <!-- <font-awesome-icon style="width:20px;height:20px;" icon="comment"/> -->
                <span>  Notes</span>
                <!-- <b-form-input v-model="notes" class="bv_input" id="desc" list="my-list-id"></b-form-input> -->
                <b-form-textarea
                    id="textarea"
                    v-model="notes"
                    placeholder="Enter something..."
                    rows="2"
                    max-rows="6"
                    ></b-form-textarea>
            </div>
            <!-- sub task -->
            <div class="modal_data">
                <b-icon-list-check></b-icon-list-check>
                <!-- <font-awesome-icon style="width:20px;height:20px;" icon="list"/> -->
                <span>  Sub Tasks </span>
                <font-awesome-icon v-b-modal.modal-sm style="width:22px;height:22px;float:right;cursor:pointer;" icon="plus-circle"/>
                <div v-for="(item, index) in sub_tasks" v-bind:key="item.id">
                    <div @click="removeSubTask($event,index)" style="width:20px;height:20px;float:right;cursor:pointer;">
                        <font-awesome-icon icon="times" style="marginLeft:4px;marginBottom:2px;"/> 
                    </div>
                    <b-form-checkbox
                    :checked="item.checked"
                    class="sub_task"
                    :ref="'subTaskCheckbox'+index"
                    :id="'subcheckbox-'+index"
                    :name="'subcheckbox-'+index"
                    @change="handleCheckbox($event, index)"
                    value="true"
                    unchecked-value="false">
                    <span v-if="computedSubTask(index)" style="word-wrap: break-word;display:inline-block;width:350px;text-decoration:line-through;">{{item.title}}</span>
                    <span style="word-wrap: break-word;display:inline-block;width:350px;" v-else>{{item.title}}</span>
                    </b-form-checkbox>
                    
                </div>
            </div>
            <!-- {{get_task_data}} -->
        </b-modal>
        <SubTaskModal @send_sub_task="getSubTask" />
    </div>
</template>

<script>
// import { mapGetters } from 'vuex';
import SubTaskModal from '../Layout/SubTaskModal'

export default {
    name:'TaskModal',
    props:[
        'get_task_data'
    ],
    data:function(){
        return{
            id:null,
            name:"",
            notes:"",
            sub_tasks:[],
            create_name:false,
            task_checked:false,
            
            
        }
    },
    computed:{
        computedSubTask(){    
            return (i)=>{
                return this.sub_tasks[i].checked
            }
        }
    },
    components:{
        SubTaskModal
    },
    methods:{
        getSubTask: function(message) {
            this.sub_tasks.push({checked:false,title:message})
        },
        resetTask:function(){
            this.id=null
            this.notes=""
            this.sub_tasks=[]
            this.name=""
            this.create_name=false
            this.task_checked=false

        },
        handleCheckbox:function(e, i){
            

            if(e=="true"){
                this.sub_tasks[i].checked=true
            }
            else{
                this.sub_tasks[i].checked=false
            }
        },
        handleTaskCheckbox:function(e){

            if(e=="true"){
                this.task_checked=true
            }
            else{
                this.task_checked=false
            }

        },
        removeSubTask:function(e, i){
            this.sub_tasks.splice(i, 1);
        },
        sendTaskData:function(){
        
            if(this.get_task_data.modify){
                this.$store.dispatch('sendTaskData',{
                    id : this.id,
                    task : this.name,
                    task_checked : this.task_checked,
                    notes : this.notes,
                    sub_tasks : this.sub_tasks
                })
            }
            else{
                this.$store.dispatch('sendTaskData',{
                    task : this.name,
                    task_checked : this.task_checked,
                    notes : this.notes,
                    sub_tasks : this.sub_tasks
                })

            }
            
            
        },
        checkName:function(){
            if(this.name==""){
                this.create_name=false
            }
            else{
                this.create_name=true
            }
        },
        removeTask:function(){
            this.name=""
            this.create_name=false
            this.task_checked=false 

        },
        openModal:function(){
            if(this.get_task_data.modify){
                this.id=this.get_task_data.data.id
                this.name=this.get_task_data.data.name
                if(this.name!="")this.create_name=true
                this.notes=this.get_task_data.data.notes
                this.task_checked=this.get_task_data.data.complete
                for(var i in this.get_task_data.data.sub_task){
                    this.sub_tasks.push({
                    id:this.get_task_data.data.sub_task[i].id,
                    title:this.get_task_data.data.sub_task[i].name,
                    checked:this.get_task_data.data.sub_task[i].complete})
                }
            }
        }
    }
}
</script>


<style scoped>

    .bv_input{
        border-right: none;
        border-left: none;
        border-top: none;
    }
    .modal_data{
        padding:20px;
        padding-bottom: 50px;
    }
    .task_name{
        padding-top:40px;
    }
   
    .modal_data > span{
        margin-left: 5px;
    }
    .sub_task{
        margin:10px;
    }
</style>


