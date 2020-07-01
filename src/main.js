import Vue from 'vue'
import VueSession from 'vue-session'
import App from './App.vue'
import  store  from "./store";

import {BootstrapVue, BootstrapVueIcons} from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import router from './router'
import axios from 'axios'
import VueCookies from 'vue-cookies'

//font awasome
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(fas)
library.add(far)

Vue.component('font-awesome-icon', FontAwesomeIcon)

// import checkAuth from './plugins/checkAuth'


axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(VueSession)
// Vue.use(checkAuth)
Vue.use(VueCookies)

Vue.config.productionTip = false
Vue.prototype.$http = axios
new Vue({
  render: h => h(App),
  router,
  store
}).$mount('#app')
