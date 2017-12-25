import Home from '@/components/Home';
import DataBefore from '@/components/DataBefore';
import Results from '@/components/Results';
import Comparing from '@/components/Comparing';
import Statistics from '@/components/Statistics';
import Method from '@/components/Method';

export default [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/method',
    name: 'method',
    component: Method,
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
  {
    path: '/stats',
    name: 'stats',
    component: Statistics,
  },
];
