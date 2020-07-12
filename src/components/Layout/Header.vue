<template>
    <div class='header d-flex flex-column flex-md-row align-items-center p-4 px-md-5 mb-5 bg-white border-bottom shadow-sm'>
        <!-- <router-link :to="{ name: 'Home'}"><font-awesome-icon style="marginRight:20px; width:50px;height:50px;" icon="clipboard-list" /></router-link> -->
        <font-awesome-icon v-b-toggle.sidebar-variant style="marginRight:20px; width:50px;height:50px;" icon="clipboard-list" />
        
        <!-- <router-link class="title my-0 mr-md-auto font-weight-bold h2" :to="{ name: 'Home'}">
            TODO List
        </router-link> -->
        <div @click="goHome" class="title my-0 mr-md-auto font-weight-bold h2">
            TODO List
        </div>
        
        
        <!-- <h5 class="title my-0 mr-md-auto font-weight-bold h2">Clawsome</h5> -->
        <nav class="my-2 my-md-0 mr-md-3">
        </nav>
        <router-link v-if="this.$store.state.isAuthenticated" v-b-modal.modal-footer-sm class="btn btn-outline-danger btn-lg mr-4" :to="{ name: 'Home'}">
            Logout
        </router-link>
        <router-link v-else class="btn btn-outline-primary btn-lg mr-4" :to="{ name: 'Login'}">
            Login
        </router-link>
        <router-link class="btn btn-outline-primary btn-lg mr-4" :to="{ name: 'SignUp'}">
            Sign in
        </router-link>
        
        <b-modal @ok="handleOk" id="modal-footer-sm" title="Logout" button-size="sm">
            <p class="my-2">Are you sure you want to log out?</p>
        </b-modal>
    </div>
    
</template>

<script>
// import { mapGetters } from 'vuex';
export default {
    name:'Header',
    
    beforeCreate() {
        this.$store.dispatch('checkAuth')
    },
    methods:{
        showModal() {
            this.$refs['modal-footer-sm'].show()
        },
        handleOk(){
            this.$cookies.remove('token')
            window.location.href='/'
        },
        goHome(){
            window.location.href='/'
        }
    }
}
</script>

<style scoped>
    .title{
        color: rgb(88, 88, 86);
        text-decoration: none;
        cursor: pointer;
    }
    img.site_icon{
        width: 60px;
        height: 60px;
        margin-right: 20px
    }
   

</style>