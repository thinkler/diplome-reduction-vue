import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/Home';
import DataBefore from '@/components/DataBefore';
import Results from '@/components/Results';
import Comparing from '@/components/Comparing';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/data-before',
      name: 'Data Before',
      component: DataBefore,
    },
    {
      path: '/results',
      name: 'Results',
      component: Results,
    },
    {
      path: '/comparing',
      name: 'Comparing',
      component: Comparing,
    },
  ],
});
