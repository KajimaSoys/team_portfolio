import { createRouter, createWebHistory } from 'vue-router'

import ProjectsView from "../views/ProjectsView.vue";
import SoloProject from "../views/SoloProject.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/projects',
      alias: '/',
      name: 'main',
      component: ProjectsView
    },
    {
      path: '/projects/:id',
      // component: () => import('../views/SoloProject.vue'),
      component: SoloProject,
      name: 'projects',
    }
  ],

})
export default router
