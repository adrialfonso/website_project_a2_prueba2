import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/views/HomePage'
import SignUp from '@/views/SignUp'
import LogIn from '@/views/LogIn'
import store from '@/store/store'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage,
      meta: {auth: false}
    },
    {
      path: '/signup',
      name: 'SignUp',
      component: SignUp,
      meta: {
        auth: false
      }
    },
    {
      path: '/login',
      name: 'LogIn',
      component: LogIn,
      meta: {
        auth: false
      }
    }

  ]
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = store.state.username !== ''

  if (to.matched.some(record => record.meta.auth)) {
    if (!isAuthenticated) {
      next('/login')
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
