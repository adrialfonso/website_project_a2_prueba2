import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/components/HomePage'
import SignUp from '@/components/SignUp'
import LogIn from '@/components/LogIn'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/account',
      name: 'SignUp',
      component: SignUp
    },
    {
      path: '/login',
      name: 'LogIn',
      component: LogIn
    }

  ]
})
