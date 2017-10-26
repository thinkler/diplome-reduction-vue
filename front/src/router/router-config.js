import Home from '@/components/Home';
import DataBefore from '@/components/DataBefore';
import Results from '@/components/Results';
import Comparing from '@/components/Comparing';

export default [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/data-before',
    name: 'dataBefore',
    component: DataBefore,
  },
  {
    path: '/results',
    name: 'results',
    component: Results,
  },
  {
    path: '/comparing',
    name: 'comparing',
    component: Comparing,
  },
];
