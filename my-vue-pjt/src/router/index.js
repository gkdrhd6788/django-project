import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MovieListView from '../views/MovieListView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import ReviewSearchView from '../views/ReviewSearchView.vue'
import RecommendedView from '../views/RecommendedView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
        path: '/movies',
        name: 'movieList',
        component: MovieListView
      },
      {
        path: '/:movieId',
        name: 'movieDetail',
        component: MovieDetailView
      },
      {
        path: '/review-search',
        name: 'reviewSearch',
        component: ReviewSearchView
      },
      {
        path: '/recommended',
        name: 'recommended',
        component: RecommendedView
      },
    
  ]
})

export default router
