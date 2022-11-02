import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import( '../views/LoginView.vue')
  },
  {
    path: '/reg/:remindMode',
    name: 'Reg',
    component: () => import( '../views/RegView.vue'),    
    props: true
  },
  {
    path: '/setting/:id',
    name: 'Single',
    component: () => import( '../components/Single.vue'),
    props: true
  },
  {
    path: '/secure',
    name: 'Secure',
    component: () => import( '../components/Secure.vue'),
    meta: { 
     // requiresAuth: true
    }
  },
  {
    path: '/news',
    name: 'News',
    component: () => import( '../components/News.vue'),
    meta: { 
     // requiresAuth: true
    }
  },
  {
    path: '/news/:id',
    name: 'NewsOne',
    component: () => import( '../components/NewsOne.vue'),
    props: true
  },
  {
    path: '/news/update/:id',
    name: 'NewsUpdate',
    component: () => import( '../components/NewsUpdate.vue'),
    props: true
  },
  {
    path: '/news/addNews',
    name: 'AddNews',
    component: () => import('../components/AddNews.vue')
  },
  {
    path: '/staff',
    name: 'Staff',
    component: () => import( '../components/Staff.vue'),
    meta: { 
     // requiresAuth: true
    }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'Page404',
    component: () => import('../views/Page404.vue')
  },
  {
    path: '/reset_password/:uid/:token',
    name: 'Reset_password',
    component: () => import('../views/ResetPassword.vue')
  },
]

const router = createRouter({
  mode:history,
  history: createWebHashHistory(),
  routes
})
/*
router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isLoggedIn) {
      next()
      return
    }
    next('/login') 
  } else {
    next() 
  }
})//*/

router.beforeEach((to, from, next) => {
  const access_token = localStorage.getItem('access_token')
  console.log(to.name)

  if(!access_token){ //Если НЕ авторизован
    // Список страниц разрешенных для неавторизованных
   if (to.name === 'Login'
    || to.name === 'About'
    || to.name === 'Home'
    || to.name === 'Staff'    
    || to.name === 'Page404'
    || to.name === 'Reg'
    || to.name === 'Reset_password'){

    return next()

   }else{
    // иначе переходим на страницу логина
    return next({
      name:'Login'
    }) 

    //  if(to.name ==='Home' || to.name ==='Staff'){
    //   return next()
    //  }else{
    //     return next({
    //       name:'Login'
    //     })
    //   }
    }
  }

  // Если авторизован, то не показывать страницу ввода логина, перейти в ЛК (или домашнюю)
  if(to.name == 'Login' && access_token){
    return next({
      name: 'Secure'
    })
  }
  next()
})

export default router
