import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store/index.js'
import IndexView from '@/views/IndexView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import CommunityView from '@/views/CommunityView.vue'
import PostDetailView from '@/views/PostDetailView.vue'
import PostCreateView from '@/views/PostCreateView.vue'
import PostUpdateView from '@/views/PostUpdateView.vue'
import ProfileView from '@/views/ProfileView.vue'
import SearchView from '@/views/SearchView.vue'
import NotFound404 from '@/views/NotFound404.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexView,
  },
  {
    path: '/movie/:movieId',
    name: 'movieDetail',
    component: MovieDetailView,
    // component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView,
  },
  {
    path: '/community/create',
    name: 'createPost',
    component: PostCreateView,
    beforeEnter(to, from, next) {
      if (store.getters.isLogin) {
        next()
      } else {
        alert('로그인 해주세요')
        store.commit('TOGGLE_LOGIN_MODAL', true)
      }
    },
  },
  {
    path: '/post/:postId/update',
    name: 'updatePost',
    component: PostUpdateView,
    beforeEnter(to, from, next) {
      if (store.getters.isLogin) {
        next()
      } else {
        alert('로그인 해주세요')
        store.commit('TOGGLE_LOGIN_MODAL', true)
      }
    },
  },
  {
    path: '/post/:postId',
    name: 'postDetail',
    component: PostDetailView,
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView,
    beforeEnter(to, from, next) {
      if (store.getters.isLogin) {
        next()
      } else {
        alert('로그인 해주세요')
        store.commit('TOGGLE_LOGIN_MODAL', true)
      }
    },
  },
  {
    path: '/search/:query',
    name: 'search',
    component: SearchView,
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404,
  },
  {
    path: '*',
    redirect: '/404',
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch((err) => {
    if (err.name !== 'NavigationDuplicated') throw err
  })
}

export default router
