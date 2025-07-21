import Vue from 'vue';
import Router from 'vue-router';
import UserRegister from '../components/UserRegister.vue';
import UserLogin from '../components/UserLogin.vue';
import TodoList from '../components/TodoList.vue';

Vue.use(Router);

const routes = [
  {
    path: '/register',
    name: 'UserRegister',
    component: UserRegister
  },
  {
    path: '/login',
    name: 'UserLogin',
    component: UserLogin
  },
  {
    path: '/todos',
    name: 'TodoList',
    component: TodoList
  }
];

const router = new Router({
  mode: 'history',
  routes
});

export default router;
