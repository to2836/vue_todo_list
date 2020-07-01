<template>
    <div class="sub_task_modal">
        <b-modal
            id="modal-sm"
            size="sm"
            title="Sub Task"
            ok-title="Add"
            centered
            @hide="resetSubTask"
            @cancel="resetSubTask"
            @close="resetSubTask"
            @ok="addSubTask"
            >
            <b-form-input @keyup.enter="addSubTask" v-model="sub_task" class="bv_input" id="desc" list="my-list-id"></b-form-input>
        </b-modal>
    </div>
</template>


<script>
// import { mapGetters } from 'vuex';

export default {
    name:'SubTaskModal',
    data:function(){
        return{
            sub_task:""
        }
    },
    methods:{
        addSubTask:function(){
            this.$emit('send_sub_task', this.sub_task)
            this.sub_task=""

        },
        resetSubTask:function(){
            this.sub_task=""
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
        margin:20px;
        margin-bottom: 50px;
    }
    .sub_task{
        margin:10px;
    }
</style>