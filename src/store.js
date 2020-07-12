// store.js
import Vue from "vue";
import Vuex from "vuex";
import request from './helper/request'
import VueCookies from 'vue-cookies'
import router from './router'

// import { mapState } from 'vuex';
// import { mapGetters } from 'vuex';
// import { mapMutations } from 'vuex';
// import { mapActions } from 'vuex';


Vue.use(Vuex);

export default new Vuex.Store({
  state:{
    isAuthenticated: false,
  },
  mutations:{
      LOGIN(state){
        state.isAuthenticated = true
      },
      LOGOUT(state){
        state.isAuthenticated = false
        router.push('/login')
      },
  },
  actions:{
      login(state,payload){
        return request({
            url:'/apiv1/login',
            method:'post',
            data:payload
        }).then(res=>{
            VueCookies.set('token',res)
            this.commit('LOGIN')
            return 'success'
        }).catch(()=>'error')
      },
      checkAuth(){
        console.log(VueCookies.get('token'))
        return request({
            url:'/apiv1/token/verify',
            method:'post',
            data:VueCookies.get('token')
          }).then(()=>{
            this.commit('LOGIN')
        }).catch(()=>{
            this.commit('LOGOUT')
        })
      },
      getTaskList(){
        return request({
          url:'/apiv1/task'
        }).then(res=>{
          // console.log(res)
          return res
        }).catch(e=>{
          console.log(e)
        })
      },
      sendTaskData(state, payload){
        console.log('JWT '+VueCookies.get('token').token)
        return request({
          url:'/apiv1/task',
          method:'post',
          // headers:{
          //   Authorization: 'JWT '+VueCookies.get('token').token
          // },
          data:payload
        }).then(res=>{
          console.log(res)
          window.location.href='/'
        }).catch(e=>{
          console.log(e)
        })
      },
      updateTaskComplete(state, payload){
        console.log(payload)
        return request({
          url:'/apiv1/task/update',
          method:'patch',
          data:payload
        }).then(res=>{
          console.log(res)
          router.push('/')

        }).catch(e=>{
          console.log(e)
        })
      },
      removeTask(state, payload){
        return request({
          url:'/apiv1/task/remove/'+payload.id,
          method:'delete',
        }).then(res=>{
          console.log(res)
          router.push('/')
        })
      },
      addRepository(state, payload){
        return request({
          url:'/apiv1/repository',
          method:'post',
          data:payload
        }).then(()=>{
          // console.log(res)
        })
      },
      getRepository(){
        return request({
          url:'/apiv1/repository',
          method:'get'
        }).then(res=>{
          return res
        })
      }

  }
});

