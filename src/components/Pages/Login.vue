<template>
  <div class="login">
      <h1 class="h2 mb-3 font-weight-bold" style="color:#2c3e50;">Please sign in</h1>
      <h5 class="text-danger" v-if="loginError">아이디 또는 패스워드가 맞지 않습니다</h5>
      <div class="form-signin">
        <label for="inputEmail" class="sr-only">Email address</label>
        <input @focus="loginError=false" @keyup.enter="handleSubmit" v-model="loginData.username" type="email" id="inputEmail" class="form-control" placeholder="ID" required="" autofocus="">
        <label for="inputPassword" class="sr-only">Password</label>
        <input @focus="loginError=false"  @keyup.enter="handleSubmit" v-model="loginData.password" type="password" id="inputPassword" class="form-control" placeholder="Password" required="">
        <button @click="handleSubmit"   class="btn btn-lg btn-primary btn-block font-weight-bold mt-4">Sign in</button>
      </div>
  </div>
</template>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>

<script>

export default {
    name:'Login',
    data:()=>({
        loginData:{
            username:"",
            password:""
        },
        loginError:false
        
    }),
    methods:{

        async handleSubmit(){
            this.$store.dispatch('login',this.loginData)
            .then(res=>{
                if(res=='success'){
                    window.location.href='/'
                }
                else this.loginError=true   
            })
        }
    }
}

</script>
<style scoped>
    .login{
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        margin-top: 10%;
        background: #f5f5f5;
    }
    .form-signin{
        width:100%;
        max-width: 420px;
        padding: 15px;
        margin:auto;
        
    }
    /* .form-signin input[type="email"]{
        margin-bottom: -1px;
        height: auto;
        padding: 10px;   
    } */
    .form-control{
        font-weight:500;
        margin-bottom: 5px;
        height: 65px;
        padding: 10px;
        font-size: 19px;


    }

</style>