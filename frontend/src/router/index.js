import Vue from "vue"
import VueRouter from "vue-router"
import IndexView from "@/views/IndexView.vue"
import DetailView from "@/views/DetailView.vue"

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "index",
    component: IndexView,
  },
  {
    path: "/detail/:tmdb_id",
    name: "detail",
    component: DetailView,
    // component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  // {
  //   path: "/community",
  //   name: "comunity",
  //   component: DetailView,
  // },
  // {
  //   path: "/post/:article_pk",
  //   name: "comunity",
  //   component: DetailView,
  // },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

export default router
