import Vue from 'vue'
import Router from 'vue-router'

import Home from '../components/Pages/Home'
import Login from '../components/Pages/Login'
import SignUp from '../components/Pages/SignUp'


// 뷰 어플리케이션에 라우터 플러그인을 추가함
Vue.use(Router)

const router = new Router({
    mode: 'history',
    routes: [
        {
            path:'/',
            name:'Home',
            component:Home
        },
        {
            path:'/login',
            name:'Login',
            component:Login
        },
        {
            path:'/signup',
            name:'SignUp',
            component:SignUp
        }

    ]

})

export default router;