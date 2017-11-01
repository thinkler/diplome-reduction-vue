import Vue from 'vue';
import Vuex from 'vuex';
import Router from 'vue-router';
import BootstrapVue from 'bootstrap-vue';
import VueCharts from 'vue-charts';
import Chartkick from 'chartkick';
import VueChartkick from 'vue-chartkick';
import Chart from 'chart.js'; // eslint-disable-line 
import { sync } from 'vuex-router-sync';

import App from './App';
import VuexStore from './vuex/store';
import routes from './router/router-config';

Vue.use(VueChartkick, { Chartkick });
Vue.use(Vuex);
Vue.use(Router);
Vue.use(BootstrapVue);
Vue.use(VueCharts);

const store = new Vuex.Store(VuexStore);

const router = new Router({
  routes,
  mode: 'history',
});

sync(store, router);

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
