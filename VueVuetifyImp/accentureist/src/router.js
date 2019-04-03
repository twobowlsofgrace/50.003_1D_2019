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
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard
    },
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/createuser',
      name: 'createuser',
      component: Createuser
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile
    },
    {
      path: '/createticket',
      name: 'createticket',
      component: Createticket
    },
    {
      path: '/dashboarduser',
      name: 'dashboarduser',
      component: Dashboarduser
    }
  ]
})
