import Vue from 'vue'
import VueRouter from 'vue-router'
import Authorization from '../views/Authorization'
import BaseContent from '../views/BaseContent'
import Registration from '../views/Registration'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Authorization',
    component: Authorization
  },
  {
    path: '/',
    name: 'BaseContent',
    component: BaseContent
  },
  {
    path: '/',
    name: 'Registration',
    component: Registration
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
