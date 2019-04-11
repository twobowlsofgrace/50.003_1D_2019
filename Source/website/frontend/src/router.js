import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from './views/Dashboard'
import Login from './views/Login'
import Createuser from './views/Createuser'
import Profile from './views/Profile'
import Createticket from './views/Createticket'
import Dashboarduser from './views/Dashboarduser'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login
    }
  ]
})
