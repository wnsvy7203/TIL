import Vue from 'vue'
import VueRouter from 'vue-router'
import TheLotto from '@/views/TheLotto'
import TheLunch from '@/views/TheLunch'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'lunch',
    component: TheLunch
    // component: () => import('@/views/TheLunch')  // lazy loading 
  },
  {
    path: '/lotto/:lunchMenu',
    name: 'lotto',
    component: TheLotto
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
